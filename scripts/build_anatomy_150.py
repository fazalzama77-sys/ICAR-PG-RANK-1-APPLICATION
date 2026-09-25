# scripts/build_anatomy_150.py
# Aggregates and formats the 150 exam-calibrated Veterinary Anatomy questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from anat_mod1_osteology import get_module1_questions
from anat_mod2_splanchnology import get_module2_questions
from anat_mod3_neuro_angio import get_module3_questions
from anat_mod4_histology_embryo import get_module4_questions
from anat_mod5_avian import get_module5_questions

def get_all_150_van_questions():
    m1 = get_module1_questions() # 40
    m2 = get_module2_questions() # 40
    m3 = get_module3_questions() # 30
    m4 = get_module4_questions() # 25
    m5 = get_module5_questions() # 15

    combined = m1 + m2 + m3 + m4 + m5
    assert len(combined) == 150, f"Expected 150 VAN questions, got {len(combined)}"

    formatted = []
    pyq_count = 0
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        tags = ["Anatomy", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
            pyq_count += 1
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"van_exp_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "1st_year",
            "subjectId": "van",
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
    qs = get_all_150_van_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total VAN Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")
    out_path = os.path.join(scripts_dir, '..', 'src', 'data', 'questionPacks', 'van_150_new.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to: {out_path}")
