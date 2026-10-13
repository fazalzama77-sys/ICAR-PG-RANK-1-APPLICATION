# scripts/build_genetics_250.py
# Aggregates and formats the 250 exam-calibrated Animal Genetics & Breeding (AGB) questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from agb_mod1 import get_module1_questions
from agb_mod2 import get_module2_questions
from agb_mod3 import get_module3_questions
from agb_mod4 import get_module4_questions
from agb_mod5 import get_module5_questions
from agb_mod6 import get_module6_questions

CANONICAL_TOPICS = {
    "Mendelian, Chromosomal & Cytogenetics",
    "Molecular Genetics, Genomics & Markers",
    "Population Genetics (Hardy-Weinberg Equilibrium & Gene Frequency)",
    "Quantitative Genetics (Variance, Heritability, Repeatability & Correlations)",
    "Selection Methods, Sire Evaluation & Breeding Values (BLUP)",
    "Mating Systems, Heterosis, Breeds & Conservation",
}

def get_all_250_agb_questions():
    m1 = get_module1_questions()  # 45
    m2 = get_module2_questions()  # 40
    m3 = get_module3_questions()  # 45
    m4 = get_module4_questions()  # 45
    m5 = get_module5_questions()  # 40
    m6 = get_module6_questions()  # 35

    assert len(m1) == 45, f"Expected 45 in Mod 1, got {len(m1)}"
    assert len(m2) == 40, f"Expected 40 in Mod 2, got {len(m2)}"
    assert len(m3) == 45, f"Expected 45 in Mod 3, got {len(m3)}"
    assert len(m4) == 45, f"Expected 45 in Mod 4, got {len(m4)}"
    assert len(m5) == 40, f"Expected 40 in Mod 5, got {len(m5)}"
    assert len(m6) == 35, f"Expected 35 in Mod 6, got {len(m6)}"

    combined = m1 + m2 + m3 + m4 + m5 + m6
    assert len(combined) == 250, f"Expected 250 AGB questions, got {len(combined)}"

    formatted = []
    pyq_count = 0
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        assert topic in CANONICAL_TOPICS, f"Invalid topic at Q{idx+1}: {topic}"
        assert len(opts) == 4, f"Expected 4 options at Q{idx+1}, got {len(opts)}"
        assert 0 <= correct_idx < 4, f"Invalid correct_idx at Q{idx+1}: {correct_idx}"

        tags = ["Genetics & Breeding", "AGB", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
            pyq_count += 1
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"agb_exp_{idx+1:03d}",
            "domain": "animal_science",
            "year": "2nd_year",
            "subjectId": "agb",
            "topic": topic,
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": expl,
            "difficulty": "Hard" if is_pyq else "Medium",
            "tags": tags,
            "isPYQ": is_pyq,
            "createdAt": 1778000000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_250_agb_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total AGB Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")

    # Verify uniqueness of question texts within batch
    texts = set(q['questionText'].strip().lower() for q in qs)
    assert len(texts) == 250, f"Duplicate question text found in AGB: {len(texts)} unique out of 250"
    print("Intra-batch uniqueness verification: 100% passed (0 duplicates).")

    # Verify 0 duplicates against existing_agb_stems.txt
    existing_path = os.path.join(scripts_dir, "existing_agb_stems.txt")
    if os.path.exists(existing_path):
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_stems = set(line.strip().lower() for line in f if line.strip())
        overlap = texts.intersection(existing_stems)
        assert len(overlap) == 0, f"Found overlap with existing_agb_stems.txt: {overlap}"
        print(f"Cross-check against {len(existing_stems)} stems in existing_agb_stems.txt: 100% passed (0 duplicates).")
