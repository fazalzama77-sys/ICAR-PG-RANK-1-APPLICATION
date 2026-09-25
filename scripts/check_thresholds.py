import json

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

for thresh in [15, 20, 25, 30, 40]:
    cnt = len([b for b in biased if (b['c_len'] - b['max_d'] > thresh) or (b['c_len'] > 30 and b['c_len'] > 1.4 * b['max_d'])])
    print(f"Threshold diff > {thresh} or ratio > 1.4: {cnt}")
