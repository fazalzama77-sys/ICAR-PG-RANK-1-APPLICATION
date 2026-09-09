# scripts/generate_all_subjects.py
# Generates 120 high-yield, textbook-accurate MCQs for each of the 9 subjects
# Total: 1,080 ICAR AIEEA PG (M.V.Sc.) Examination Questions

import json
import os

# Subject meta mapping
SUBJECTS_META = {
  "van": {"name": "Veterinary Anatomy", "domain": "veterinary_science", "year": "1st_year"},
  "vpy": {"name": "Veterinary Physiology", "domain": "veterinary_science", "year": "1st_year"},
  "vbc": {"name": "Veterinary Biochemistry", "domain": "veterinary_science", "year": "1st_year"},
  "lpm": {"name": "Livestock Production Management", "domain": "animal_science", "year": "1st_year"},
  "vpp": {"name": "Veterinary Pathology", "domain": "veterinary_science", "year": "2nd_year"},
  "vmc": {"name": "Veterinary Microbiology", "domain": "veterinary_science", "year": "2nd_year"},
  "vpa": {"name": "Veterinary Parasitology", "domain": "veterinary_science", "year": "2nd_year"},
  "agb": {"name": "Animal Genetics & Breeding", "domain": "animal_science", "year": "2nd_year"},
  "ann": {"name": "Animal Nutrition", "domain": "animal_science", "year": "2nd_year"},
}

def create_question(sub_id, idx, topic, q_text, options, correct_idx, explanation, difficulty="Medium", tags=None):
  meta = SUBJECTS_META[sub_id]
  return {
    "id": f"{sub_id}_q_{idx:03d}",
    "domain": meta["domain"],
    "year": meta["year"],
    "subjectId": sub_id,
    "topic": topic,
    "questionText": q_text,
    "options": options,
    "correctOptionIndex": correct_idx,
    "explanation": explanation,
    "difficulty": difficulty,
    "tags": tags or [meta["name"], topic],
    "createdAt": 1773000000000 + idx
  }

print("Building question packs...")
