# scripts/build_agb_ann_200.py
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from agb_mod1_genetics_molecular import get_agb_module1_questions
from agb_mod2_quant_breeding import get_agb_module2_questions
from ann_mod1_principles_ruminant import get_ann_module1_questions
from ann_mod2_toxins_monogastric_clinical import get_ann_module2_questions


def build_packs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    packs_dir = os.path.join(base_dir, "..", "src", "data", "questionPacks")

    agb_tuples = get_agb_module1_questions() + get_agb_module2_questions()
    ann_tuples = get_ann_module1_questions() + get_ann_module2_questions()

    assert len(agb_tuples) == 100, f"Expected 100 AGB questions, got {len(agb_tuples)}"
    assert len(ann_tuples) == 100, f"Expected 100 ANN questions, got {len(ann_tuples)}"

    agb_json = []
    for i, (q_text, opts, ans_idx, expl, is_pyq, topic) in enumerate(agb_tuples, start=1):
        assert len(opts) == 4, f"AGB Q{i} does not have 4 options"
        assert len(set(opts)) == 4, f"AGB Q{i} has duplicate options: {opts}"
        assert 0 <= ans_idx < 4, f"AGB Q{i} invalid ans_idx: {ans_idx}"
        agb_json.append({
            "id": f"agb_exp_{i:03d}",
            "domain": "animal_science",
            "year": "2nd_year",
            "subjectId": "agb",
            "topic": f"{topic} (ICAR PG PYQ)" if is_pyq else topic,
            "questionText": q_text,
            "options": list(opts),
            "correctOptionIndex": ans_idx,
            "explanation": expl,
            "difficulty": "Hard" if i % 2 == 1 else "Medium",
            "tags": [
                "Animal Genetics & Breeding",
                "AGB",
                "High-Yield",
                "ICAR PG PYQ" if is_pyq else "ICAR PG Pattern"
            ],
            "isPYQ": bool(is_pyq),
            "createdAt": 1775000000000 + i * 1000
        })

    ann_json = []
    for i, (q_text, opts, ans_idx, expl, is_pyq, topic) in enumerate(ann_tuples, start=1):
        assert len(opts) == 4, f"ANN Q{i} does not have 4 options"
        assert len(set(opts)) == 4, f"ANN Q{i} has duplicate options: {opts}"
        assert 0 <= ans_idx < 4, f"ANN Q{i} invalid ans_idx: {ans_idx}"
        ann_json.append({
            "id": f"ann_exp_{i:03d}",
            "domain": "animal_science",
            "year": "2nd_year",
            "subjectId": "ann",
            "topic": f"{topic} (ICAR PG PYQ)" if is_pyq else topic,
            "questionText": q_text,
            "options": list(opts),
            "correctOptionIndex": ans_idx,
            "explanation": expl,
            "difficulty": "Hard" if i % 2 == 1 else "Medium",
            "tags": [
                "Animal Nutrition",
                "ANN",
                "High-Yield",
                "ICAR PG PYQ" if is_pyq else "ICAR PG Pattern"
            ],
            "isPYQ": bool(is_pyq),
            "createdAt": 1775100000000 + i * 1000
        })

    agb_out = os.path.join(packs_dir, "agb_100_new.json")
    ann_out = os.path.join(packs_dir, "ann_100_new.json")

    with open(agb_out, "w", encoding="utf-8") as f:
        json.dump(agb_json, f, indent=2, ensure_ascii=False)

    with open(ann_out, "w", encoding="utf-8") as f:
        json.dump(ann_json, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(agb_json)} AGB questions to {agb_out}")
    print(f"Successfully wrote {len(ann_json)} ANN questions to {ann_out}")


if __name__ == "__main__":
    build_packs()
