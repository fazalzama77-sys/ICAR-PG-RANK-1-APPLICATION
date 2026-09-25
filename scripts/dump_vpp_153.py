import json

with open('scripts/missing_253.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

vpp_153 = [m for m in missing if m['sub'] == 'vpp']
print(f"VPP missing: {len(vpp_153)}")

with open('scripts/vpp_153_dump.json', 'w', encoding='utf-8') as f:
    json.dump(vpp_153, f, indent=2)

print("Dumped 153 VPP questions to scripts/vpp_153_dump.json")
