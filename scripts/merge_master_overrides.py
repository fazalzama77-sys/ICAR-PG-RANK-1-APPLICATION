import json, sys, os

master_overrides = {}

# 1. Existing overrides from equalize_engine.py
sys.path.append('scripts')
from equalize_engine import QUESTION_OVERRIDES
master_overrides.update(QUESTION_OVERRIDES)
print(f"Loaded {len(QUESTION_OVERRIDES)} from equalize_engine.py")

# 2. VMC 13
from overrides_vmc_13 import VMC_13_OVERRIDES
master_overrides.update(VMC_13_OVERRIDES)
print(f"Loaded {len(VMC_13_OVERRIDES)} from overrides_vmc_13")

# 3. VAN 106
with open('scripts/overrides_van_87.json', 'r', encoding='utf-8') as f:
    van_ov = json.load(f)
master_overrides.update(van_ov)
print(f"Loaded {len(van_ov)} from overrides_van_87.json")

# 4. VPP parts 1-6
vpp_total = 0
for i in range(1, 7):
    part_file = f'scripts/vpp_part{i}.json'
    if os.path.exists(part_file):
        with open(part_file, 'r', encoding='utf-8') as f:
            vpp_part = json.load(f)
            master_overrides.update(vpp_part)
            vpp_total += len(vpp_part)
print(f"Loaded {vpp_total} from VPP parts 1-6")

print(f"Total Unique Overrides in Master: {len(master_overrides)}")

with open('scripts/master_tricky_overrides.json', 'w', encoding='utf-8') as f:
    json.dump(master_overrides, f, indent=2)

print("Saved to scripts/master_tricky_overrides.json")
