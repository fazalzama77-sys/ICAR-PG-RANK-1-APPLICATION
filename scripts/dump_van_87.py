import json

with open('scripts/missing_253.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

van_87 = [m for m in missing if m['sub'] == 'van']
print(f"VAN missing: {len(van_87)}")

with open('scripts/van_87_dump.json', 'w', encoding='utf-8') as f:
    json.dump(van_87, f, indent=2)

print("Dumped 87 VAN questions to scripts/van_87_dump.json")
