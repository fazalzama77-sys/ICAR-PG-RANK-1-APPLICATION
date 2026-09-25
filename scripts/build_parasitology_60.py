# scripts/build_parasitology_60.py
# Aggregates and formats the 60 exam-calibrated Veterinary Parasitology questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from para_mod1_helminths import get_module1_questions
from para_mod2_protozoa_arthropods import get_module2_questions

def get_all_60_vpa_questions():
    m1 = get_module1_questions() # 30
    m2 = get_module2_questions() # 30

    combined = m1 + m2
    assert len(combined) == 60, f"Expected 60 VPA questions, got {len(combined)}"

    formatted = []
    pyq_count = 0
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        tags = ["Parasitology", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
            pyq_count += 1
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"vpa_exp_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "2nd_year",
            "subjectId": "vpa",
            "topic": topic,
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": expl,
            "difficulty": "Hard" if is_pyq else "Medium",
            "tags": tags,
            "isPYQ": is_pyq,
            "createdAt": 1774700000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_60_vpa_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total VPA Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")
    out_path = os.path.join(scripts_dir, '..', 'src', 'data', 'questionPacks', 'vpa_60_new.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to: {out_path}")
