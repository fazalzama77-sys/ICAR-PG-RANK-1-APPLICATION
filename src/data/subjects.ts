import { Subject } from '../types';

export const SUBJECT_LIST: Subject[] = [
  // 1st Year - Veterinary Science (ICAR Major Subject Group Code 13)
  {
    id: 'van',
    name: 'Veterinary Anatomy',
    code: 'VAN',
    domain: 'veterinary_science',
    year: '1st_year',
    description: 'Gross anatomy, osteology, arthrology, myology, histology, embryology and neuroanatomy of domestic animals. (ICAR Code 13.1)',
    topics: [
      'Osteology & Arthrology',
      'Myology & Angiology',
      'Neurology & Special Senses',
      'Digestive, Respiratory & Urogenital Splanchnology',
      'General & Systemic Histology',
      'General & Applied Embryology & Avian Anatomy'
    ]
  },

  // 1st Year - Animal Science (ICAR Major Subject Group Code 14)
  {
    id: 'vpy',
    name: 'Veterinary Physiology',
    code: 'VPY',
    domain: 'animal_science',
    year: '1st_year',
    description: 'Cellular biophysics, blood, cardiovascular, respiratory, renal, digestive, endocrine and reproductive physiology. (ICAR Code 14.3)',
    topics: [
      'Blood, Hematology & Body Fluids',
      'Cardiovascular & Respiratory Physiology',
      'Digestive & Ruminant Physiology',
      'Renal & Environmental Physiology',
      'Neurophysiology, Muscle & Sense Organs',
      'Endocrinology, Reproduction & Lactation Physiology'
    ]
  },
  {
    id: 'vbc',
    name: 'Veterinary Biochemistry',
    code: 'VBC',
    domain: 'animal_science',
    year: '1st_year',
    description: 'Biomolecules, enzymology, bioenergetics, nutrient metabolism, molecular biology, and clinical diagnostic biochemistry. (ICAR Code 14 Unit II)',
    topics: [
      'Biomolecules: Carbohydrates, Lipids & Proteins',
      'Enzymology, Coenzymes & Bioenergetics',
      'Intermediary Metabolism (Carbs, Lipid, Amino Acid)',
      'Molecular Biology & Acid-Base / Electrolyte Balance',
      'Clinical & Diagnostic Biochemistry (Liver/Kidney Function)',
      'Biochemistry of Hormones, Vitamins & Minerals'
    ]
  },
  {
    id: 'lpm',
    name: 'Livestock Production Management',
    code: 'LPM',
    domain: 'animal_science',
    year: '1st_year',
    description: 'Principles of livestock management, shelter design, behavior, and production systems of ruminants, equines, swine and poultry.',
    topics: [
      'General Livestock Management, Housing & Behavior',
      'Dairy Cattle & Buffalo Production Management',
      'Sheep & Goat Production Management',
      'Swine, Equine & Camel Management',
      'Poultry Production, Broiler & Layer Management',
      'Hatchery Management, Biosecurity & Animal Welfare'
    ]
  },

  // 2nd Year - Veterinary Science
  {
    id: 'vpp',
    name: 'Veterinary Pathology',
    code: 'VPP',
    domain: 'veterinary_science',
    year: '2nd_year',
    description: 'General pathology, systemic pathology, infectious disease pathology, oncology, avian, necropsy and clinical pathology.',
    topics: [
      'General Pathology: Cell Injury, Degenerations & Necrosis',
      'Inflammation, Tissue Repair & Hemodynamic Disorders',
      'Systemic Pathology (Digestive, Respiratory, Cardiovascular, Urinary, Nervous & Reproductive)',
      'Pathology of Infectious Diseases (Bacterial, Viral, Fungal & Parasitic)',
      'Veterinary Oncology & Neoplasia',
      'Avian, Clinical & Necropsy Pathology'
    ]
  },
  {
    id: 'vmc',
    name: 'Veterinary Microbiology',
    code: 'VMC',
    domain: 'veterinary_science',
    year: '2nd_year',
    description: 'General and systematic bacteriology, veterinary mycology, veterinary virology, immunology and serology.',
    topics: [
      'General Bacteriology & Bacterial Genetics',
      'Systematic Bacteriology (Gram +ve, Gram -ve, Acid-Fast, Spirochetes & Mycoplasma)',
      'Veterinary Mycology & Mycotoxicoses',
      'General & Systematic Virology (DNA & RNA Animal/Poultry Viruses & Prions)',
      'Veterinary Immunology & Vaccinology',
      'Diagnostic Serology & Molecular Microbiology'
    ]
  },
  {
    id: 'vpa',
    name: 'Veterinary Parasitology',
    code: 'VPA',
    domain: 'veterinary_science',
    year: '2nd_year',
    description: 'Veterinary helminthology, veterinary entomology & acarology, and veterinary protozoology.',
    topics: [
      'General Parasitology & Helminthology: Trematodes (Flukes)',
      'Helminthology: Cestodes (Tapeworms & Metacestodes)',
      'Helminthology: Nematodes (Gastrointestinal, Bursate & Filarial)',
      'Veterinary Entomology (Flies, Myiasis, Lice & Fleas)',
      'Veterinary Acarology (Hard/Soft Ticks & Mange Mites)',
      'Veterinary Protozoology (Hemoprotozoa, Coccidia & Flagellates)'
    ]
  },

  // 2nd Year - Animal Science
  {
    id: 'agb',
    name: 'Animal Genetics & Breeding',
    code: 'AGB',
    domain: 'animal_science',
    year: '2nd_year',
    description: 'Principles of genetics, population & quantitative genetics, molecular genetics and livestock breeding strategies.',
    topics: [
      'Mendelian, Chromosomal & Cytogenetics',
      'Molecular Genetics, Genomics & Markers',
      'Population Genetics (Hardy-Weinberg Equilibrium & Gene Frequency)',
      'Quantitative Genetics (Variance, Heritability, Repeatability & Correlations)',
      'Selection Methods, Sire Evaluation & Breeding Values (BLUP)',
      'Mating Systems, Heterosis, Breeds & Conservation'
    ]
  },
  {
    id: 'ann',
    name: 'Animal Nutrition',
    code: 'ANN',
    domain: 'animal_science',
    year: '2nd_year',
    description: 'Principles of animal nutrition, nutrient digestion & metabolism, feed processing, applied ruminant and monogastric feeding.',
    topics: [
      'Principles of Nutrition, Proximate Analysis & Nutrient Metabolism',
      'Feed Evaluation & Energy/Protein Partitioning (TDN, ME, NE, RUP/RDP)',
      'Forage Conservation (Silage, Hay), Feed Processing & Anti-Nutritional Factors',
      'Minerals, Vitamins, Feed Additives & Metabolic Deficiency Diseases',
      'Applied Ruminant Nutrition (Dairy Cattle, Buffalo, Sheep & Goat)',
      'Applied Monogastric, Poultry & Pet/Equine Nutrition'
    ]
  },

  // Advanced Years (Extensible for future years)
  {
    id: 'vpt',
    name: 'Veterinary Pharmacology & Toxicology',
    code: 'VPT',
    domain: 'veterinary_science',
    year: '3rd_year',
    description: 'Pharmacokinetics, pharmacodynamics, autonomic, CNS, chemotherapeutic agents, and veterinary toxicology.',
    topics: ['General Pharmacology', 'Autonomic Pharmacology', 'Chemotherapy', 'Toxicology']
  },
  {
    id: 'vpe',
    name: 'Veterinary Public Health & Epidemiology',
    code: 'VPE',
    domain: 'veterinary_science',
    year: '3rd_year',
    description: 'Zoonotic diseases, food safety (meat & milk hygiene), epidemiology and one-health principles.',
    topics: ['Zoonoses', 'Meat & Milk Hygiene', 'Veterinary Epidemiology']
  }
];

export const DOMAIN_LABELS: Record<string, string> = {
  veterinary_science: 'Veterinary Science (Code 13)',
  animal_science: 'Animal Sciences (Code 14)'
};

export const YEAR_LABELS: Record<string, string> = {
  '1st_year': '1st Professional Year',
  '2nd_year': '2nd Professional Year',
  '3rd_year': '3rd Professional Year',
  '4th_year': '4th Professional Year',
  '5th_year': '5th Professional Year'
};
