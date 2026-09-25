import json, subprocess

proc = subprocess.run(['git', 'show', '9786b8f:src/data/questionPacks/high_yield_master_clean.json'], capture_output=True, text=True, encoding='utf-8')
data_1665 = json.loads(proc.stdout)
clean_map = {q['id']: q for q in data_1665}

with open('scripts/need_tricky_293.json', 'r', encoding='utf-8') as f:
    need_tricky = json.load(f)

found_in_clean = 0
for q in need_tricky:
    if q['id'] in clean_map:
        found_in_clean += 1

print(f"Found in clean commit 9786b8f: {found_in_clean} of {len(need_tricky)}")

# Show 5 examples of clean options
for q in need_tricky[:5]:
    qid = q['id']
    if qid in clean_map:
        cq = clean_map[qid]
        c_opt = cq['options'][cq['correctOptionIndex']]
        d_opts = [cq['options'][i] for i in range(len(cq['options'])) if i != cq['correctOptionIndex']]
        print(f"[{qid}] Q: {cq['questionText'][:60]}")
        print(f"  C: {c_opt}")
        print(f"  D: {d_opts}")
