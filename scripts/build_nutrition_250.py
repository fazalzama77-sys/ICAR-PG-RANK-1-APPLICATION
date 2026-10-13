# scripts/build_nutrition_250.py
# Aggregates and formats the 250 exam-calibrated Animal Nutrition (ann) questions
import json
import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from ann_mod1 import get_module1_questions
from ann_mod2 import get_module2_questions
from ann_mod3 import get_module3_questions
from ann_mod4 import get_module4_questions
from ann_mod5 import get_module5_questions
from ann_mod6 import get_module6_questions

CANONICAL_TOPICS = {
    "Principles of Nutrition, Proximate Analysis & Nutrient Metabolism",
    "Feed Evaluation & Energy/Protein Partitioning (TDN, ME, NE, RUP/RDP)",
    "Forage Conservation (Silage, Hay), Feed Processing & Anti-Nutritional Factors",
    "Minerals, Vitamins, Feed Additives & Metabolic Deficiency Diseases",
    "Applied Ruminant Nutrition (Dairy Cattle, Buffalo, Sheep & Goat)",
    "Applied Monogastric, Poultry & Pet/Equine Nutrition",
}

def get_all_250_ann_questions():
    m1 = get_module1_questions()  # 45
    m2 = get_module2_questions()  # 45
    m3 = get_module3_questions()  # 45
    m4 = get_module4_questions()  # 45
    m5 = get_module5_questions()  # 35
    m6 = get_module6_questions()  # 35

    assert len(m1) == 45, f"Expected 45 in Mod 1, got {len(m1)}"
    assert len(m2) == 45, f"Expected 45 in Mod 2, got {len(m2)}"
    assert len(m3) == 45, f"Expected 45 in Mod 3, got {len(m3)}"
    assert len(m4) == 45, f"Expected 45 in Mod 4, got {len(m4)}"
    assert len(m5) == 35, f"Expected 35 in Mod 5, got {len(m5)}"
    assert len(m6) == 35, f"Expected 35 in Mod 6, got {len(m6)}"

    combined = m1 + m2 + m3 + m4 + m5 + m6
    assert len(combined) == 250, f"Expected 250 ANN questions, got {len(combined)}"

    formatted = []
    for idx, item in enumerate(combined):
        q_text, opts, correct_idx, expl, is_pyq, topic = item
        assert topic in CANONICAL_TOPICS, f"Invalid topic at index {idx}: {topic}"
        assert len(opts) == 4, f"Expected 4 options at index {idx}, got {len(opts)}"
        assert 0 <= correct_idx < 4, f"Invalid correct_idx at index {idx}: {correct_idx}"

        tags = ["Animal Nutrition", "High-Yield"]
        if is_pyq:
            tags.extend(["ICAR PG PYQ", "Authentic PYQ"])
        else:
            tags.append("Core Concept")

        formatted.append({
            "id": f"ann_exp_{idx+1:03d}",
            "domain": "animal_science",
            "year": "2nd_year",
            "subjectId": "ann",
            "topic": topic,
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": expl,
            "difficulty": "Hard" if is_pyq else "Medium",
            "tags": tags,
            "isPYQ": is_pyq,
            "createdAt": 1777000000000 + idx
        })
    return formatted

if __name__ == '__main__':
    qs = get_all_250_ann_questions()
    pyqs = [q for q in qs if q.get('isPYQ')]
    print(f"Total ANN Questions Built: {len(qs)}")
    print(f"Total Authentic PYQs flagged: {len(pyqs)}")

    # Verify intra-batch uniqueness
    texts = [q['questionText'].strip() for q in qs]
    unique_texts = set(texts)
    assert len(unique_texts) == 250, f"Duplicate question text found: {len(unique_texts)} unique out of 250"
    print("Intra-batch uniqueness verification: 100% passed (250 unique stems, 0 duplicates).")

    # Verify against existing_ann_stems.txt
    existing_path = os.path.join(scripts_dir, 'existing_ann_stems.txt')
    if os.path.exists(existing_path):
        with open(existing_path, 'r', encoding='utf-8') as f:
            existing_stems = {line.strip().lower() for line in f if line.strip()}
        overlaps = [t for t in texts if t.lower() in existing_stems]
        assert len(overlaps) == 0, f"Found overlaps with existing_ann_stems.txt: {overlaps}"
        print(f"Cross-check against existing_ann_stems.txt ({len(existing_stems)} stems): 0 duplicates.")

    # Check option length statistics
    longest_correct_count = 0
    severe_bias_count = 0
    for q in qs:
        opts = q['options']
        c_idx = q['correctOptionIndex']
        c_len = len(opts[c_idx])
        other_lens = [len(o) for i, o in enumerate(opts) if i != c_idx]
        max_other = max(other_lens)
        avg_other = sum(other_lens) / 3.0
        if c_len > max_other:
            longest_correct_count += 1
        if c_len >= 1.8 * avg_other and (c_len - max_other) >= 20:
            severe_bias_count += 1
    print(f"Correct option strictly longest: {longest_correct_count}/250 ({longest_correct_count/2.5:.1f}%)")
    print(f"Severe length bias count: {severe_bias_count}/250")
