import json

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

for sub in ['vpp', 'vmc', 'van', 'vpy', 'ann', 'vpa', 'lpm', 'vbc', 'agb']:
    sub_items = [b for b in biased if b['subjectId'] == sub]
    print(f"\n==================== {sub.upper()} ({len(sub_items)} questions) ====================")
    for item in sub_items[:3]:
        print(f"ID: {item['id']} | C_len: {item['c_len']} | Max_D: {item['max_d']}")
        print(f"  Q: {item['qText'][:80]}")
        print(f"  C: {item['c_opt']}")
        print(f"  D: {item['d_opts']}")
