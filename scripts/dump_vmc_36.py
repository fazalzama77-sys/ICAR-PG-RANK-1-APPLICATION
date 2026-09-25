import json, subprocess

proc = subprocess.run(['git', 'show', '9786b8f:src/data/questionPacks/high_yield_master_clean.json'], capture_output=True, text=True, encoding='utf-8')
data_1665 = json.loads(proc.stdout)
clean_map = {q['id']: q for q in data_1665}

with open('scripts/need_tricky_293.json', 'r', encoding='utf-8') as f:
    need_tricky = json.load(f)

vmc_qs = [clean_map[q['id']] for q in need_tricky if q['subjectId'] == 'vmc']
print(f"Total VMC questions: {len(vmc_qs)}")

with open('scripts/vmc_36_dump.json', 'w', encoding='utf-8') as f:
    json.dump([{'id': q['id'], 'q': q['questionText'], 'c': q['options'][q['correctOptionIndex']], 'd': [q['options'][i] for i in range(len(q['options'])) if i != q['correctOptionIndex']]} for q in vmc_qs], f, indent=2)

print("Dumped 36 VMC questions to scripts/vmc_36_dump.json")
