import json, sys
sys.path.append('scripts')
from equalize_engine import QUESTION_OVERRIDES

proc_clean = open('src/data/questionPacks/high_yield_master_clean.json', 'r', encoding='utf-8')
data_1725 = json.load(proc_clean)
proc_clean.close()

with open('scripts/need_tricky_293.json', 'r', encoding='utf-8') as f:
    need_tricky = json.load(f)

for sub in ['van', 'vpp']:
    sub_qs = [q for q in need_tricky if q['subjectId'] == sub]
    already = [q for q in sub_qs if q['id'] in QUESTION_OVERRIDES]
    missing = [q for q in sub_qs if q['id'] not in QUESTION_OVERRIDES]
    print(f"{sub.upper()} Total: {len(sub_qs)} | In QUESTION_OVERRIDES: {len(already)} | Missing: {len(missing)}")
