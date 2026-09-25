import json

with open('scripts/compiled_final_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

m = {q['id']: q for q in master}

for target_id in ['vpp_q_036', 'van_exp_031']:
    q = m[target_id]
    print(f"\n=== {q['id']} ===")
    print('Q:', q['questionText'])
    for idx, opt in enumerate(q['options']):
        tag = ' [CORRECT]' if idx == q['correctOptionIndex'] else ''
        print(f"  {chr(65+idx)}: {opt} ({len(opt)} chars){tag}")
