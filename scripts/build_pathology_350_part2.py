# scripts/build_pathology_350_part2.py
# Aggregates and formats the 350 Part-2 exam-calibrated Veterinary Pathology (vpp) questions
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)

from path2_mod1 import get_module1_questions
from path2_mod2 import get_module2_questions
from path2_mod3 import get_module3_questions
from path2_mod4 import get_module4_questions
from path2_mod5 import get_module5_questions
from path2_mod6 import get_module6_questions

CANONICAL_TOPICS = {
    "General Pathology: Cell Injury, Degenerations & Necrosis",
    "Inflammation, Tissue Repair & Hemodynamic Disorders",
    "Systemic Pathology (Digestive, Respiratory, Cardiovascular, Urinary, Nervous & Reproductive)",
    "Pathology of Infectious Diseases (Bacterial, Viral, Fungal & Parasitic)",
    "Veterinary Oncology & Neoplasia",
    "Avian, Clinical & Necropsy Pathology",
}

def get_all_350_vpp_part2_questions():
    m1 = get_module1_questions()  # 70
    m2 = get_module2_questions()  # 60
    m3 = get_module3_questions()  # 70
    m4 = get_module4_questions()  # 60
    m5 = get_module5_questions()  # 45
    m6 = get_module6_questions()  # 45

    assert len(m1) == 70, f"Module 1 expected 70, got {len(m1)}"
    assert len(m2) == 60, f"Module 2 expected 60, got {len(m2)}"
    assert len(m3) == 70, f"Module 3 expected 70, got {len(m3)}"
    assert len(m4) == 60, f"Module 4 expected 60, got {len(m4)}"
    assert len(m5) == 45, f"Module 5 expected 45, got {len(m5)}"
    assert len(m6) == 45, f"Module 6 expected 45, got {len(m6)}"

    combined = m1 + m2 + m3 + m4 + m5 + m6
    assert len(combined) == 350, f"Expected 350 VPP Part 2 questions, got {len(combined)}"

    formatted = []
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        assert len(opts) == 4, f"Question {idx+1} does not have 4 options"
        assert 0 <= correct_idx < 4, f"Question {idx+1} has invalid correct_idx {correct_idx}"
        assert topic in CANONICAL_TOPICS, f"Question {idx+1} has non-canonical topic: {topic}"

        tags = ["Pathology", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"vpp_exp2_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "2nd_year",
            "subjectId": "vpp",
            "topic": topic,
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": expl,
            "difficulty": "Hard" if is_pyq else "Medium",
            "tags": tags,
            "isPYQ": is_pyq,
            "createdAt": 1775000000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_350_vpp_part2_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total VPP Part-2 Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")

    # Intra-batch uniqueness
    texts = [q['questionText'].strip() for q in qs]
    unique_texts = set(texts)
    assert len(unique_texts) == 350, f"Duplicate question text in Part 2: {len(unique_texts)} unique out of 350"
    print("Intra-batch uniqueness verification: 100% passed (0 duplicates).")

    # Check against existing_vpp_stems.txt
    existing_path = os.path.join(scripts_dir, "existing_vpp_stems.txt")
    if os.path.exists(existing_path):
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_stems = set(line.strip().lower() for line in f if line.strip())
        overlaps = [t for t in texts if t.lower() in existing_stems]
        assert len(overlaps) == 0, f"Found {len(overlaps)} overlaps with existing_vpp_stems.txt: {overlaps}"
        print(f"Cross-check against existing_vpp_stems.txt ({len(existing_stems)} stems): 0 duplicates.")

    # Check option length distribution (how often is correct option strictly the longest?)
    longest_correct_count = 0
    for q in qs:
        opts = q['options']
        c_idx = q['correctOptionIndex']
        c_len = len(opts[c_idx])
        max_other_len = max(len(opts[i]) for i in range(4) if i != c_idx)
        if c_len > max_other_len:
            longest_correct_count += 1
    pct = (longest_correct_count / len(qs)) * 100
    print(f"Correct option strictly longest in {longest_correct_count}/350 questions ({pct:.1f}%).")
