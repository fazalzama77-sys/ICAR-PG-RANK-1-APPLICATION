# scripts/audit_length_bias.py
import json

with open('src/data/questionPacks/high_yield_master_1380.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

print(f"Total questions: {len(master)}")

biased_questions = []
for q in master:
    opts = q['options']
    c_idx = q['correctOptionIndex']
    c_len = len(opts[c_idx])
    other_lens = [len(opt) for i, opt in enumerate(opts) if i != c_idx]
    avg_other = sum(other_lens) / len(other_lens) if other_lens else 0
    max_other = max(other_lens) if other_lens else 0

    # Criterion for length bias:
    # Correct option is at least 1.8x longer than average distractor and at least 20 chars longer than the longest distractor
    if c_len >= 1.8 * avg_other and (c_len - max_other) >= 20:
        biased_questions.append({
            'id': q['id'],
            'subjectId': q['subjectId'],
            'questionText': q['questionText'],
            'correct': opts[c_idx],
            'correct_len': c_len,
            'distractors': [opt for i, opt in enumerate(opts) if i != c_idx],
            'max_other': max_other,
            'avg_other': avg_other
        })

print(f"Total questions with severe longest-option bias: {len(biased_questions)}")
print("\nFirst 15 examples:")
for item in biased_questions[:15]:
    print("----------------------------------------------------------------------")
    print(f"[{item['id']}] ({item['subjectId']}) {item['questionText']}")
    print(f"CORRECT ({item['correct_len']} chars): {item['correct']}")
    print(f"DISTRACTORS (avg {item['avg_other']:.1f} chars):")
    for d in item['distractors']:
        print(f"  - ({len(d)} chars): {d}")
