import json, subprocess

proc = subprocess.run(['git', 'show', '9786b8f:src/data/questionPacks/high_yield_master_clean.json'], capture_output=True, text=True, encoding='utf-8')
data_1665 = json.loads(proc.stdout)
clean_map = {q['id']: q for q in data_1665}

with open('scripts/need_tricky_293.json', 'r', encoding='utf-8') as f:
    need_tricky = json.load(f)

for sub in ['vmc', 'van', 'vpp']:
    sub_qs = [clean_map[q['id']] for q in need_tricky if q['subjectId'] == sub]
    print(f"\n==================== {sub.upper()} ({len(sub_qs)} questions) ====================")
    for q in sub_qs[:5]:
        c_opt = q['options'][q['correctOptionIndex']]
        d_opts = [q['options'][i] for i in range(len(q['options'])) if i != q['correctOptionIndex']]
        print(f"ID: {q['id']}")
        print(f"  Q: {q['questionText']}")
        print(f"  C: {c_opt}")
        print(f"  D: {d_opts}")
