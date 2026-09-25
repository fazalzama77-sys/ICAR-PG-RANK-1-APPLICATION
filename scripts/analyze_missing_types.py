import json, re

with open('scripts/missing_253.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

paren_p = re.compile(r'^(.*?)\s*\((.*?)\)$')

with_paren = []
without_paren = []

for m in missing:
    if paren_p.match(m['c']):
        with_paren.append(m)
    else:
        without_paren.append(m)

print(f"Missing with parenthetical: {len(with_paren)}")
print(f"Missing without parenthetical: {len(without_paren)}")

print("\nSample with parenthetical:")
for item in with_paren[:6]:
    print(f"[{item['id']} - {item['sub']}] Q: {item['q'][:60]}")
    print(f"  C: {item['c']}")
    print(f"  D: {item['d']}")

print("\nSample without parenthetical:")
for item in without_paren[:6]:
    print(f"[{item['id']} - {item['sub']}] Q: {item['q'][:60]}")
    print(f"  C: {item['c']}")
    print(f"  D: {item['d']}")
