# scripts/distribute_all_packs.py
import json, os

with open('scripts/compiled_final_master.json', 'r', encoding='utf-8') as f:
    master_questions = json.load(f)

master_map = {q['id']: q for q in master_questions}
print(f"Loaded {len(master_questions)} questions from compiled_final_master.json")

packs_dir = 'src/data/questionPacks'

# 1. Update high_yield_master_clean.json
with open(os.path.join(packs_dir, 'high_yield_master_clean.json'), 'w', encoding='utf-8') as f:
    json.dump(master_questions, f, indent=2)
print("Updated high_yield_master_clean.json")

# 2. Update high_yield_master_1380.json
with open(os.path.join(packs_dir, 'high_yield_master_1380.json'), 'w', encoding='utf-8') as f:
    json.dump(master_questions, f, indent=2)
print("Updated high_yield_master_1380.json")

# 3. Update JSON packs
json_packs = [
    'pyqs_300.json',
    'van_150_new.json',
    'vpp_300_new.json',
    'vmc_300_new.json',
    'vpa_60_new.json',
    'high_yield_clean_base.json',
    'high_yield_1080.json'
]

for jp in json_packs:
    path = os.path.join(packs_dir, jp)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            pack_data = json.load(f)
        updated_pack = []
        for q in pack_data:
            if q['id'] in master_map:
                updated_pack.append(master_map[q['id']])
            else:
                updated_pack.append(q)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(updated_pack, f, indent=2)
        print(f"Updated {jp} ({len(updated_pack)} questions)")

# 4. Generate pyqQuestions.ts
core_pyqs = [master_map[qid] for qid in master_map if qid.startswith('pyq_')]
with open(os.path.join(packs_dir, 'pyqQuestions.ts'), 'w', encoding='utf-8') as f:
    f.write('import { Question } from \'../../types\';\n\n')
    f.write('export const ALL_ICAR_PG_PYQ_QUESTIONS: Question[] = ')
    json.dump(core_pyqs, f, indent=2)
    f.write(';\n')
print(f"Updated pyqQuestions.ts ({len(core_pyqs)} questions)")

# 5. Generate allQuestions.ts
with open(os.path.join(packs_dir, 'allQuestions.ts'), 'w', encoding='utf-8') as f:
    f.write('import { Question } from \'../../types\';\n')
    f.write('export { ALL_ICAR_PG_PYQ_QUESTIONS } from \'./pyqQuestions\';\n\n')
    f.write('export const ALL_HIGH_YIELD_QUESTIONS: Question[] = ')
    json.dump(master_questions, f, indent=2)
    f.write(';\n')
print(f"Updated allQuestions.ts ({len(master_questions)} questions)")
