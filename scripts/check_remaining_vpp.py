import json

with open('scripts/vpp_153_dump.json', 'r', encoding='utf-8') as f:
    all_vpp = json.load(f)

done = set()
for part in ['vpp_part1.json', 'vpp_part2.json', 'vpp_part3.json', 'vpp_part4.json']:
    with open('scripts/' + part, 'r', encoding='utf-8') as f:
        done.update(json.load(f).keys())

remaining = [q for q in all_vpp if q['id'] not in done]
print(f"Remaining VPP questions: {len(remaining)}")
for r in remaining:
    print(f"ID: {r['id']} | C: {r['c']}")
