import json, re

with open('scripts/test_rule_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect the remaining 449 questions in biased_remaining
with open('scripts/biased_remaining_sample.json', 'w', encoding='utf-8') as f:
    pass

import subprocess
res = subprocess.run(['python', '-c', """
import json, re, sys
sys.path.append('scripts')
from test_rule_pipeline import biased_remaining

print('Total biased:', len(biased_remaining))
with_paren = [q for q in biased_remaining if '(' in q['options'][q['correctOptionIndex']]]
print('With paren in correct:', len(with_paren))

for q in biased_remaining[:10]:
    c = q['options'][q['correctOptionIndex']]
    d = [q['options'][i] for i in range(4) if i != q['correctOptionIndex']]
    print(f\"[{q['id']} - {q['subjectId']}] C ({len(c)}): {c}\")
    print(f\"     D: {d}\")
"""], capture_output=True, text=True, encoding='utf-8')

print(res.stdout)
