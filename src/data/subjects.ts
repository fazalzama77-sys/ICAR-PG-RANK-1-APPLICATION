import { Subject } from '../types';

export const SUBJECT_LIST: Subject[] = [
  // 1st Year - Veterinary Science
  {
    id: 'van',
    name: 'Veterinary Anatomy',
    code: 'VAN',
    domain: 'veterinary_science',
    year: '1st_year',
    description: 'Gross anatomy, osteology, arthrology, myology, histology, embryology and neuroanatomy of domestic animals.',
    topics: [
      'Osteology & Arthrology',
      'Myology & Angiology',
      'Neurology & Splanchnology',
      'Systemic & General Histology',
      'General & Applied Embryology',
      'Avian Anatomy'
    ]
  },
  {
    id: 'vpy',
    name: 'Veterinary Physiology',
    code: 'VPY',
    domain: 'veterinary_science',
    year: '1st_year',
    description: 'Cellular biophysics, blood, cardiovascular, respiratory, renal, digestive, endocrine and reproductive physiology.',
    topics: [
      'Hematology & Cardiovascular System',
      'Respiration & Environmental Physiology',
      'Digestive Physiology (Ruminant & Non-ruminant)',
      'Excretion & Body Fluids',
      'Endocrine & Neurophysiology',
      'Reproductive & Lactation Physiology'
    ]
  },
  {
    id: 'vbc',
    name: 'Veterinary Biochemistry',
    code: 'VBC',
    domain: 'veterinary_science',
    year: '1st_year',
    description: 'Biomolecules, enzymology, bioenergetics, metabolism, molecular biology, and clinical diagnostic biochemistry.',
    topics: [
      'Biomolecules & Enzymes',
      'Intermediary Metabolism (Carbs, Lipids, Proteins)',
      'Bioenergetics & Biological Oxidation',
      'Molecular Biology (Replication, Transcription, Translation)',
      'Clinical Biochemistry & Diagnostic Enzymology',
      'Mineral, Vitamin & Hormone Chemistry'
    ]
  },

  // 1st Year - Animal Science
  {
    id: 'lpm',
    name: 'Livestock Production Management',
    code: 'LPM',
    domain: 'animal_science',
    year: '1st_year',
    description: 'Principles of livestock management, shelter design, behavior, and production systems of ruminants, equines, swine and poultry.',
    topics: [
      'General Livestock Management & Housing',
      'Dairy Cattle & Buffalo Management',
      'Sheep & Goat Management',
      'Swine, Equine & Camel Management',
      'Broiler & Layer Poultry Production',
      'Hatchery Operations & Biosecurity'
    ]
  },

  // 2nd Year - Veterinary Science
  {
    id: 'vpp',
    name: 'Veterinary Pathology',
    code: 'VPP',
    domain: 'veterinary_science',
    year: '2nd_year',
    description: 'General pathology, systemic pathology, infectious disease pathology, oncology, necropsy and clinical pathology.',
    topics: [
      'General Pathology (Degenerations, Necrosis, Inflammation)',
      'Hemodynamic Disorders & Shock',
      'Systemic Pathology (Respiratory, Digestive, Urogenital, CNS)',
      'Pathology of Infectious Diseases (Bacterial, Viral, Fungal)',
      'Veterinary Oncology & Neoplasia',
      'Necropsy Procedures & Clinical Pathology'
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
      'Systematic Bacteriology (Gram +ve & Gram -ve Pathogens)',
      'Veterinary Mycology (Dermatophytes, Systemic Mycoses)',
      'General & Systematic Virology (DNA & RNA Animal Viruses)',
      'Immunology (Innate & Adaptive, Hypersensitivity, Vaccines)',
      'Diagnostic Serology & Molecular Diagnostics'
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
      'Helminthology: Trematodes (Flukes)',
      'Helminthology: Cestodes (Tapeworms)',
      'Helminthology: Nematodes (Roundworms)',
      'Veterinary Entomology (Diptera, Lice, Fleas)',
      'Veterinary Acarology (Ticks & Mites)',
      'Veterinary Protozoology (Trypanosoma, Babesia, Theileria, Coccidia)'
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
      'Principles of Genetics & Cytogenetics',
      'Population Genetics (Hardy-Weinberg equilibrium, Gene Frequency)',
      'Quantitative Genetics (Heritability, Repeatability, Correlations)',
      'Selection Methods & Breeding Values (BLUP, Selection Index)',
      'Breeding Systems (Inbreeding, Outbreeding, Crossbreeding)',
      'Conservation of Indigenous Animal Genetic Resources'
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
      'Principles of Animal Nutrition & Nutrient Metabolism',
      'Feed Evaluation & Energy/Protein Partitioning (TDN, ME, NE)',
      'Feedstuffs, Forage Conservation (Silage/Hay) & Anti-Nutrients',
      'Applied Ruminant Nutrition (Dairy, Beef, Small Ruminants)',
      'Applied Monogastric Nutrition (Swine & Poultry)',
      'Feed Additives, Minerals, Vitamins & Metabolic Disorders'
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
  veterinary_science: 'Veterinary Science Subjects',
  animal_science: 'Animal Science Subjects'
};

export const YEAR_LABELS: Record<string, string> = {
  '1st_year': '1st Professional Year',
  '2nd_year': '2nd Professional Year',
  '3rd_year': '3rd Professional Year',
  '4th_year': '4th Professional Year',
  '5th_year': '5th Professional Year'
};
