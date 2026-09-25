import json
from collections import Counter
import re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

d_words = Counter()
for b in biased:
    for d in b['d_opts']:
        d_clean = re.sub(r'[^\w\s]', '', d).strip()
        if len(d_clean) > 2:
            d_words[d_clean] += 1

print("Top 30 most common distractor expressions:")
for term, count in d_words.most_common(30):
    print(f"  {term}: {count}")
