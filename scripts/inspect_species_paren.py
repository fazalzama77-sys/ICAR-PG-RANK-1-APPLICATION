import json, re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

paren_pattern = re.compile(r'^(.*?)\s*\((.*?)\)$')
species_keywords = ['Equine', 'Bovine', 'Canine', 'Feline', 'Porcine', 'Ovine', 'Caprine', 'Horse', 'Ox', 'Dog', 'Cat', 'Pig', 'Sheep', 'Goat']

species_paren = []
for b in biased:
    c_opt = b['c_opt']
    m = paren_pattern.match(c_opt)
    if m:
        term, details = m.group(1).strip(), m.group(2).strip()
        if any(sk in term or sk in details for sk in species_keywords):
            species_paren.append(b)

print(f"Total species_paren: {len(species_paren)}")
for s in species_paren:
    print(f"[{s['id']}] C ({s['c_len']}): {s['c_opt']}")
    print(f"  D: {s['d_opts']}")
