import json, re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

print(f"Total biased questions: {len(biased)}")

# Let's inspect van_exp_031 and vpp_q_036 specifically
targets = [b for b in biased if b['id'] in ['van_exp_031', 'vpp_q_036']]
for t in targets:
    print("Found target:", t['id'])
    print("  Q:", t['qText'])
    print("  C:", t['c_opt'])
    print("  D:", t['d_opts'])
