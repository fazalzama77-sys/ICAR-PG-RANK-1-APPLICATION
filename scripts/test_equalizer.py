# scripts/test_equalizer.py
import json
import re

with open('scripts/biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

print(f"Total biased questions: {len(biased)}")

# Sample inspection of 20 questions
for i, q in enumerate(biased[:20]):
    print(f"\n[{q['id']}] Q: {q['questionText'][:75]}...")
    print(f"  CORRECT ({len(q['correct'])}): {q['correct']}")
    print(f"  DISTRACTORS: {q['distractors']}")
