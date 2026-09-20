import json
import os
import sys

# Add scripts directory to path
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

from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs

from enrich_to_120 import SUPPLEMENTARY_POOLS

def is_dummy(q):
    q_text = q.get('questionText', '')
    topic = q.get('topic', '')
    opts = q.get('options', [])
    if 'Clinical Landmark MCQ #' in q_text:
        return True
    if 'Core Diagnostic' in topic:
        return True
    if any('Standard validated laboratory' in opt for opt in opts):
        return True
    return False

def main():
    print("==================================================================")
    print("REMOVING ALL DUMMY PLACEHOLDER QUESTIONS FROM QUESTION PACKS")
    print("==================================================================")

    # 1. Collect genuine base questions
    van_qs = get_van_questions()
    
    # VPY: 100 initial + 20 from SUPPLEMENTARY_POOLS
    vpy_initial = get_vpy_questions()
    vpy_supp = []
    for q_text, opts, ans, exp in SUPPLEMENTARY_POOLS.get('vpy', []):
        idx = len(vpy_initial) + len(vpy_supp) + 1
        vpy_supp.append({
            "id": f"vpy_q_{idx:03d}",
            "domain": "animal_science", # Official ICAR PG Code 14.3
            "year": "1st_year",
            "subjectId": "vpy",
            "topic": "Veterinary Physiology High-Yield Core",
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": ans,
            "explanation": exp,
            "difficulty": "Medium",
            "tags": ["Veterinary Physiology", "ICAR PG Core"],
            "createdAt": 1773000000000 + idx
        })
    vpy_qs = vpy_initial + vpy_supp

    vbc_qs = get_vbc_questions()
    lpm_qs = get_lpm_questions()
    vpp_qs = get_vpp_questions()
    vmc_qs = get_vmc_questions()
    vpa_qs = get_vpa_questions()
    agb_qs = get_agb_questions()
    ann_qs = get_ann_questions()

    base_subjects = [
        ("VAN", van_qs),
        ("VPY", vpy_qs),
        ("VBC", vbc_qs),
        ("LPM", lpm_qs),
        ("VPP", vpp_qs),
        ("VMC", vmc_qs),
        ("VPA", vpa_qs),
        ("AGB", agb_qs),
        ("ANN", ann_qs),
    ]

    clean_base_questions = []
    print("\n--- Verified Genuine Base Questions by Subject ---")
    for code, qs in base_subjects:
        valid_qs = [q for q in qs if not is_dummy(q)]
        print(f"[{code}] {len(valid_qs)} genuine questions (removed {len(qs) - len(valid_qs)} dummy)")
        clean_base_questions.extend(valid_qs)

    # Harmonize domains
    for q in clean_base_questions:
        if q.get('subjectId') in ['vpy', 'vbc']:
            q['domain'] = 'animal_science'
        elif q.get('subjectId') in ['van', 'vpp', 'vmc', 'vpa']:
            q['domain'] = 'veterinary_science'
        elif q.get('subjectId') in ['lpm', 'agb', 'ann']:
            q['domain'] = 'animal_science'

    print(f"\nTotal Verified Genuine Base Questions: {len(clean_base_questions)}")

    # 2. Collect PYQs
    vpp_pyqs = get_vpp_pyqs()
    vmc_pyqs = get_vmc_pyqs()
    vbc_pyqs = get_vbc_pyqs()
    all_pyqs = vpp_pyqs + vmc_pyqs + vbc_pyqs

    # Verify no dummy in PYQs
    clean_pyqs = [q for q in all_pyqs if not is_dummy(q)]
    print(f"Total Verified PYQ Questions: {len(clean_pyqs)} (VPP: {len(vpp_pyqs)}, VMC: {len(vmc_pyqs)}, VBC: {len(vbc_pyqs)})")

    # 3. Master list: clean base + clean PYQs
    master_clean = clean_base_questions + clean_pyqs
    print(f"\nTotal Clean Master Questions: {len(master_clean)}")

    # Final assertion that NO dummy question remains
    assert all(not is_dummy(q) for q in master_clean), "Error: Dummy questions still present!"
    print("Verification Passed: 0 dummy questions found.")

    # 4. Save to files
    root_dir = os.path.join(scripts_dir, "..")
    packs_dir = os.path.join(root_dir, "src", "data", "questionPacks")

    # Save high_yield_1080.json
    p1 = os.path.join(packs_dir, "high_yield_1080.json")
    with open(p1, "w", encoding="utf-8") as f:
        json.dump(clean_base_questions, f, indent=2, ensure_ascii=False)
    print(f"Updated {p1} ({len(clean_base_questions)} questions)")

    # Save high_yield_master_1380.json
    p2 = os.path.join(packs_dir, "high_yield_master_1380.json")
    with open(p2, "w", encoding="utf-8") as f:
        json.dump(master_clean, f, indent=2, ensure_ascii=False)
    print(f"Updated {p2} ({len(master_clean)} questions)")

    # Save allQuestions.ts
    p3 = os.path.join(packs_dir, "allQuestions.ts")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(f"// Autogenerated Verified Question Bank ({len(clean_base_questions)} Core Syllabus + {len(clean_pyqs)} High-Yield ICAR PG PYQs = {len(master_clean)} Total Verified)\n")
        f.write("// All placeholder dummy questions have been strictly removed.\n")
        f.write("import { Question } from '../../types';\n")
        f.write("import { ALL_ICAR_PG_PYQ_QUESTIONS, VPP_PYQ_QUESTIONS, VMC_PYQ_QUESTIONS, VBC_PYQ_QUESTIONS } from './pyqQuestions';\n\n")
        f.write("export { ALL_ICAR_PG_PYQ_QUESTIONS, VPP_PYQ_QUESTIONS, VMC_PYQ_QUESTIONS, VBC_PYQ_QUESTIONS };\n\n")
        f.write("const BASE_QUESTIONS: Question[] = " + json.dumps(clean_base_questions, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("export const ALL_HIGH_YIELD_QUESTIONS: Question[] = [\n")
        f.write("  ...BASE_QUESTIONS,\n")
        f.write("  ...ALL_ICAR_PG_PYQ_QUESTIONS\n")
        f.write("];\n")
    print(f"Updated {p3} ({len(master_clean)} total export)")

if __name__ == "__main__":
    main()
