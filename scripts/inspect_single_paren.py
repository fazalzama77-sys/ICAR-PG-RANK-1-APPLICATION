import json, re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

paren_pattern = re.compile(r'^(.*?)\s*\((.*?)\)$')

single_paren = []
for b in biased:
    c_opt = b['c_opt']
    m = paren_pattern.match(c_opt)
    if m:
        term, details = m.group(1).strip(), m.group(2).strip()
        single_paren.append((b['id'], b['subjectId'], term, details, b['d_opts'], b['qText']))

print(f"Total single_paren: {len(single_paren)}")

# Let's inspect 10 examples
for item in single_paren[:10]:
    print(f"[{item[0]}] Term: '{item[2]}' | Parenthetical: '({item[3]})'")
    print(f"  Distractors: {item[4]}")
