# scripts/build_microbiology_300.py
# Aggregates and formats the 300 exam-calibrated Veterinary Microbiology questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from micro_mod1_bacteriology import get_module1_questions
from micro_mod2_virology import get_module2_questions
from micro_mod3_genbact import get_module3_questions
from micro_mod4_immunology import get_module4_questions
from micro_mod5_genvirol import get_module5_questions
from micro_mod6_mycology import get_module6_questions

def get_all_300_vmc_questions():
    m1 = get_module1_questions() # 90
    m2 = get_module2_questions() # 80
    m3 = get_module3_questions() # 45
    m4 = get_module4_questions() # 45
    m5 = get_module5_questions() # 25
    m6 = get_module6_questions() # 15

    combined = m1 + m2 + m3 + m4 + m5 + m6
    assert len(combined) == 300, f"Expected 300 VMC questions, got {len(combined)}"

    formatted = []
    pyq_count = 0
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        tags = ["Microbiology", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
            pyq_count += 1
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"vmc_exp_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "2nd_year",
            "subjectId": "vmc",
            "topic": topic,
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": expl,
            "difficulty": "Hard" if is_pyq else "Medium",
            "tags": tags,
            "isPYQ": is_pyq,
            "createdAt": 1774600000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_300_vmc_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total VMC Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")
    # Verify uniqueness of question texts
    texts = set(q['questionText'] for q in qs)
    assert len(texts) == 300, f"Duplicate question text found in VMC: {len(texts)} unique out of 300"
    print("Intra-batch uniqueness verification: 100% passed (0 duplicates).")
