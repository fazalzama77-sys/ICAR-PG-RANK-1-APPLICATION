# scripts/inspect_patterns.py
import json
import re

with open('scripts/biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

print(f"Total biased: {len(biased)}")

types = {
    'paren_acronym': [],
    'paren_synonym': [],
    'paren_disease': [],
    'paren_desc': [],
    'paren_numbers': [],
    'long_desc': [],
    'multi_item': [],
    'other': []
}

for q in biased:
    c = q['correct']
    d = q['distractors']
    m = re.search(r'\((.*?)\)', c)
    if m:
        content = m.group(1).strip()
        if re.search(r'\d+', content):
            types['paren_numbers'].append(q)
        elif len(content) <= 8 and content.isupper():
            types['paren_acronym'].append(q)
        elif any(w in content.lower() for w in ['demonstrating', 'characterized by', 'resulting in', 'due to', 'mediated by', 'caused by', 'assuming', 'derived from']):
            types['paren_desc'].append(q)
        elif any(w in content.lower() for w in ['disease', 'fever', 'syndrome', 'infection', 'stomatitis', 'pox']):
            types['paren_disease'].append(q)
        else:
            types['paren_synonym'].append(q)
    elif ',' in c and c.count(',') >= 2:
        types['multi_item'].append(q)
    elif len(c) >= 40:
        types['long_desc'].append(q)
    else:
        types['other'].append(q)

for k, v in types.items():
    print(f"{k}: {len(v)}")

print("\n--- SAMPLE paren_desc (10 examples) ---")
for q in types['paren_desc'][:10]:
    print(f"[{q['id']}] {q['correct']} | Distractors: {q['distractors']}")

print("\n--- SAMPLE long_desc (10 examples) ---")
for q in types['long_desc'][:10]:
    print(f"[{q['id']}] {q['correct']} | Distractors: {q['distractors']}")

print("\n--- SAMPLE paren_synonym (10 examples) ---")
for q in types['paren_synonym'][:10]:
    print(f"[{q['id']}] {q['correct']} | Distractors: {q['distractors']}")

print("\n--- SAMPLE paren_numbers (10 examples) ---")
for q in types['paren_numbers'][:10]:
    print(f"[{q['id']}] {q['correct']} | Distractors: {q['distractors']}")
