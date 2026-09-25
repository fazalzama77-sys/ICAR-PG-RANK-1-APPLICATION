import json

with open('scripts/van_87_dump.json', 'r', encoding='utf-8') as f:
    van_qs = json.load(f)

print(f"Loaded {len(van_qs)} VAN questions.")

# Let's inspect each question's ID, correct, and distractors
for i, q in enumerate(van_qs):
    print(f"{i+1:02d}. ID: {q['id']}")
    print(f"    Q: {q['q']}")
    print(f"    C: {q['c']}")
    print(f"    D: {q['d']}")
