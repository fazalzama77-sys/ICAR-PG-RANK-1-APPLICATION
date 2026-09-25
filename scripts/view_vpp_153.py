import json

with open('scripts/vpp_153_dump.json', 'r', encoding='utf-8') as f:
    vpp_qs = json.load(f)

print(f"Total VPP questions: {len(vpp_qs)}")

for idx, q in enumerate(vpp_qs):
    print(f"[{idx+1:03d}] {q['id']} (len C: {len(q['c'])}) | Q: {q['q'][:65]}")
    print(f"      C: {q['c']}")
