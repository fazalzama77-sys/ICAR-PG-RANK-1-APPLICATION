# scripts/compile_pyqs.py
import json
import os
import sys

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from pyq_van import get_van_pyqs
from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs
from build_pathology_300 import get_all_300_vpp_questions
from build_microbiology_300 import get_all_300_vmc_questions
from build_anatomy_150 import get_all_150_van_questions

def main():
    print("Compiling Complete Question Bank (565 Base + 350 Core PYQs + 300 VPP Exp + 300 VMC Exp + 150 VAN Exp = 1,665 Questions)...")
    
    van_pyqs = get_van_pyqs() # 50
    vpp_pyqs = get_vpp_pyqs() # 100
    vmc_pyqs = get_vmc_pyqs() # 100
    vbc_pyqs = get_vbc_pyqs() # 100
    
    new_vpp_300 = get_all_300_vpp_questions() # 300
    new_vmc_300 = get_all_300_vmc_questions() # 300
    new_van_150 = get_all_150_van_questions() # 150

    print(f"Veterinary Anatomy Core PYQs (VAN): {len(van_pyqs)}")
    print(f"Veterinary Pathology Core PYQs (VPP): {len(vpp_pyqs)}")
    print(f"Veterinary Microbiology Core PYQs (VMC): {len(vmc_pyqs)}")
    print(f"Veterinary Biochemistry Core PYQs (VBC): {len(vbc_pyqs)}")
    print(f"New Expanded Veterinary Pathology (VPP): {len(new_vpp_300)}")
    print(f"New Expanded Veterinary Microbiology (VMC): {len(new_vmc_300)}")
    print(f"New Expanded Veterinary Anatomy (VAN): {len(new_van_150)}")

    all_core_pyqs = van_pyqs + vpp_pyqs + vmc_pyqs + vbc_pyqs
    assert len(all_core_pyqs) == 350, f"Expected 350 core PYQs, got {len(all_core_pyqs)}"

    # Check ID uniqueness across all new and pyq sets
    all_combined_new_and_pyq = all_core_pyqs + new_vpp_300 + new_vmc_300 + new_van_150
    ids = set()
    for q in all_combined_new_and_pyq:
        if q["id"] in ids:
            raise ValueError(f"Duplicate ID found: {q['id']}")
        ids.add(q["id"])

    # Paths
    root_dir = os.path.join(scripts_dir, "..")
    packs_dir = os.path.join(root_dir, "src", "data", "questionPacks")

    # Read base clean questions (565)
    base_json_path = os.path.join(packs_dir, "high_yield_clean_base.json")
    with open(base_json_path, "r", encoding="utf-8") as f:
        clean_base = json.load(f)

    clean_base = [
        q for q in clean_base 
        if 'Clinical Landmark MCQ' not in q.get('questionText', '')
        and not any('Standard validated laboratory' in opt for opt in q.get('options', []))
    ]
    print(f"Verified genuine base questions: {len(clean_base)}")

    master_1665 = clean_base + all_core_pyqs + new_vpp_300 + new_vmc_300 + new_van_150
    print(f"Total Master Questions: {len(master_1665)}")
    assert len(master_1665) == 1665, f"Expected 1,665 questions, got {len(master_1665)}"

    # Save initial un-shuffled JSONs
    with open(os.path.join(packs_dir, "vpp_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(new_vpp_300, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "vmc_300_new.json"), "w", encoding="utf-8") as f:
        json.dump(new_vmc_300, f, indent=2, ensure_ascii=False)
    with open(os.path.join(packs_dir, "van_150_new.json"), "w", encoding="utf-8") as f:
        json.dump(new_van_150, f, indent=2, ensure_ascii=False)

    print("Now executing apply_balance() to balance distractor indices across all 1665 questions...")
    from apply_balanced_options import apply_balance
    apply_balance()

if __name__ == "__main__":
    main()
