# scripts/compile_pyqs.py
import json
import os
import sys
from collections import Counter

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from data_van import get_van_questions
from data_vpy import get_vpy_questions
from data_vbc import get_vbc_questions
from data_lpm import get_lpm_questions
from data_vpp import get_vpp_questions
from data_vmc import get_vmc_questions
from data_vpa import get_vpa_questions
from data_agb import get_agb_questions
from data_ann import get_ann_questions
from enrich_to_120 import SUPPLEMENTARY_POOLS

from pyq_van import get_van_pyqs
from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs

from build_pathology_300 import get_all_300_vpp_questions
from build_microbiology_300 import get_all_300_vmc_questions
from build_anatomy_150 import get_all_150_van_questions
from build_parasitology_60 import get_all_60_vpa_questions

from build_pathology_350_part2 import get_all_350_vpp_part2_questions
from build_microbiology_350_part2 import get_all_350_vmc_part2_questions
from build_nutrition_250 import get_all_250_ann_questions
from build_genetics_250 import get_all_250_agb_questions

from canonical_topics import map_question_to_canonical_unit, CANONICAL_UNITS
from option_parity_engine import equalize_question_bank_options


def is_dummy(q):
    q_text = q.get('questionText', '')
    topic = q.get('topic', '')
    opts = q.get('options', [])
    return (
        'Clinical Landmark MCQ #' in q_text
        or 'Core Diagnostic' in topic
        or any('Standard validated laboratory' in opt for opt in opts)
    )


def build_pure_base_565():
    vpy_initial = get_vpy_questions()
    vpy_supp = []
    for q_text, opts, ans, exp in SUPPLEMENTARY_POOLS.get('vpy', []):
        idx = len(vpy_initial) + len(vpy_supp) + 1
        vpy_supp.append({
            "id": f"vpy_q_{idx:03d}",
            "domain": "animal_science",
            "year": "1st_year",
            "subjectId": "vpy",
            "topic": "Veterinary Physiology High-Yield Core",
            "questionText": q_text,
            "options": list(opts),
            "correctOptionIndex": ans,
            "explanation": exp,
            "difficulty": "Medium",
            "tags": ["Veterinary Physiology", "ICAR PG Core"],
            "createdAt": 1773000000000 + idx
        })
    vpy_qs = vpy_initial + vpy_supp

    pools = [
        get_van_questions(),
        vpy_qs,
        get_vbc_questions(),
        get_lpm_questions(),
        get_vpp_questions(),
        get_vmc_questions(),
        get_vpa_questions(),
        get_agb_questions(),
        get_ann_questions(),
    ]

    clean_base = [q for qs in pools for q in qs if not is_dummy(q)]
    for q in clean_base:
        if q.get('subjectId') in ['vpy', 'vbc', 'lpm', 'agb', 'ann']:
            q['domain'] = 'animal_science'
        elif q.get('subjectId') in ['van', 'vpp', 'vmc', 'vpa']:
            q['domain'] = 'veterinary_science'
    assert len(clean_base) == 565, f"Expected 565 clean base questions, got {len(clean_base)}"
    return clean_base


def main():
    print("=========================================================================")
    print("COMPILING MASTER 3,125 QUESTION BANK FROM CLEAN PYTHON SOURCE GENERATORS")
    print("=========================================================================")

    clean_base = build_pure_base_565()          # 565
    van_pyqs = get_van_pyqs()                   # 50
    vpp_pyqs = get_vpp_pyqs()                   # 100
    vmc_pyqs = get_vmc_pyqs()                   # 100
    vbc_pyqs = get_vbc_pyqs()                   # 100
    all_core_pyqs = van_pyqs + vpp_pyqs + vmc_pyqs + vbc_pyqs  # 350

    new_vpp_300 = get_all_300_vpp_questions()   # 300
    new_vmc_300 = get_all_300_vmc_questions()   # 300
    new_van_150 = get_all_150_van_questions()   # 150
    new_vpa_60 = get_all_60_vpa_questions()     # 60

    new_vpp_350_p2 = get_all_350_vpp_part2_questions()  # 350
    new_vmc_350_p2 = get_all_350_vmc_part2_questions()  # 350
    new_ann_250 = get_all_250_ann_questions()           # 350
    new_agb_250 = get_all_250_agb_questions()           # 350

    master_raw = (
        clean_base
        + all_core_pyqs
        + new_vpp_300
        + new_vmc_300
        + new_van_150
        + new_vpa_60
        + new_vpp_350_p2
        + new_vmc_350_p2
        + new_ann_250
        + new_agb_250
    )

    print(f"Total Master Questions Assembled: {len(master_raw)}")
    assert len(master_raw) == 3125, f"Expected 3,125 questions, got {len(master_raw)}"

    # Map every question to its Canonical Syllabus Unit / Chapter (preserving subTopic)
    for q in master_raw:
        orig_topic = q.get("topic", "")
        canonical_unit = map_question_to_canonical_unit(q)
        if orig_topic and orig_topic != canonical_unit:
            q["subTopic"] = orig_topic
        q["topic"] = canonical_unit

    # Verify all topics belong to CANONICAL_UNITS
    for q in master_raw:
        subj = q["subjectId"]
        assert q["topic"] in CANONICAL_UNITS[subj], f"Non-canonical topic {q['topic']} for {subj}"

    # Apply Intra-Question Option-Length Parity Engine across all 3,125 questions
    master_equalized = equalize_question_bank_options(master_raw)
    eq_by_id = {q["id"]: q for q in master_equalized}

    # Save un-shuffled source JSONs in src/data/questionPacks
    root_dir = os.path.join(scripts_dir, "..")
    packs_dir = os.path.join(root_dir, "src", "data", "questionPacks")

    def pick_eq(q_list):
        return [eq_by_id[q["id"]] for q in q_list]

    with open(os.path.join(packs_dir, "high_yield_clean_base.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(clean_base), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "pyqs_300.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(all_core_pyqs), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vpp_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_vpp_300), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vmc_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_vmc_300), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "van_150_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_van_150), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vpa_60_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_vpa_60), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vpp_350_part2.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_vpp_350_p2), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vmc_350_part2.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_vmc_350_p2), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "ann_250_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_ann_250), f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "agb_250_new.json"), "w", encoding="utf-8") as f:
        json.dump(pick_eq(new_agb_250), f, indent=2, ensure_ascii=False)

    print("Now executing apply_balance() to balance A/B/C/D answer indices and generate TS bundles...")
    from apply_balanced_options import apply_balance
    apply_balance()


if __name__ == "__main__":
    main()
