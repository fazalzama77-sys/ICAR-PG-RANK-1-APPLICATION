# scripts/build_microbiology_350_part2.py
# Aggregates and formats the 350 exam-replica Veterinary Microbiology (Part 2) questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from micro2_mod1 import get_module1_questions
from micro2_mod2 import get_module2_questions
from micro2_mod3 import get_module3_questions
from micro2_mod4 import get_module4_questions
from micro2_mod5 import get_module5_questions
from micro2_mod6 import get_module6_questions

CANONICAL_TOPICS = {
    "General Bacteriology & Bacterial Genetics",
    "Systematic Bacteriology (Gram +ve, Gram -ve, Acid-Fast, Spirochetes & Mycoplasma)",
    "Veterinary Mycology & Mycotoxicoses",
    "General & Systematic Virology (DNA & RNA Animal/Poultry Viruses & Prions)",
    "Veterinary Immunology & Vaccinology",
    "Diagnostic Serology & Molecular Microbiology",
}

def get_all_350_vmc_part2_questions():
    m1 = get_module1_questions()[:65]  # 65
    m2 = get_module2_questions()[:75]  # 75
    m3 = get_module3_questions()[:45]  # 45
    m4 = get_module4_questions()[:75]  # 75
    m5 = get_module5_questions()[:50]  # 50
    m6 = get_module6_questions()[:40]  # 40

    assert len(m1) == 65, f"Expected 65 in mod1, got {len(m1)}"
    assert len(m2) == 75, f"Expected 75 in mod2, got {len(m2)}"
    assert len(m3) == 45, f"Expected 45 in mod3, got {len(m3)}"
    assert len(m4) == 75, f"Expected 75 in mod4, got {len(m4)}"
    assert len(m5) == 50, f"Expected 50 in mod5, got {len(m5)}"
    assert len(m6) == 40, f"Expected 40 in mod6, got {len(m6)}"

    combined = m1 + m2 + m3 + m4 + m5 + m6
    assert len(combined) == 350, f"Expected 350 VMC Part 2 questions, got {len(combined)}"

    formatted = []
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        assert topic in CANONICAL_TOPICS, f"Invalid topic at index {idx}: {topic}"
        assert len(opts) == 4, f"Expected 4 options at index {idx}, got {len(opts)}"
        assert 0 <= correct_idx < 4, f"Invalid correct_idx at index {idx}: {correct_idx}"

        tags = ["Microbiology", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"vmc_exp2_{idx+1:03d}",
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
            "createdAt": 1776000000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_350_vmc_part2_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total VMC Part 2 Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")

    # Verify intra-batch uniqueness of question texts
    texts = [q['questionText'].strip() for q in qs]
    unique_texts = set(texts)
    assert len(unique_texts) == 350, f"Duplicate question text found: {len(unique_texts)} unique out of 350"
    print("Intra-batch uniqueness verification: 100% passed (0 duplicates).")

    # Verify cross-batch uniqueness against existing_vmc_stems.txt
    existing_path = os.path.join(scripts_dir, "existing_vmc_stems.txt")
    if os.path.exists(existing_path):
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_stems = set(line.strip() for line in f if line.strip())
        overlap = unique_texts.intersection(existing_stems)
        assert len(overlap) == 0, f"Found {len(overlap)} overlapping stems with existing_vmc_stems.txt: {overlap}"
        print(f"Cross-batch uniqueness vs {len(existing_stems)} existing stems: 100% passed (0 overlaps).")

    # Check option length distribution
    longest_char_count = 0
    longest_word_count = 0
    for q in qs:
        c_idx = q["correctOptionIndex"]
        opts = q["options"]
        char_lens = [len(o) for o in opts]
        word_lens = [len(o.split()) for o in opts]
        if char_lens[c_idx] == max(char_lens) and char_lens.count(max(char_lens)) == 1:
            longest_char_count += 1
        if word_lens[c_idx] == max(word_lens) and word_lens.count(max(word_lens)) == 1:
            longest_word_count += 1
    print(f"Correct option is strictly longest by chars: {longest_char_count}/350 ({longest_char_count/350*100:.1f}%)")
    print(f"Correct option is strictly longest by words: {longest_word_count}/350 ({longest_word_count/350*100:.1f}%)")
