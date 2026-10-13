# scripts/option_parity_engine.py
"""
Intra-Question Option-Length Parity & Distractor Refinement Engine.
Strictly operates WITHIN each individual question (NEVER swaps distractors between questions).
Ensures:
1. Giveaway parentheticals, slash-synonyms, and trailing explanatory clauses on correct options are trimmed
   without ever leaving a dangling preposition or adjective.
2. Across every subject and the entire 2,925-question bank, the correct option is strictly the longest
   option in ~21-24.8% of questions (matching uniform random chance among 4 options).
"""
import re
import random

STRICT_PAIR_STEM = (
    'which two', 'which 2', 'both ', 'union of', 'between which',
    'ratio of', 'pair of', 'triad'
)

CONCISE_REPLACEMENTS = [
    ("Central Nervous System", "CNS"),
    ("central nervous system", "CNS"),
    ("Autonomous Nervous System", "ANS"),
    ("autonomic nervous system", "ANS"),
    ("Gastrointestinal tract", "GI tract"),
    ("gastrointestinal tract", "GI tract"),
    ("Rough endoplasmic reticulum", "Rough ER"),
    ("rough endoplasmic reticulum", "rough ER"),
    ("Smooth endoplasmic reticulum", "Smooth ER"),
    ("smooth endoplasmic reticulum", "smooth ER"),
    ("endoplasmic reticulum", "ER"),
    ("reticuloendothelial system", "RES"),
    ("polymorphonuclear leukocytes", "neutrophils"),
    ("Polymorphonuclear leukocytes", "Neutrophils"),
    ("red blood cells", "erythrocytes"),
    ("Red blood cells", "Erythrocytes"),
    ("white blood cells", "leukocytes"),
    ("White blood cells", "Leukocytes"),
    ("cerebrospinal fluid", "CSF"),
    ("Cerebrospinal fluid", "CSF"),
    ("immunoglobulin ", "Ig "),
    ("Immunoglobulin ", "Ig "),
    ("immunoglobulins", "Igs"),
    ("Immunoglobulins", "Igs"),
    ("adenosine triphosphate", "ATP"),
    ("molecular weight", "MW"),
    ("degrees Fahrenheit", "degrees F"),
    ("degrees Celsius", "degrees C"),
    ("Dietary Cation-Anion Difference", "DCAD"),
    ("Angiotensin-Converting Enzyme", "ACE"),
    ("Insulin-like Growth Factor 1", "IGF-1"),
    ("is characterized by ", ""),
    ("characterized by ", ""),
    ("which is responsible for ", "for "),
    ("that is responsible for ", "for "),
    ("in the presence of ", "with "),
    ("as a result of ", "from "),
    ("at the level of the ", "at the "),
    ("in the region of the ", "in the "),
    ("on the surface of the ", "on the "),
    ("within the cytoplasm of ", "in "),
    ("within the nucleus of ", "in "),
]

# Authentic, concise veterinary appositives/synonyms for short distractors
EXACT_TERM_EXPANSIONS = {
    "ox": "Domestic cattle (Bos taurus)",
    "cattle": "Domestic cattle (Bos taurus)",
    "cow": "Dairy cattle (Bos taurus)",
    "buffalo": "Riverine buffalo (Bubalus bubalis)",
    "horse": "Domestic horse (Equus caballus)",
    "dog": "Domestic dog (Canis familiaris)",
    "cat": "Domestic cat (Felis catus)",
    "pig": "Domestic pig (Sus scrofa)",
    "swine": "Domestic swine (Sus scrofa)",
    "sheep": "Domestic sheep (Ovis aries)",
    "goat": "Domestic goat (Capra hircus)",
    "fowl": "Domestic fowl (Gallus domesticus)",
    "chicken": "Domestic chicken (Gallus gallus)",
    "poultry": "Domestic poultry (Gallus domesticus)",
    "camel": "Dromedary camel (Camelus dromedarius)",
    "rabbit": "Laboratory rabbit (Oryctolagus cuniculus)",
    "heart": "Ventricular myocardium and endocardium",
    "myocardium": "Ventricular cardiac myocardium",
    "kidney": "Renal cortex and medullary tubules",
    "kidneys": "Renal cortex and medullary parenchyma",
    "liver": "Hepatic lobular parenchyma and sinusoids",
    "spleen": "Splenic red pulp and lymphoid follicles",
    "lung": "Pulmonary alveolar parenchyma and bronchi",
    "lungs": "Pulmonary alveolar and bronchiolar tissue",
    "brain": "Cerebral cortex and brainstem nuclei",
    "trachea": "Cartilaginous cervical and thoracic trachea",
    "alveoli": "Thin-walled pulmonary alveolar sacs",
    "femur": "Proximal and distal extremity of femur",
    "tibia": "Proximal and distal shaft of tibia",
    "radius": "Proximal and diaphyseal shaft of radius",
    "ulna": "Olecranon process and shaft of ulna",
    "humerus": "Diaphysis and distal condyle of humerus",
    "scapula": "Lateral surface and spine of scapula",
    "rabies": "Rabies street virus (Lyssavirus)",
    "anthrax": "Peracute septicemic anthrax (B. anthracis)",
    "blackleg": "Black quarter (Clostridium chauvoei)",
    "glanders": "Cutaneous and pulmonary glanders (B. mallei)",
    "rinderpest": "Classical rinderpest (Morbillivirus)",
    "bluetongue": "Bluetongue viral orbivirus infection",
    "brucellosis": "Bovine contagious abortion (B. abortus)",
    "tuberculosis": "Chronic fibrocaseous bovine tuberculosis",
    "johne's disease": "Chronic granulomatous paratuberculosis",
    "poxvirus": "Cytoplasmic brick-shaped Poxviridae",
    "rotavirus": "Double-stranded segmented RNA Rotavirus",
    "retrovirus": "Reverse-transcriptase RNA Retroviridae",
    "herpesvirus": "Double-stranded DNA Herpesviridae",
    "adenovirus": "Non-enveloped icosahedral Adenoviridae",
    "parvovirus": "Single-stranded DNA Parvoviridae",
    "birnavirus": "Bisegmented dsRNA Avibirnavirus",
    "coronavirus": "Enveloped positive-sense RNA Coronaviridae",
    "pyknosis": "Nuclear shrinkage and chromatin condensation",
    "karyolysis": "Enzymatic dissolution of nuclear chromatin",
    "karyorrhexis": "Fragmentation of condensed nuclear chromatin",
    "fatty change": "Intracellular neutral triglyceride steatosis",
    "amyloid": "Extracellular beta-pleated fibrillar amyloid",
    "glycogen": "Intracellular PAS-positive glycogen granules",
    "hemosiderin": "Prussian blue-positive ferric hemosiderin",
    "lipofuscin": "Perinuclear wear-and-tear lipofuscin pigment",
    "melanin": "Masson-Fontana positive endogenous melanin",
    "amylase": "Pancreatic alpha-amylase glycolytic enzyme",
    "pepsin": "Gastric chief-cell pepsinogen protease",
    "trypsin": "Pancreatic serine protease trypsinogen",
    "enterokinase": "Duodenal brush-border enteropeptidase",
    "lipase": "Pancreatic colipase-dependent lipase",
    "renin": "Juxtaglomerular aspartyl protease renin",
    "kallikrein": "Plasma and tissue serine protease kallikrein",
    "insulin": "Pancreatic beta-cell peptide hormone insulin",
    "thyroxine": "Follicular tetraiodothyronine (T4) hormone",
    "calcitonin": "Parafollicular C-cell hypocalcemic calcitonin",
}

FORBIDDEN_ENDING_WORDS = {
    'of', 'in', 'to', 'for', 'with', 'on', 'at', 'from', 'by', 'into',
    'and', 'or', 'the', 'a', 'an', 'as', 'is', 'are', 'that', 'which',
    'both', 'between', 'structural', 'ileal', 'epithelial', 'definitive',
    'cranial', 'caudal', 'dorsal', 'ventral', 'medial', 'lateral',
    'internal', 'external', 'upper', 'lower', 'acute', 'chronic',
    'primary', 'secondary', 'left', 'right', 'terminal', 'proximal',
    'distal', 'intracytoplasmic', 'intranuclear', 'soluble', 'insoluble',
    'reversible', 'irreversible', 'positive', 'negative', 'high', 'low'
}


def is_valid_tightened_phrase(cand: str, d_lower: set[str]) -> bool:
    if not cand or len(cand) < 2:
        return False
    if cand.lower() in d_lower:
        return False
    words = cand.rstrip(".,;)").split()
    if not words:
        return False
    last_w = words[-1].lower()
    if last_w in FORBIDDEN_ENDING_WORDS:
        return False
    return True


def clean_correct_option(q_text: str, c_opt: str, d_opts: list[str], aggressive: bool = False) -> str:
    max_d = max(len(d) for d in d_opts)
    cur = c_opt.strip()
    d_lower = {d.strip().lower() for d in d_opts}

    # 1. Remove parenthetical (...) whenever cur > max_d and not all distractors have parens
    if len(cur) > max_d and "(" in cur and (aggressive or not all("(" in d for d in d_opts)):
        no_paren = re.sub(r"\s*\([^)]*\)", "", cur).strip(" ,;-")
        if is_valid_tightened_phrase(no_paren, d_lower):
            cur = no_paren

    # 2. Remove slash alternative (' / ' or '/')
    if len(cur) > max_d and "/" in cur and not any("/" in d for d in d_opts):
        if " / " in cur:
            parts = [p.strip() for p in cur.split(" / ") if is_valid_tightened_phrase(p.strip(), d_lower)]
            if parts:
                cur = min(parts, key=len)
        else:
            p0 = cur.split("/")[0].strip()
            if len(p0) >= 4 and is_valid_tightened_phrase(p0, d_lower):
                cur = p0

    # 3. Remove ' or ' alternative if distractors don't have ' or '
    if len(cur) > max_d and re.search(r"\s+or\s+", cur, flags=re.IGNORECASE) and not any(re.search(r"\s+or\s+", d, flags=re.IGNORECASE) for d in d_opts):
        p0 = re.split(r"\s+or\s+", cur, flags=re.IGNORECASE)[0].strip()
        if len(p0) >= 4 and is_valid_tightened_phrase(p0, d_lower):
            cur = p0

    # 4. Strip trailing explanatory clauses & participial phrases
    changed = True
    while changed and len(cur) > max_d:
        changed = False
        for sep in [
            " — ", " - ", ", which ", " which ", ", that ", " that ",
            ", causing ", " causing ", ", resulting in ", " resulting in ",
            ", characterized by ", " characterized by ", ", leading to ", " leading to ",
            ", producing ", " producing ", ", forming ", " forming ",
            ", reducing ", " reducing ", ", regulating ", " regulating ",
            ", releasing ", " releasing ", ", trapping ", " trapping ",
            ", contacting ", " contacting ", ", preventing ", " preventing ",
            ", allowing ", " allowing ", ", inducing ", " inducing ",
            ", transferring ", " transferring ", ", secreting ", " secreting ",
            ", exacerbated by ", " exacerbated by ", ", interfering with ", " interfering with ",
            ", joined at ", " joined at ", ", using ", " using ",
            ", making ", ", giving ", ", especially ", ", particularly ",
            ", with ", " with obligatory ", ", where ",
            " instead of ", " rather than ", " due to ",
            " to form ", " to produce ", " to prevent ", " to suck ", " in order to ",
            " for continued ", " in the presence of ", " buffered at ",
            " by inhibiting ", " by activating ", " by blocking ", " by binding ",
            " located ", " situated ", " found in ", " present in ",
            " secreted by ", " produced by ", " synthesized in ", " synthesized by ",
            " derived from ", " originating from ", " mediated by ", "; "
        ]:
            if sep in cur and not any(sep in d for d in d_opts):
                cand = cur.split(sep)[0].strip(" ,;-")
                if len(cand) >= 4 and is_valid_tightened_phrase(cand, d_lower):
                    cur = cand
                    changed = True
                    break

    # 5. Strip redundant leading filler phrases
    if len(cur) > max_d:
        for prefix in [
            "The presence of a ", "The presence of ", "Presence of a ", "Presence of ",
            "Complete absence of ", "The absence of ", "A marked increase in ",
            "An increased level of ", "Predominantly ", "Specifically ",
            "Characteristic ", "Classic ", "Definitive ", "Seasonally polyestrous ",
            "Extensive trans-uterine "
        ]:
            if cur.startswith(prefix) and not any(d.startswith(prefix) for d in d_opts):
                cand = cur[len(prefix):].strip()
                if len(cand) >= 4:
                    cand = cand[0].upper() + cand[1:]
                    if is_valid_tightened_phrase(cand, d_lower):
                        cur = cand
                        break

    # 6. Apply concise standard veterinary abbreviations/replacements
    if len(cur) > max_d:
        for old_s, new_s in CONCISE_REPLACEMENTS:
            if old_s in cur and len(cur) > max_d:
                cand = cur.replace(old_s, new_s).strip(" ,")
                if is_valid_tightened_phrase(cand, d_lower):
                    cur = cand

    # 7. Strip trailing locative/manner prepositional modifier when distractors don't have it
    thresh = max_d if aggressive else max_d + 4
    if len(cur) > thresh:
        for prep in [
            " in the ", " on the ", " at the ", " from the ", " into the ",
            " into ", " across the ", " through the ", " inside ", " within the ",
            " during ", " following ", " throughout the ", " via "
        ]:
            if prep in cur and not any(prep in d for d in d_opts):
                cand = cur.split(prep)[0].strip(" ,")
                if len(cand) >= 8 and is_valid_tightened_phrase(cand, d_lower):
                    cur = cand
                    break

    # 8. Comma-separated list of 3+ items (when stem doesn't ask for triad/three/four)
    ql = q_text.lower()
    if len(cur) > max_d and cur.count(",") >= 2 and not any(d.count(",") >= 2 for d in d_opts) and "triad" not in ql and "three" not in ql and "four" not in ql:
        parts = [p.strip() for p in cur.replace(", and ", ", ").replace(" and ", ", ").split(",") if p.strip()]
        if len(parts) >= 3:
            cand = f"{parts[0]} and {parts[1]}"
            if len(cand) >= 6 and is_valid_tightened_phrase(cand, d_lower):
                cur = cand

    # 9. Compound ' and ' when first clause is complete and valid
    if len(cur) > thresh and (" and " in cur or " AND " in cur):
        if not any(kw in ql for kw in STRICT_PAIR_STEM) and not any(kw in cur.lower() for kw in ("both ", "between ")):
            parts = re.split(r"\s+and\s+", cur, flags=re.IGNORECASE)
            p0 = parts[0].strip(" ,")
            if len(p0) >= 10 and is_valid_tightened_phrase(p0, d_lower) and not p0.lower().endswith(('al', 'ic', 'ar', 'ous', 'ive', 'ary', 'ed', 'ing')):
                cur = p0
            elif len(parts) == 2 and len(parts[1].split()) >= 2:
                cand2 = parts[1].strip(" ,")
                if len(cand2) >= 10 and is_valid_tightened_phrase(cand2, d_lower):
                    cur = cand2[0].upper() + cand2[1:]

    if aggressive and len(cur) > max_d:
        # Remove non-essential adverbs
        for adv in [
            "directly ", "completely ", "exclusively ", "primarily ", "specifically ",
            "progressively ", "intensely ", "markedly ", "severely ", "rapidly ",
            "readily ", "selectively ", "continually ", "continuously ", "typically ",
            "classically ", "predominantly ", "generalized "
        ]:
            if adv in cur.lower() and len(cur) > max_d:
                cand = re.sub(re.escape(adv), "", cur, count=1, flags=re.IGNORECASE).strip()
                if cand:
                    cand = cand[0].upper() + cand[1:]
                    if is_valid_tightened_phrase(cand, d_lower):
                        cur = cand

    if aggressive and len(cur) > max_d:
        # Remove articles ("the ", "a ", "an ")
        cand = re.sub(r"\b(the|a|an)\s+", "", cur, flags=re.IGNORECASE).strip()
        if cand:
            cand = cand[0].upper() + cand[1:]
            if is_valid_tightened_phrase(cand, d_lower):
                cur = cand

    return cur


def enrich_distractor_naturally(d_text: str, c_text: str) -> str:
    """
    Only uses authentic veterinary lexicon synonyms, numeric range format matching,
    or shared category tail nouns (NEVER generic boilerplate suffixes!).
    """
    cur = d_text.strip()
    low = cur.lower().strip(".")
    if low in EXACT_TERM_EXPANSIONS:
        return EXACT_TERM_EXPANSIONS[low]

    # 1. If c_text is "X or Y" and cur is a single integer "N"
    if re.fullmatch(r"\d+", cur) and re.fullmatch(r"\d+\s+or\s+\d+", c_text.strip()):
        n = int(cur)
        return f"{max(1, n-1)} or {n}"

    # 2. If c_text is a numeric range "X to Y <unit>" and cur is a single number "<Z> <unit>"
    c_range_m = re.match(r"^(\d+(?:\.\d+)?)\s+to\s+(\d+(?:\.\d+)?)\s+(.+)$", c_text.strip())
    d_num_m = re.match(r"^(\d+(?:\.\d+)?)\s+(.+)$", cur)
    if c_range_m and d_num_m and " to " not in cur:
        c_unit = c_range_m.group(3).strip()
        z_str = d_num_m.group(1)
        if "." in z_str:
            z = float(z_str)
            step = max(0.5, round(z * 0.1, 1))
            return f"{z - step:.1f} to {z + step:.1f} {c_unit}"
        else:
            z = int(z_str)
            step = 1 if z < 15 else (5 if z >= 50 else 2)
            return f"{max(1, z - step)} to {z + step} {c_unit}"

    # 3. Check shared category tail noun or trailing unit phrase from c_text
    tail_nouns = [
        "nerves", "nerve", "veins", "vein", "arteries", "artery", "muscles", "muscle",
        "bones", "bone", "ligaments", "ligament", "glands", "gland", "cells", "cell",
        "fibers", "hormones", "hormone", "enzymes", "enzyme", "receptors", "receptor",
        "antibodies", "antibody", "toxins", "toxin", "viruses", "virus", "bacteria",
        "cartilages", "cartilage", "foramina", "foramen", "processes", "process",
        "sinuses", "sinus", "nodes", "node", "ducts", "duct", "valves", "valve",
        "pathways", "pathway", "deficiency", "poisoning", "toxicity", "syndrome",
        "degeneration", "necrosis", "inflammation", "infection", "infections",
        "calcification", "hypersensitivity", "carcinoma", "sarcoma", "adenoma", "lymphoma"
    ]
    c_words = c_text.rstrip(".").split()
    if c_words:
        last_w = c_words[-1].lower()
        if last_w in tail_nouns and not cur.lower().rstrip(".").endswith(last_w):
            return cur.rstrip(".") + " " + last_w

    return cur


def equalize_question_bank_options(questions: list[dict], target_max_longest_rate: float = 0.242) -> list[dict]:
    """
    Balances option lengths per subject using strictly authentic, non-boilerplate intra-question
    refinements so that in every subject, the correct option is strictly the longest option
    no more than ~24.2% of the time.
    """
    by_subject = {}
    for q in questions:
        by_subject.setdefault(q["subjectId"], []).append(q)

    result_map = {}

    for subj, subj_qs in sorted(by_subject.items()):
        n_subj = len(subj_qs)
        target_longest = int(n_subj * target_max_longest_rate)

        working = [dict(q, options=list(q["options"])) for q in subj_qs]

        # Rank questions where c_opt is currently strictly longest, sorted by diff descending
        candidates = []
        for idx, q in enumerate(working):
            c_idx = q["correctOptionIndex"]
            c_opt = q["options"][c_idx]
            d_opts = [o for i, o in enumerate(q["options"]) if i != c_idx]
            diff = len(c_opt) - max(len(d) for d in d_opts)
            if diff > 0:
                candidates.append((diff, idx))

        candidates.sort(key=lambda x: (-x[0], x[1]))

        cur_longest_count = len(candidates)
        for diff, idx in candidates:
            # Stop once this subject is at or below target_longest AND remaining diffs are small (<= 14 chars)
            if cur_longest_count <= target_longest and diff <= 14:
                break
            q = working[idx]
            c_idx = q["correctOptionIndex"]
            c_opt = q["options"][c_idx]
            d_indices = [i for i in range(4) if i != c_idx]
            d_opts = [q["options"][i] for i in d_indices]

            # Step 1: non-aggressive clean_correct_option + natural distractor format matching
            new_c = clean_correct_option(q["questionText"], c_opt, d_opts, aggressive=False)
            new_ds = [enrich_distractor_naturally(q["options"][i], new_c) for i in d_indices]
            if len(new_c) <= max(len(d) for d in new_ds):
                q["options"][c_idx] = new_c
                for di, nd in zip(d_indices, new_ds):
                    q["options"][di] = nd
                cur_longest_count -= 1
                continue

            # Step 2: aggressive clean_correct_option + natural distractor format matching
            new_c_agg = clean_correct_option(q["questionText"], c_opt, d_opts, aggressive=True)
            new_ds_agg = [enrich_distractor_naturally(q["options"][i], new_c_agg) for i in d_indices]
            q["options"][c_idx] = new_c_agg
            for di, nd in zip(d_indices, new_ds_agg):
                q["options"][di] = nd
            if len(new_c_agg) <= max(len(d) for d in new_ds_agg):
                cur_longest_count -= 1

        for q in working:
            result_map[q["id"]] = q

    return [result_map[q["id"]] for q in questions]


if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from data_van import get_van_questions
    from data_vpy import get_vpy_questions
    from data_vbc import get_vbc_questions
    from data_lpm import get_lpm_questions
    from data_vpp import get_vpp_questions
    from data_vmc import get_vmc_questions
    from data_vpa import get_vpa_questions
    from data_agb import get_agb_questions
    from data_ann import get_ann_questions
    from enrich_to_120 import SUPPLEMENTARY_POOLS
    from pyq_van import get_van_pyqs
    from pyq_vpp import get_vpp_pyqs
    from pyq_vmc import get_vmc_pyqs
    from pyq_vbc import get_vbc_pyqs
    from build_pathology_300 import get_all_300_vpp_questions
    from build_microbiology_300 import get_all_300_vmc_questions
    from build_anatomy_150 import get_all_150_van_questions
    from build_parasitology_60 import get_all_60_vpa_questions
    from build_pathology_350_part2 import get_all_350_vpp_part2_questions
    from build_microbiology_350_part2 import get_all_350_vmc_part2_questions
    from build_nutrition_250 import get_all_250_ann_questions
    from build_genetics_250 import get_all_250_agb_questions

    def is_dummy(q):
        q_text = q.get('questionText', '')
        topic = q.get('topic', '')
        opts = q.get('options', [])
        return ('Clinical Landmark MCQ #' in q_text or 'Core Diagnostic' in topic or any('Standard validated laboratory' in opt for opt in opts))

    vpy_init = get_vpy_questions()
    vpy_supp = []
    for q_text, opts, ans, exp in SUPPLEMENTARY_POOLS.get('vpy', []):
        idx = len(vpy_init) + len(vpy_supp) + 1
        vpy_supp.append({'id': f'vpy_q_{idx:03d}', 'domain': 'animal_science', 'year': '1st_year', 'subjectId': 'vpy', 'topic': 'Veterinary Physiology High-Yield Core', 'questionText': q_text, 'options': list(opts), 'correctOptionIndex': ans, 'explanation': exp, 'difficulty': 'Medium', 'tags': ['Veterinary Physiology', 'ICAR PG Core'], 'createdAt': 1773000000000 + idx})

    base = [q for qs in [get_van_questions(), vpy_init + vpy_supp, get_vbc_questions(), get_lpm_questions(), get_vpp_questions(), get_vmc_questions(), get_vpa_questions(), get_agb_questions(), get_ann_questions()] for q in qs if not is_dummy(q)]
    pyqs = get_van_pyqs() + get_vpp_pyqs() + get_vmc_pyqs() + get_vbc_pyqs()
    exp1 = get_all_300_vpp_questions() + get_all_300_vmc_questions() + get_all_150_van_questions() + get_all_60_vpa_questions()
    exp2 = get_all_350_vpp_part2_questions() + get_all_350_vmc_part2_questions() + get_all_250_ann_questions() + get_all_250_agb_questions()
    all_2925 = base + pyqs + exp1 + exp2

    eq = equalize_question_bank_options(all_2925)
    for s in sorted(set(q["subjectId"] for q in eq)):
        sqs = [q for q in eq if q["subjectId"] == s]
        lc = sum(1 for q in sqs if len(q["options"][q["correctOptionIndex"]]) == max(len(o) for o in q["options"]) and sum(1 for o in q["options"] if len(o) == max(len(x) for x in q["options"])) == 1)
        lw = sum(1 for q in sqs if len(q["options"][q["correctOptionIndex"]].split()) == max(len(o.split()) for o in q["options"]) and sum(1 for o in q["options"] if len(o.split()) == max(len(x.split()) for x in q["options"])) == 1)
        print(f"[{s.upper()}] Total: {len(sqs):3d} | Char-longest correct: {lc:3d} ({lc/len(sqs)*100:4.1f}%) | Word-longest correct: {lw:3d} ({lw/len(sqs)*100:4.1f}%)")
    tot_c = sum(1 for q in eq if len(q["options"][q["correctOptionIndex"]]) == max(len(o) for o in q["options"]) and sum(1 for o in q["options"] if len(o) == max(len(x) for x in q["options"])) == 1)
    tot_w = sum(1 for q in eq if len(q["options"][q["correctOptionIndex"]].split()) == max(len(o.split()) for o in q["options"]) and sum(1 for o in q["options"] if len(o.split()) == max(len(x.split()) for x in q["options"])) == 1)
    print(f"OVERALL ({len(eq)} Qs): Char-longest correct: {tot_c}/{len(eq)} ({tot_c/len(eq)*100:.1f}%) | Word-longest correct: {tot_w}/{len(eq)} ({tot_w/len(eq)*100:.1f}%)")
