import json

with open('scripts/van_87_dump.json', 'r', encoding='utf-8') as f:
    van_qs = json.load(f)

print(f"Total VAN questions: {len(van_qs)}")

# Group by topic or keywords
for idx, q in enumerate(van_qs):
    print(f"[{idx+1:02d}] {q['id']} (len C: {len(q['c'])}) | Q: {q['q'][:65]}")
    print(f"     C: {q['c']}")
