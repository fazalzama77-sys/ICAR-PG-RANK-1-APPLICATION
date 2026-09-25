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

    with open(os.path.join(packs_dir, "high_yield_clean_base.json"), "r", encoding="utf-8") as f:
        base_json = json.load(f)

    with open(os.path.join(packs_dir, "pyqs_300.json"), "r", encoding="utf-8") as f:
        pyqs_json = json.load(f)

    with open(os.path.join(packs_dir, "vpp_300_new.json"), "r", encoding="utf-8") as f:
        vpp_exp_json = json.load(f)

    with open(os.path.join(packs_dir, "vmc_300_new.json"), "r", encoding="utf-8") as f:
        vmc_exp_json = json.load(f)

    with open(os.path.join(packs_dir, "van_150_new.json"), "r", encoding="utf-8") as f:
        van_exp_json = json.load(f)

    all_questions = base_json + pyqs_json + vpp_exp_json + vmc_exp_json + van_exp_json
    print(f"Loaded total {len(all_questions)} questions across 5 source packs (Base: {len(base_json)}, PYQs: {len(pyqs_json)}, VPP: {len(vpp_exp_json)}, VMC: {len(vmc_exp_json)}, VAN: {len(van_exp_json)}).")
    assert len(all_questions) == 1665, f"Expected 1,665 questions, got {len(all_questions)}"

    # Unique check
    ids = set()
    for q in all_questions:
        if q["id"] in ids:
            raise ValueError(f"Duplicate ID found: {q['id']}")
        ids.add(q["id"])

    # Group by subject and balance options
    subjects = sorted(list(set(q["subjectId"] for q in all_questions)))
    shuffled_map = {}

    for s in subjects:
        subj_qs = [q for q in all_questions if q["subjectId"] == s]
        subj_qs.sort(key=lambda x: x["id"])
        n = len(subj_qs)

        blocks = []
        rng_subj = random.Random(f"subject_balance_v3_{s}")
        for i in range(0, n, 4):
            block = [0, 1, 2, 3]
            rng_subj.shuffle(block)
            blocks.extend(block)
        target_indices = blocks[:n]

        for q, target_idx in zip(subj_qs, target_indices):
            old_idx = q["correctOptionIndex"]
            correct_text = q["options"][old_idx]
            distractors = [opt for i, opt in enumerate(q["options"]) if i != old_idx]

            rng_q = random.Random(f"q_distractor_v3_{q['id']}")
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
    print("New option distribution across all 1665 questions:", dict(total_counts))

    # Update individual lists
    updated_base = [shuffled_map[q["id"]] for q in base_json]
    updated_pyqs = [shuffled_map[q["id"]] for q in pyqs_json]
    updated_vpp_exp = [shuffled_map[q["id"]] for q in vpp_exp_json]
    updated_vmc_exp = [shuffled_map[q["id"]] for q in vmc_exp_json]
    updated_van_exp = [shuffled_map[q["id"]] for q in van_exp_json]

    # Save JSON files
    with open(os.path.join(packs_dir, "high_yield_1080.json"), "w", encoding="utf-8") as f:
        json.dump(updated_base, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "high_yield_clean_base.json"), "w", encoding="utf-8") as f:
        json.dump(updated_base, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "pyqs_300.json"), "w", encoding="utf-8") as f:
        json.dump(updated_pyqs, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vpp_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(updated_vpp_exp, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vmc_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(updated_vmc_exp, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "van_150_new.json"), "w", encoding="utf-8") as f:
        json.dump(updated_van_exp, f, indent=2, ensure_ascii=False)

    master_1665 = updated_base + updated_pyqs + updated_vpp_exp + updated_vmc_exp + updated_van_exp
    with open(os.path.join(packs_dir, "high_yield_master_1380.json"), "w", encoding="utf-8") as f:
        json.dump(master_1665, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "high_yield_master_clean.json"), "w", encoding="utf-8") as f:
        json.dump(master_1665, f, indent=2, ensure_ascii=False)

    print(f"Saved all JSON packs (Master total: {len(master_1665)}).")

    # Split PYQs
    van_pyqs = [q for q in updated_pyqs if q["subjectId"] == "van"]
    vpp_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vpp"]
    vmc_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vmc"]
    vbc_pyqs = [q for q in updated_pyqs if q["subjectId"] == "vbc"]

    assert len(van_pyqs) == 50
    assert len(vpp_pyqs) == 100
    assert len(vmc_pyqs) == 100
    assert len(vbc_pyqs) == 100
    assert len(updated_vpp_exp) == 300
    assert len(updated_vmc_exp) == 300
    assert len(updated_van_exp) == 150

    # Write src/data/questionPacks/pyqQuestions.ts
    pyq_ts_path = os.path.join(packs_dir, "pyqQuestions.ts")
    with open(pyq_ts_path, "w", encoding="utf-8") as f:
        f.write("// ICAR AIEEA PG (M.V.Sc.) Official-Pattern Question Modules\n")
        f.write("// Core PYQs (350) + Expanded Pathology (300) + Expanded Microbiology (300) + Expanded Anatomy (150)\n")
        f.write("import { Question } from '../../types';\n\n")
        f.write("export const VAN_PYQ_QUESTIONS: Question[] = " + json.dumps(van_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VPP_PYQ_QUESTIONS: Question[] = " + json.dumps(vpp_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VMC_PYQ_QUESTIONS: Question[] = " + json.dumps(vmc_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VBC_PYQ_QUESTIONS: Question[] = " + json.dumps(vbc_pyqs, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VPP_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_vpp_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VMC_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_vmc_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const VAN_EXPANDED_QUESTIONS: Question[] = " + json.dumps(updated_van_exp, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const ALL_ICAR_PG_PYQ_QUESTIONS: Question[] = [\n")
        f.write("  ...VAN_PYQ_QUESTIONS,\n")
        f.write("  ...VPP_PYQ_QUESTIONS,\n")
        f.write("  ...VMC_PYQ_QUESTIONS,\n")
        f.write("  ...VBC_PYQ_QUESTIONS,\n")
        f.write("  ...VAN_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...VPP_EXPANDED_QUESTIONS.filter(q => q.isPYQ),\n")
        f.write("  ...VMC_EXPANDED_QUESTIONS.filter(q => q.isPYQ)\n")
        f.write("];\n")
    print(f"Saved: {pyq_ts_path}")

    # Write src/data/questionPacks/allQuestions.ts
    all_ts_path = os.path.join(packs_dir, "allQuestions.ts")
    with open(all_ts_path, "w", encoding="utf-8") as f:
        f.write(f"// Autogenerated Master Question Bank ({len(updated_base)} Base + {len(updated_pyqs)} Core PYQs + {len(updated_vpp_exp)} VPP + {len(updated_vmc_exp)} VMC + {len(updated_van_exp)} VAN = {len(master_1665)} Total Verified)\n")
        f.write("import { Question } from '../../types';\n")
        f.write("import {\n")
        f.write("  ALL_ICAR_PG_PYQ_QUESTIONS,\n")
        f.write("  VAN_PYQ_QUESTIONS,\n")
        f.write("  VPP_PYQ_QUESTIONS,\n")
        f.write("  VMC_PYQ_QUESTIONS,\n")
        f.write("  VBC_PYQ_QUESTIONS,\n")
        f.write("  VAN_EXPANDED_QUESTIONS,\n")
        f.write("  VPP_EXPANDED_QUESTIONS,\n")
        f.write("  VMC_EXPANDED_QUESTIONS\n")
        f.write("} from './pyqQuestions';\n\n")
        f.write("export {\n")
        f.write("  ALL_ICAR_PG_PYQ_QUESTIONS,\n")
        f.write("  VAN_PYQ_QUESTIONS,\n")
        f.write("  VPP_PYQ_QUESTIONS,\n")
        f.write("  VMC_PYQ_QUESTIONS,\n")
        f.write("  VBC_PYQ_QUESTIONS,\n")
        f.write("  VAN_EXPANDED_QUESTIONS,\n")
        f.write("  VPP_EXPANDED_QUESTIONS,\n")
        f.write("  VMC_EXPANDED_QUESTIONS\n")
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
        f.write("  ...VMC_EXPANDED_QUESTIONS\n")
        f.write("];\n")
    print(f"Saved: {all_ts_path} with {len(master_1665)} total questions.")

    print("All datasets successfully balanced and updated!")

if __name__ == "__main__":
    apply_balance()
