# scripts/option_parity_engine.py
"""
Intra-Question Option-Length Parity & Distractor Refinement Engine.
Strictly operates WITHIN each individual question (NEVER swaps distractors between questions).
Ensures:
1. Giveaway parentheticals, slash-synonyms, and trailing explanatory clauses on correct options are trimmed.
2. Across every subject and the entire 2,925-question bank, the correct option is strictly the longest
   option in only ~23-25% of questions (matching uniform random chance among 4 options), and never by a
   conspicuous giveaway margin.
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


def clean_correct_option(q_text: str, c_opt: str, d_opts: list[str], aggressive: bool = False) -> str:
    max_d = max(len(d) for d in d_opts)
    cur = c_opt.strip()
    d_lower = {d.strip().lower() for d in d_opts}
    ql = q_text.lower()

    # 1. Remove parenthetical (...) whenever cur > max_d
    if len(cur) > max_d and "(" in cur:
        no_paren = re.sub(r"\s*\([^)]*\)", "", cur).strip(" ,;-")
        if len(no_paren) >= 1 and no_paren.lower() not in d_lower:
            cur = no_paren

    # 2. Remove slash alternative (' / ' or '/')
    if len(cur) > max_d and "/" in cur and not any("/" in d for d in d_opts):
        if " / " in cur:
            parts = [p.strip() for p in cur.split(" / ") if len(p.strip()) >= 2 and p.strip().lower() not in d_lower]
            if parts:
                cur = min(parts, key=len)
        else:
            p0 = cur.split("/")[0].strip()
            if len(p0) >= 3 and p0.lower() not in d_lower:
                cur = p0

    # 3. Remove ' or ' alternative (case-insensitive) if distractors don't have ' or '
    if len(cur) > max_d and re.search(r"\s+or\s+", cur, flags=re.IGNORECASE) and not any(re.search(r"\s+or\s+", d, flags=re.IGNORECASE) for d in d_opts):
        p0 = re.split(r"\s+or\s+", cur, flags=re.IGNORECASE)[0].strip()
        if len(p0) >= 2 and p0.lower() not in d_lower:
            cur = p0

    # 4. Strip trailing explanatory clauses & participial phrases (loop until no more match)
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
                if len(cand) >= 3 and cand.lower() not in d_lower:
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
                    if cand.lower() not in d_lower:
                        cur = cand
                        break

    # 6. Apply concise standard veterinary abbreviations/replacements
    if len(cur) > max_d:
        for old_s, new_s in CONCISE_REPLACEMENTS:
            if old_s in cur and len(cur) > max_d:
                cand = cur.replace(old_s, new_s).strip(" ,")
                if len(cand) >= 3 and cand.lower() not in d_lower:
                    cur = cand

    # 7. Strip trailing prepositional modifier when distractors don't have it
    if len(cur) > max_d + 4:
        for prep in [
            " of the ", " in the ", " on the ", " at the ", " from the ",
            " into the ", " into ", " across the ", " through the ", " inside ",
            " from dam to ", " via ", " of ", " in "
        ]:
            if prep in cur and not any(prep in d for d in d_opts):
                cand = cur.split(prep)[0].strip(" ,")
                if len(cand) >= 8 and cand.lower() not in d_lower and not cand.lower().endswith((
                    'lack', 'absence', 'presence', 'increase', 'decrease', 'loss', 'fusion',
                    'union', 'branch', 'branches', 'site', 'form', 'type', 'types', 'stage',
                    'phase', 'rate', 'ratio', 'number', 'concentration', 'level', 'levels',
                    'activity', 'deficiency', 'excess', 'inhibition', 'activation', 'stimulation',
                    'degeneration', 'necrosis', 'inflammation', 'hypoplasia', 'atrophy',
                    'hypertrophy', 'hyperplasia', 'metaplasia', 'carcinoma', 'sarcoma',
                    'entrapment', 'migration', 'penetration', 'deposition', 'secretion',
                    'excretion', 'absorption', 'digestion', 'fermentation', 'oxidation',
                    'reduction', 'synthesis', 'hydrolysis', 'cleavage', 'binding',
                    'attachment', 'detachment', 'mobility', 'inability', 'failure', 'removal',
                    'halfway', 'between'
                )):
                    cur = cand
                    break

    # 8. Comma-separated list of 3+ items
    if len(cur) > max_d and cur.count(",") >= 2 and not any(d.count(",") >= 2 for d in d_opts) and "triad" not in ql and "three" not in ql and "four" not in ql:
        parts = [p.strip() for p in cur.replace(", and ", ", ").replace(" and ", ", ").split(",") if p.strip()]
        if len(parts) >= 3:
            cand = f"{parts[0]} and {parts[1]}"
            if len(cand) >= 6 and cand.lower() not in d_lower:
                cur = cand

    # 9. Compound ' and '
    if len(cur) > max_d + 4 and (" and " in cur or " AND " in cur):
        if not any(kw in ql for kw in STRICT_PAIR_STEM) and not any(kw in cur.lower() for kw in ("both ", "between ")):
            parts = re.split(r"\s+and\s+", cur, flags=re.IGNORECASE)
            p0 = parts[0].strip(" ,")
            if len(p0) >= 10 and p0.lower() not in d_lower and not p0.lower().endswith((
                'cranial', 'caudal', 'dorsal', 'ventral', 'medial', 'lateral',
                'internal', 'external', 'upper', 'lower', 'acute', 'chronic',
                'primary', 'secondary', 'left', 'right', 'both', 'terminal',
                'proximal', 'distal', 'intracytoplasmic', 'intranuclear'
            )):
                cur = p0
            elif len(parts) == 2 and len(parts[1].split()) >= 2:
                cand2 = parts[1].strip(" ,")
                if len(cand2) >= 10 and cand2.lower() not in d_lower:
                    cur = cand2[0].upper() + cand2[1:]

    if aggressive and len(cur) > max_d:
        cand = re.sub(r"\b(the|a|an)\s+", "", cur, flags=re.IGNORECASE).strip()
        if cand:
            cand = cand[0].upper() + cand[1:]
            if len(cand) >= 4 and cand.lower() not in d_lower:
                cur = cand

    return cur
