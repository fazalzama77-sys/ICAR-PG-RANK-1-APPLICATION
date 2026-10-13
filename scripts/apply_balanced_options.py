# scripts/apply_balanced_options.py
import json
import os
import random
import sys
from collections import Counter

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')


def apply_balance():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    packs_dir = os.path.join(base_dir, "..", "src", "data", "questionPacks")

    def load_pack(name):
        with open(os.path.join(packs_dir, name), "r", encoding="utf-8") as f:
            return json.load(f)

    base_json = load_pack("high_yield_clean_base.json")     # 565
    pyqs_json = load_pack("pyqs_300.json")                  # 350
    vpp_exp1_json = load_pack("vpp_300_new.json")           # 300
    vmc_exp1_json = load_pack("vmc_300_new.json")           # 300
    van_exp_json = load_pack("van_150_new.json")            # 150
    vpa_exp_json = load_pack("vpa_60_new.json")             # 60
    vpp_exp2_json = load_pack("vpp_350_part2.json")         # 350
    vmc_exp2_json = load_pack("vmc_350_part2.json")         # 350
    ann_exp_json = load_pack("ann_250_new.json")            # 350
    agb_exp_json = load_pack("agb_250_new.json")            # 350

    all_questions = (
        base_json
        + pyqs_json
        + vpp_exp1_json
        + vmc_exp1_json
        + van_exp_json
        + vpa_exp_json
        + vpp_exp2_json
        + vmc_exp2_json
        + ann_exp_json
        + agb_exp_json
    )

    print(f"Loaded total {len(all_questions)} questions across 10 source packs.")
    assert len(all_questions) == 3125, f"Expected 3,125 questions, got {len(all_questions)}"

    # Check ID uniqueness
    ids = set()
    for q in all_questions:
        if q["id"] in ids:
            raise ValueError(f"Duplicate ID found: {q['id']}")
        ids.add(q["id"])

    # Check Stem uniqueness across all 3,125 questions
    stems = {}
    dup_stems = []
    for q in all_questions:
        norm = " ".join(q["questionText"].lower().split())
        if norm in stems:
            dup_stems.append((q["id"], stems[norm], q["questionText"][:80]))
        else:
            stems[norm] = q["id"]
    if dup_stems:
        print(f"WARNING: Found {len(dup_stems)} duplicate stems:")
        for d in dup_stems:
            print("  DUP:", d)

    # Group by subject and balance A/B/C/D options
    subjects = sorted(list(set(q["subjectId"] for q in all_questions)))
    shuffled_map = {}

    for s in subjects:
        subj_qs = [q for q in all_questions if q["subjectId"] == s]
        subj_qs.sort(key=lambda x: x["id"])
        n = len(subj_qs)

        blocks = []
        rng_subj = random.Random(f"subject_balance_v5_{s}")
        for _ in range(0, n, 4):
            block = [0, 1, 2, 3]
            rng_subj.shuffle(block)
            blocks.extend(block)
        target_indices = blocks[:n]

        for q, target_idx in zip(subj_qs, target_indices):
            old_idx = q["correctOptionIndex"]
            correct_text = q["options"][old_idx]
            distractors = [opt for i, opt in enumerate(q["options"]) if i != old_idx]

            rng_q = random.Random(f"q_distractor_v5_{q['id']}")
            rng_q.shuffle(distractors)

            new_opts = [None] * 4
            new_opts[target_idx] = correct_text
            d_idx = 0
            for i in range(4):
                if i != target_idx:
                    new_opts[i] = distractors[d_idx]
                    d_idx += 1

            assert new_opts[target_idx] == correct_text
            assert sorted(new_opts) == sorted(q["options"])

            q_updated = dict(q)
            q_updated["options"] = new_opts
            q_updated["correctOptionIndex"] = target_idx
            shuffled_map[q["id"]] = q_updated

    total_counts = Counter(q["correctOptionIndex"] for q in shuffled_map.values())
    print("Balanced A/B/C/D option distribution across all 3,125 questions:", dict(total_counts))

    def map_list(q_list):
        return [shuffled_map[q["id"]] for q in q_list]

    updated_base = map_list(base_json)
    updated_pyqs = map_list(pyqs_json)
    updated_vpp_exp1 = map_list(vpp_exp1_json)
    updated_vmc_exp1 = map_list(vmc_exp1_json)
    updated_van_exp = map_list(van_exp_json)
    updated_vpa_exp = map_list(vpa_exp_json)
    updated_vpp_exp2 = map_list(vpp_exp2_json)
    updated_vmc_exp2 = map_list(vmc_exp2_json)
    updated_ann_exp = map_list(ann_exp_json)
    updated_agb_exp = map_list(agb_exp_json)

    updated_vpp_all_exp = updated_vpp_exp1 + updated_vpp_exp2  # 650
    updated_vmc_all_exp = updated_vmc_exp1 + updated_vmc_exp2  # 650

    # Save JSON files
    def save_pack(name, data):
        with open(os.path.join(packs_dir, name), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    save_pack("high_yield_1080.json", updated_base)
    save_pack("high_yield_clean_base.json", updated_base)
    save_pack("pyqs_300.json", updated_pyqs)
    save_pack("vpp_300_new.json", updated_vpp_exp1)
    save_pack("vmc_300_new.json", updated_vmc_exp1)
    save_pack("van_150_new.json", updated_van_exp)
    save_pack("vpa_60_new.json", updated_vpa_exp)
    save_pack("vpp_350_part2.json", updated_vpp_exp2)
    save_pack("vmc_350_part2.json", updated_vmc_exp2)
    save_pack("ann_250_new.json", updated_ann_exp)
    save_pack("agb_250_new.json", updated_agb_exp)

    master_2925 = (
        updated_base
        + updated_pyqs
        + updated_vpp_all_exp
        + updated_vmc_all_exp
        + updated_van_exp
        + updated_vpa_exp
        + updated_ann_exp
        + updated_agb_exp
    )
    save_pack("high_yield_master_1380.json", master_2925)
    save_pack("high_yield_master_clean.json", master_2925)

    print(f"Saved all JSON packs (Master total: {len(master_2925)}).")

    # Split Core PYQs
    van_pyqs = [q for q in updated_pyqs if q["subjectId"] == "van"]
    vpp_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vpp"]
    vmc_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vmc"]
    vbc_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vbc"]

    assert len(van_pyqs) == 50
    assert len(vpp_pyqs) == 100
    assert len(vmc_pyqs) == 100
    assert len(vbc_pyqs) == 100
    assert len(updated_vpp_all_exp) == 650
    assert len(updated_vmc_all_exp) == 650
    assert len(updated_van_exp) == 150
    assert len(updated_vpa_exp) == 60
    assert len(updated_ann_exp) == 350
    assert len(updated_agb_exp) == 350

    # Write src/data/questionPacks/pyqQuestions.ts
    pyq_ts_path = os.path.join(packs_dir, "pyqQuestions.ts")
    with open(pyq_ts_path, "w", encoding="utf-8") as f:
        f.write("// ICAR AIEEA PG (M.V.Sc.) Official-Pattern Question Modules\n")
        f.write("// Core PYQs (350) + Expanded Pathology (650) + Expanded Microbiology (650) + Expanded Anatomy (150) + Expanded Parasitology (60) + Expanded Nutrition (350) + Expanded Genetics (350)\n")
        f.write("import { Question } from '../../types';\n\n")
        f.write("export const VAN_PYQ_QUESTIONS: Question[] = " + json.dumps(van_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VPP_PYQ_QUESTIONS: Question[] = " + json.dumps(vpp_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VMC_PYQ_QUESTIONS: Question[] = " + json.dumps(vmc_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VBC_PYQ_QUESTIONS: Question[] = " + json.dumps(vbc_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VPP_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_vpp_all_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VMC_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_vmc_all_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VAN_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_van_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VPA_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_vpa_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const ANN_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_ann_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const AGB_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_agb_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const ALL_ICAR_PG_PYQ_QUESTIONS: Question[] = [\n")
        f.write("  ...VAN_PYQ_QUESTIONS,\n")
        f.write("  ...VPP_PYQ_QUESTIONS,\n")
        f.write("  ...VMC_PYQ_QUESTIONS,\n")
        f.write("  ...VBC_PYQ_QUESTIONS,\n")
        f.write("  ...VAN_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...VPP_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...VMC_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...VPA_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...ANN_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...AGB_EXPANDED_QUESTIONS.filter(q => q.isPYQ)\n")
        f.write("];\n")
    print(f"Saved: {pyq_ts_path}")

    # Write src/data/questionPacks/allQuestions.ts
    all_ts_path = os.path.join(packs_dir, "allQuestions.ts")
    with open(all_ts_path, "w", encoding="utf-8") as f:
        f.write(f"// Autogenerated Master Question Bank ({len(updated_base)} Base + {len(updated_pyqs)} Core PYQs + {len(updated_vpp_all_exp)} VPP + {len(updated_vmc_all_exp)} VMC + {len(updated_van_exp)} VAN + {len(updated_vpa_exp)} VPA + {len(updated_ann_exp)} ANN + {len(updated_agb_exp)} AGB = {len(master_2925)} Total Verified)\n")
        f.write("import { Question } from '../../types';\n")
        f.write("import {\n")
        f.write("  ALL_ICAR_PG_PYQ_QUESTIONS,\n")
        f.write("  VAN_PYQ_QUESTIONS,\n")
        f.write("  VPP_PYQ_QUESTIONS,\n")
        f.write("  VMC_PYQ_QUESTIONS,\n")
        f.write("  VBC_PYQ_QUESTIONS,\n")
        f.write("  VAN_EXPANDED_QUESTIONS,\n")
        f.write("  VPP_EXPANDED_QUESTIONS,\n")
        f.write("  VMC_EXPANDED_QUESTIONS,\n")
        f.write("  VPA_EXPANDED_QUESTIONS,\n")
        f.write("  ANN_EXPANDED_QUESTIONS,\n")
        f.write("  AGB_EXPANDED_QUESTIONS\n")
        f.write("} from './pyqQuestions';\n\n")
        f.write("export {\n")
        f.write("  ALL_ICAR_PG_PYQ_QUESTIONS,\n")
        f.write("  VAN_PYQ_QUESTIONS,\n")
        f.write("  VPP_PYQ_QUESTIONS,\n")
        f.write("  VMC_PYQ_QUESTIONS,\n")
        f.write("  VBC_PYQ_QUESTIONS,\n")
        f.write("  VAN_EXPANDED_QUESTIONS,\n")
        f.write("  VPP_EXPANDED_QUESTIONS,\n")
        f.write("  VMC_EXPANDED_QUESTIONS,\n")
        f.write("  VPA_EXPANDED_QUESTIONS,\n")
        f.write("  ANN_EXPANDED_QUESTIONS,\n")
        f.write("  AGB_EXPANDED_QUESTIONS\n")
        f.write("};\n\n")
        f.write("const AUTHENTIC_BASE_QUESTIONS: Question[] = " + json.dumps(updated_base, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const ALL_HIGH_YIELD_QUESTIONS: Question[] = [\n")
        f.write("  ...AUTHENTIC_BASE_QUESTIONS,\n")
        f.write("  ...VAN_PYQ_QUESTIONS,\n")
        f.write("  ...VPP_PYQ_QUESTIONS,\n")
        f.write("  ...VMC_PYQ_QUESTIONS,\n")
        f.write("  ...VBC_PYQ_QUESTIONS,\n")
        f.write("  ...VAN_EXPANDED_QUESTIONS,\n")
        f.write("  ...VPP_EXPANDED_QUESTIONS,\n")
        f.write("  ...VMC_EXPANDED_QUESTIONS,\n")
        f.write("  ...VPA_EXPANDED_QUESTIONS,\n")
        f.write("  ...ANN_EXPANDED_QUESTIONS,\n")
        f.write("  ...AGB_EXPANDED_QUESTIONS\n")
        f.write("];\n")
    print(f"Saved: {all_ts_path} with {len(master_2925)} total questions.")


if __name__ == "__main__":
    apply_balance()
