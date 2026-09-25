import json
import re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

paren_pattern = re.compile(r'^(.*?)\s*\((.*?)\)$')

categories = {
    'single_paren': [], # "Term (Details)"
    'species_paren': [], # "Species (Common/Details)"
    'compound_list': [], # "A, B, C, and D"
    'sentence_desc': [], # Long descriptive sentence
    'other': []
}

for b in biased:
    c_opt = b['c_opt']
    m = paren_pattern.match(c_opt)
    if m:
        term, details = m.group(1).strip(), m.group(2).strip()
        species_keywords = ['Equine', 'Bovine', 'Canine', 'Feline', 'Porcine', 'Ovine', 'Caprine', 'Horse', 'Ox', 'Dog', 'Cat', 'Pig', 'Sheep', 'Goat']
        if any(sk in term or sk in details for sk in species_keywords):
            categories['species_paren'].append((b, term, details))
        else:
            categories['single_paren'].append((b, term, details))
    elif ',' in c_opt or ' and ' in c_opt:
        categories['compound_list'].append(b)
    elif len(c_opt) > 60:
        categories['sentence_desc'].append(b)
    else:
        categories['other'].append(b)

print("Categorization of 779 biased questions:")
for k, v in categories.items():
    print(f"  {k}: {len(v)}")
