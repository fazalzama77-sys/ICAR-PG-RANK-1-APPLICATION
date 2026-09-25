import json

with open('scripts/vpp_153_dump.json', 'r', encoding='utf-8') as f:
    vpp_qs = json.load(f)

print(f"Loaded {len(vpp_qs)} VPP questions.")

# Let's inspect each question's ID, correct, and distractors
for i, q in enumerate(vpp_qs[:20]):
    print(f"{i+1:02d}. ID: {q['id']}")
    print(f"    Q: {q['q']}")
    print(f"    C: {q['c']}")
    print(f"    D: {q['d']}")
