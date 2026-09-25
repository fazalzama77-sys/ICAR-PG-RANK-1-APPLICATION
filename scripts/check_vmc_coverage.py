import json, sys
sys.path.append('scripts')
from equalize_engine import QUESTION_OVERRIDES

with open('scripts/vmc_36_dump.json', 'r', encoding='utf-8') as f:
    vmc_qs = json.load(f)

already_have = [q for q in vmc_qs if q['id'] in QUESTION_OVERRIDES]
missing = [q for q in vmc_qs if q['id'] not in QUESTION_OVERRIDES]

print(f"VMC 36: Already in QUESTION_OVERRIDES: {len(already_have)}, Missing: {len(missing)}")
for m in missing:
    print(f"Missing ID: {m['id']} | C: {m['c'][:60]}")
