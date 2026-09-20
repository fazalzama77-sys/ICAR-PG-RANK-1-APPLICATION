# scripts/pyq_vmc.py
# 100 ICAR AIEEA PG (M.V.Sc.) Previous Year Question (PYQ) Style MCQs for Veterinary Microbiology (VMC)

def get_vmc_pyqs():
    pyqs = [
        # 1-10: General Bacteriology, Morphology, Staining & Physiology
        ("The 'McFadyean reaction' used for presumptive diagnosis of Anthrax in blood smears stains which component of Bacillus anthracis?",
         ["Capsule (poly-D-glutamic acid) pink/purple with blue bacterial cell body using polychrome methylene blue", "Somatic cell wall using crystal violet", "Endospore green using malachite green", "Flagella using silver nitrate"],
         0, "Polychrome methylene blue stain demonstrates the capsular material of B. anthracis as a reddish-purple/pink halo around dark-blue truncated rods (McFadyean reaction)."),

        ("The unique capsule of Bacillus anthracis is chemically composed of:",
         ["Poly-D-glutamic acid (polypeptide)", "Hyaluronic acid", "Complex polysaccharide", "Lipopolysaccharide"],
         0, "Unlike most bacterial capsules which are polysaccharide, Bacillus anthracis possesses a polypeptide capsule made of poly-D-glutamic acid, encoded by the pXO2 plasmid."),

        ("The lethal toxin of Bacillus anthracis is composed of which two synergistic proteins?",
         ["Protective Antigen (PA) + Lethal Factor (LF)", "Protective Antigen (PA) + Edema Factor (EF)", "Lethal Factor (LF) + Edema Factor (EF)", "Alpha toxin + Perfringolysin"],
         0, "Anthrax toxin consists of three components on plasmid pXO1: PA binds host receptors and translocates LF (a zinc-metalloprotease that cleaves MAPKK) or EF (a calmodulin-dependent adenylate cyclase)."),

        ("The 'Ascoli thermoprecipitin test' is a diagnostic ring precipitation test used to detect anthrax antigens in:",
         ["Hides, skins, and decomposing tissues of suspected carcasses", "Milk from mastitic cows", "Fresh urine samples", "Serum of vaccinated animals"],
         0, "Ascoli's test utilizes thermostable anthrax polysaccharide antigens extracted by boiling suspect hide/tissue in saline, layered over anthrax hyperimmune serum to form a ring precipitate."),

        ("The 'Medusa head' colony appearance on nutrient agar is characteristic of:",
         ["Bacillus anthracis", "Clostridium perfringens", "Pseudomonas aeruginosa", "Erysipelothrix rhusiopathiae"],
         0, "Bacillus anthracis forms dull, opaque, grayish-white colonies with irregular curled borders resembling tangled locks of hair ('Medusa head' appearance) under low magnification."),

        ("The 'stormy fermentation' of litmus milk (rapid acid, gas production, and clot tearing) is pathognomonic for:",
         ["Clostridium perfringens", "Clostridium tetani", "Escherichia coli", "Lactobacillus acidophilus"],
         0, "Clostridium perfringens Type A ferments lactose vigorously in litmus milk, generating large amounts of gas that vigorously disrupt and shred the acid-curd clot ('stormy fermentation')."),

        ("The 'drumstick' or 'tennis racket' morphology of bacterial cells with terminal, spherical, bulging spores is characteristic of:",
         ["Clostridium tetani", "Clostridium botulinum", "Clostridium chauvoei", "Bacillus cereus"],
         0, "Clostridium tetani produces round, terminal spores with a diameter greater than the vegetative rod, imparting a distinctive 'drumstick' appearance."),

        ("Tetanospasmin, the potent neurotoxin produced by Clostridium tetani, acts by:",
         ["Preventing the release of inhibitory neurotransmitters (GABA and Glycine) at Renshaw cells", "Inhibiting acetylcholine release at neuromuscular junctions", "Hydrolyzing membrane sphingomyelin", "Inactivating elongation factor EF-2"],
         0, "Tetanospasmin is retrogradely transported along axons to spinal inhibitory interneurons, where it cleaves synaptobrevin (VAMP), blocking glycine and GABA exocytosis and causing spastic paralysis."),

        ("Botulinum neurotoxin causes flaccid paralysis by selectively blocking the release of which neurotransmitter?",
         ["Acetylcholine at the peripheral neuromuscular junction", "GABA in the spinal cord", "Dopamine in the basal ganglia", "Serotonin in the brainstem"],
         0, "Botulinum neurotoxin cleaves SNARE proteins (SNAP-25, syntaxin, synaptobrevin) at the motor nerve terminal, blocking acetylcholine release and producing descending flaccid paralysis."),

        ("The 'Nagler reaction' used for rapid presumptive identification of Clostridium perfringens demonstrates:",
         ["Alpha-toxin lecithinase (phospholipase C) activity inhibited by specific antitoxin on egg yolk agar", "Beta-toxin pore formation", "Epsilon-toxin enterotoxemia", "Theta-toxin oxygen-labile hemolysin"],
         0, "Nagler's reaction tests for Clostridium perfringens alpha toxin (lecithinase C); opacity is produced around colonies on egg-yolk agar, which is neutralized on the half of the plate spread with specific anti-alpha toxin."),

        # 11-20: Clostridia, Listeria, Erysipelothrix, Corynebacterium
        ("The 'pulpy kidney disease' (enterotoxemia) in rapidly growing, well-nourished sheep and lambs is caused by:",
         ["Clostridium perfringens Type D (Epsilon toxin)", "Clostridium perfringens Type B (Beta toxin)", "Clostridium perfringens Type C (Beta toxin)", "Clostridium perfringens Type A (Alpha toxin)"],
         0, "C. perfringens Type D produces the protoxin of epsilon toxin, which is cleaved and activated by trypsin in the intestinal lumen, increasing vascular permeability and causing soft autolytic pulpy kidneys."),

        ("The distinctive 'umbrella-shaped' or 'tumbling motility' seen in semi-solid agar at 22-25°C but NOT at 37°C is diagnostic of:",
         ["Listeria monocytogenes", "Campylobacter fetus", "Pseudomonas aeruginosa", "Salmonella enterica"],
         0, "Listeria monocytogenes produces peritrichous flagella and exhibits tumbling motility at room temperature (20-25°C), while flagellin synthesis is repressed at 37°C."),

        ("The 'CAMP test' (Christie, Atkins, Munch-Petersen) shows an arrowhead-shaped synergistic zone of beta-hemolysis between:",
         ["Streptococcus agalactiae and beta-lysin producing Staphylococcus aureus", "Streptococcus uberis and E. coli", "Listeria monocytogenes and Corynebacterium diphtheriae", "Bacillus cereus and Streptococcus dysgalactiae"],
         0, "Streptococcus agalactiae produces diffusible CAMP factor which synergistically acts with Staphylococcus aureus beta-lysin (sphingomyelinase C) to lyse sheep erythrocytes in an arrowhead pattern."),

        ("The 'test-tube brush' or 'lamp-brush' growth pattern in gelatin stab cultures incubated at 22°C is typical of:",
         ["Erysipelothrix rhusiopathiae", "Corynebacterium renale", "Listeria monocytogenes", "Trueperella pyogenes"],
         0, "Erysipelothrix rhusiopathiae produces lateral spikes radiating from the line of inoculation in gelatin stab culture, creating a classic 'test-tube brush' appearance without liquefaction."),

        ("In cattle, pyelonephritis characterized by ascending hemorrhagic purulent cystitis and ureteritis is primarily caused by:",
         ["Corynebacterium renale", "Streptococcus bovis", "Staphylococcus aureus", "Actinomyces bovis"],
         0, "The Corynebacterium renale group (C. renale, C. cystitidis, C. pilosum) uses pili to adhere to urinary urothelium and produces potent urease that hydrolyzes urea to ammonia, damaging mucosal surfaces."),

        ("The etiologic agent of 'Caseous Lymphadenitis' (CLA / pseudotuberculosis / onion-ring lymph nodes) in sheep and goats is:",
         ["Corynebacterium pseudotuberculosis", "Mycobacterium bovis", "Trueperella pyogenes", "Streptococcus equi"],
         0, "Corynebacterium pseudotuberculosis (producing phospholipase D and a lipid-rich cell wall) causes chronic suppurative and caseous necrotizing lymphadenitis with concentric laminar rings ('onion ring')."),

        ("The 'wooden tongue' (actinobacillosis) in cattle with granulomatous induration of the tongue is caused by which Gram-negative bacterium?",
         ["Actinobacillus lignieresii", "Actinomyces bovis", "Pasteurella multocida", "Fusobacterium necrophorum"],
         0, "Actinobacillus lignieresii is a Gram-negative bacillus causing wooden tongue, contrasting with Actinomyces bovis which is a Gram-positive filamentous branching bacterium causing lumpy jaw (osteomyelitis)."),

        ("The 'lumpy jaw' in cattle is a rarefying osteomyelitis of the mandible caused by:",
         ["Actinomyces bovis", "Actinobacillus lignieresii", "Nocardia asteroides", "Staphylococcus aureus"],
         0, "Actinomyces bovis is a Gram-positive, microaerophilic to anaerobic, filamentous, branching bacterium that invades mandibular bone marrow, causing suppurative osteomyelitis with sulfur granules."),

        ("The 'sulfur granules' discharged from sinus tracts in bovine lumpy jaw consist microscopically of:",
         ["Colonies of Actinomyces bovis surrounded by radiating, club-like Splendore-Hoeppli proteinaceous precipitates", "Precipitated elemental sulfur crystals", "Calcium oxalate crystals", "Coagulated fibrin only"],
         0, "Splendore-Hoeppli phenomenon represents radiating clubs formed by host immunoglobulins and major basic proteins surrounding central bacterial filaments in tissue granules."),

        ("Which selective and differential medium containing tellurite is routinely used for isolation of Corynebacterium species?",
         ["Hoyle’s tellurite agar / Tinsdale medium", "MacConkey agar", "Lowenstein-Jensen medium", "Brilliant Green agar"],
         0, "Corynebacterium species reduce potassium tellurite to tellurium, producing characteristic black or grayish-black colonies on Hoyle's or cystine-tellurite agar."),

        # 21-30: Enterobacteriaceae & Pasteurellaceae
        ("Which serological typing scheme is globally utilized for classifying Salmonella based on somatic (O) and flagellar (H) antigens?",
         ["Kauffmann-White-Le Minor scheme", "Lancefield scheme", "Bergey’s scheme", "Capsular typing scheme"],
         0, "The Kauffmann-White scheme differentiates Salmonella into serovars based on somatic (O) lipopolysaccharide antigens and phase-1 and phase-2 flagellar (H) antigens."),

        ("The causative agent of 'Pullorum disease' (bacillary white diarrhea) in neonatal chicks is:",
         ["Salmonella enterica subsp. enterica serovar Gallinarum-Pullorum (non-motile)", "Salmonella Typhimurium", "Salmonella Enteritidis", "Salmonella Choleraesuis"],
         0, "Salmonella Pullorum is a host-adapted, non-motile (flagella-lacking) Salmonella serovar causing high mortality, white pasted vent, and necrotic liver foci in young chicks."),

        ("Fowl Typhoid in adult poultry is caused by:",
         ["Salmonella Gallinarum", "Salmonella Pullorum", "Salmonella Anatum", "Pasteurella multocida"],
         0, "Salmonella Gallinarum causes Fowl Typhoid (bronze liver, enlarged spleen, high mortality in growers and adults). Like S. Pullorum, S. Gallinarum is non-motile."),

        ("The etiological agent of Fowl Cholera in chickens and turkeys is:",
         ["Pasteurella multocida", "Salmonella Gallinarum", "Avibacterium paragallinarum", "Gallibacterium anatis"],
         0, "Pasteurella multocida (primarily capsular serotype A) causes Fowl Cholera, marked by petechial hemorrhages, necrotic hepatitis, and swollen wattles."),

        ("The specific capsular serotypes of Pasteurella multocida responsible for Hemorrhagic Septicemia (HS) in cattle and buffaloes in Asia and Africa are:",
         ["B:2 (Asian serotype) and E:2 (African serotype) (Carter and Heddleston classification)", "A:1 and D:2", "A:3 and B:1", "C:1 and D:1"],
         0, "Carter capsular type B (somatic type 2) causes Asian HS; Carter type E (somatic type 2) causes African HS. Capsular typing is done by indirect hemagglutination and acriflavine flocculation."),

        ("The diagnostic 'bipolar staining' (safety-pin appearance) seen with Giemsa or Leishman stain in blood smears is typical of:",
         ["Pasteurella multocida and Yersinia pestis", "Brucella abortus", "Staphylococcus aureus", "Bacillus anthracis"],
         0, "Pasteurella multocida is a Gram-negative coccobacillus whose poles stain deeply while the central area remains pale ('safety-pin' appearance) when stained with polychromatic Romanowsky dyes."),

        ("The causative agent of 'Infectious Coryza' in poultry, characterized by acute seromucoid nasal discharge, facial edema, and conjunctivitis, is:",
         ["Avibacterium paragallinarum (requires V-factor / NAD)", "Gallibacterium anatis", "Ornithobacterium rhinotracheale", "Mycoplasma gallisepticum"],
         0, "Avibacterium paragallinarum (formerly Haemophilus paragallinarum) is an NAD-dependent (V-factor) bacterium causing acute upper respiratory tract infection in chickens."),

        ("The satellite phenomenon around Staphylococcus aureus streak on blood agar occurs because S. aureus provides:",
         ["V factor (NAD / Nicotinamide Adenine Dinucleotide)", "X factor (Hemin)", "Coagulase", "Alpha hemolysin"],
         0, "Fastidious organisms like Avibacterium or Haemophilus require V factor (NAD) secreted by S. aureus; hence colonies grow larger in close proximity to the feeder S. aureus streak."),

        ("The 'Shiga-toxin producing Escherichia coli' (STEC / EHEC) serotype classically associated with Hemolytic Uremic Syndrome (HUS) and hemorrhagic enteritis is:",
         ["E. coli O157:H7", "E. coli K99 (F5)", "E. coli K88 (F4)", "E. coli 987P"],
         0, "E. coli O157:H7 produces Stx-1 and Stx-2 (verotoxins) that inhibit protein synthesis in vascular endothelial cells, triggering thrombotic microangiopathy and HUS."),

        ("The principal fimbrial (pilus) adhesin in Enterotoxigenic E. coli (ETEC) causing neonatal calf scours is:",
         ["K99 (F5)", "K88 (F4)", "987P (F6)", "F41"],
         0, "ETEC strains in calves primarily utilize K99 (F5) fimbriae to adhere to small intestinal enterocytes before secreting heat-stable enterotoxin (STa)."),

        # 31-40: Brucella, Mycobacteria, Spirochaetes
        ("The 'Rose Bengal Plate Test' (RBPT) used as a rapid screening herd test for Brucellosis utilizes an antigen buffered at which pH?",
         ["Acidic pH (3.65)", "Neutral pH (7.0)", "Alkaline pH (8.6)", "Acidic pH (1.5)"],
         0, "RBPT antigen is buffered at pH 3.65 with lactic acid; this low pH inhibits non-specific agglutinins (especially bovine IgM agglutination) while permitting specific IgG1 agglutination."),

        ("The 'Milk Ring Test' (MRT) for herd screening of bovine brucellosis detects Brucella antibodies in milk through agglutination of hematoxylin-stained antigen with which milk component?",
         ["Fat globules (cream layer) coated with agglutinating IgA/IgM antibodies", "Casein precipitate", "Lactalbumin fraction", "Somatic epithelial cells"],
         0, "Brucella abortus hematoxylin-stained antigen binds specific agglutinins adsorbed to milk fat globule surfaces; as fat globules rise, they form a distinct blue cream ring at the top of the milk column."),

        ("The 'Standard Tube Agglutination Test' (STAT) for bovine brucellosis is expressed in International Units, and a diagnostic titer indicative of infection in non-vaccinated cattle is typically:",
         [">= 100 IU/ml (or 1:50 to 1:100 dilution)", ">= 10 IU/ml", ">= 1 IU/ml", ">= 500 IU/ml"],
         0, "Under OIE guidelines, a serum titer of 100 International Units (IU) per ml or higher is considered positive in non-vaccinated cattle (or 50 IU/ml in certain eradication programs)."),

        ("Brucella abortus has an intense tissue tropism for the gravid ruminant placenta and fetal fluids primarily because of high concentrations of which growth-stimulatory polyol?",
         ["Erythritol", "Mannitol", "Sorbitol", "Xylitol"],
         0, "Erythritol, a 4-carbon sugar alcohol produced in the bovine chorion and placenta, selectively stimulates the growth of Brucella abortus, B. melitensis, and B. suis, precipitating necrotizing placentitis and abortion."),

        ("Which staining procedure is used to identify Mycobacterium tuberculosis and Mycobacterium bovis based on their cell wall mycolic acid content?",
         ["Ziehl-Neelsen (Acid-Fast) stain", "Grams stain", "Albert stain", "Fontana stain"],
         0, "The thick, waxy, lipid-rich cell wall of Mycobacteria containing 60% mycolic acids retains carbol fuchsin against decolorization by acid-alcohol (3% HCl in 95% ethanol), appearing as acid-fast red rods."),

        ("The 'Single Intradermal Comparative Cervical Tuberculin' (SICCT) test in cattle differentiates M. bovis infection from sensitization to environmental mycobacteria by comparing skin swelling to:",
         ["Bovine PPD and Avian PPD injected intradermally at two sites on the neck", "Bovine PPD and Human PPD", "Brucellin and Tuberculin", "Mallein and Johnin"],
         0, "SICCT compares the delayed-type hypersensitivity (DTH) reaction 72 hours post-injection of Bovine PPD and Avian PPD; an increase in skin thickness to Bovine PPD > 4 mm greater than Avian PPD indicates bovine TB."),

        ("Mycobacterium avium subsp. paratuberculosis (MAP), the causative agent of Johne's disease, strictly requires which iron-chelating growth factor in culture media?",
         ["Mycobactin (e.g. Mycobactin J)", "Hemin", "Coenzyme A", "Biotin"],
         0, "MAP cannot synthesize the iron-transporting siderophore mycobactin in vitro; Herrold's egg yolk medium must be supplemented with Mycobactin J for primary isolation."),

        ("The 'silver impregnation technique' (Fontana stain or Levaditi stain) is standardly used for demonstrating:",
         ["Spirochaetes (Leptospira and Treponema)", "Capsules of Klebsiella", "Spores of Clostridium", "Flagella of Proteus"],
         0, "Spirochaetes have a very slender diameter (0.1 to 0.2 µm) below the resolving power of ordinary brightfield microscopy unless silver salts are deposited on their surfaces to thicken their outline."),

        ("The 'Microscopic Agglutination Test' (MAT) is the definitive gold standard serological test for the diagnosis of:",
         ["Leptospirosis", "Brucellosis", "Glanders", "Listeriosis"],
         0, "MAT utilizes live Leptospira serovars incubated with serial dilutions of patient serum and examined by darkfield microscopy for agglutination and lysis."),

        ("The causative agent of 'Swine Dysentery', characterized by mucohemorrhagic colitis and typhlitis in feeder pigs, is:",
         ["Brachyspira hyodysenteriae", "Campylobacter jejuni", "Salmonella Choleraesuis", "Lawsonia intracellularis"],
         0, "Brachyspira (Treponema) hyodysenteriae is an anaerobic spirochaete that produces beta-hemolysin, disrupting colonic epithelium and goblet cells to produce mucohemorrhagic diarrhea."),

        # 41-50: Other Bacteria (Glanders, Mycoplasma, Staph, Strep, Pseudomonas)
        ("The 'Straus reaction' (acute purulent periorchitis and testicular enlargement in inoculated male guinea pigs) is classically produced by:",
         ["Burkholderia mallei and Brucella ovis", "Bacillus anthracis", "Corynebacterium diphtheriae", "Clostridium chauvoei"],
         0, "Intraperitoneal injection of male guinea pigs with Burkholderia mallei (glanders) produces acute purulent tunica vaginalis inflammation and scrotal swelling (Straus reaction)."),

        ("The diagnostic 'Mallein test' for diagnosing latent and chronic Glanders in equines is routinely performed via which route?",
         ["Intrapalpebral (injection into lower eyelid dermis) or eye drop ophthalmic route", "Intramuscular injection", "Subcutaneous injection into neck", "Scarification on flank"],
         0, "The intrapalpebral mallein test involves intradermal injection of mallein into the lower eyelid; marked swelling, edema, and purulent conjunctivitis at 24-48 hours indicates infection."),

        ("The 'fried egg' colony appearance on specialized agar (PPLO agar supplemented with serum and yeast extract) is characteristic of:",
         ["Mycoplasma species", "Chlamydia psittaci", "Rickettsia prowazekii", "Coxiella burnetii"],
         0, "Mycoplasma lacks a peptidoglycan cell wall; its central core penetrates into the agar medium while peripheral growth spreads outward on the surface, mimicking a fried egg."),

        ("The causative agent of 'Contagious Bovine Pleuropneumonia' (CBPP), producing marbling of lungs and sequestrum formation, is:",
         ["Mycoplasma mycoides subsp. mycoides (small colony type)", "Mycoplasma bovis", "Pasteurella multocida", "Mannheimia haemolytica"],
         0, "CBPP is caused by Mycoplasma mycoides subsp. mycoides (SC type), causing unilateral fibrinous pleuropneumonia with thick interlobular septa ('marbled lung')."),

        ("The causative agent of 'Contagious Caprine Pleuropneumonia' (CCPP) in goats is:",
         ["Mycoplasma capricolum subsp. capripneumoniae", "Mycoplasma agalactiae", "Mycoplasma mycoides subsp. capri", "Mycoplasma bovis"],
         0, "CCPP is strictly caused by Mycoplasma capricolum subsp. capripneumoniae (formerly F38 biotype), marked by severe fibrinous pleuropneumonia and straw-colored pleural effusion in goats."),

        ("The 'blue-green pigment' pyocyanin and the fluorescent yellow-green pigment pyoverdine are produced by:",
         ["Pseudomonas aeruginosa", "Serratia marcescens", "Staphylococcus aureus", "Burkholderia pseudomallei"],
         0, "Pseudomonas aeruginosa produces pyocyanin (blue phenazine pigment) and pyoverdine (fluorescent siderophore), giving wounds and culture plates a characteristic sweet grape-like odor and bluish-green sheen."),

        ("The 'golden yellow' carotenoid pigment staphyloxanthin and coagulase production are major virulence markers of:",
         ["Staphylococcus aureus", "Staphylococcus epidermidis", "Staphylococcus hyicus", "Streptococcus agalactiae"],
         0, "Staphylococcus aureus produces staphyloxanthin (antioxidant carotenoid protecting against host reactive oxygen species) and coagulase which clots rabbit/human plasma."),

        ("The causative agent of 'Exudative Epidermitis' (Greasy Pig Disease) in suckling and weaned pigs is:",
         ["Staphylococcus hyicus", "Staphylococcus aureus", "Streptococcus suis", "Erysipelothrix rhusiopathiae"],
         0, "Staphylococcus hyicus secretes exfoliative toxins (exfoliatin) that cleave desmoglein-1 in stratum granulosum, resulting in widespread non-pruritic exfoliative dermatitis with greasy sebum exudate."),

        ("The Lancefield grouping of Streptococci is based on antigenic differences in their:",
         ["Cell wall C-carbohydrate (polysaccharide)", "M-protein", "Capsular polysaccharide", "Streptolysin O"],
         0, "Rebecca Lancefield grouped beta-hemolytic streptococci (Groups A through V) according to the serological specificity of their cell-wall group-specific C-carbohydrate extract."),

        ("The causative agent of 'Strangles' in horses, characterized by acute purulent pharyngitis and abscessation of mandibular and retropharyngeal lymph nodes, is:",
         ["Streptococcus equi subsp. equi (Lancefield Group C)", "Streptococcus equi subsp. zooepidemicus", "Rhodococcus equi", "Corynebacterium pseudotuberculosis"],
         0, "Streptococcus equi subsp. equi is a highly contagious Lancefield group C beta-hemolytic Streptococcus; S. zooepidemicus is a commensal opportunist fermenting lactose and sorbitol (which equi does not)."),

        # 51-65: Virology - FMD, Pox, Rhabdo, Parvo, Pestivirus, Morbilli
        ("How many distinct serotypes of Foot and Mouth Disease Virus (FMDV, Aphthovirus) exist worldwide?",
         ["7 serotypes (O, A, C, SAT-1, SAT-2, SAT-3, and Asia-1)", "5 serotypes (O, A, C, Asia-1, Asia-2)", "3 serotypes (O, A, C)", "4 serotypes (O, A, C, SAT-1)"],
         0, "FMDV (Picornaviridae) exists as 7 immunologically distinct serotypes: O, A, C, Southern African Territories (SAT-1, SAT-2, SAT-3), and Asia-1, with no cross-protection between serotypes."),

        ("Which serotype of Foot and Mouth Disease Virus (FMDV) is most prevalent and causes the vast majority of outbreaks in India?",
         ["Serotype O (Ind-2001 / PanAsia lineage)", "Serotype Asia-1", "Serotype A", "Serotype C"],
         0, "In India, Serotype O accounts for over 80-85% of all confirmed FMD outbreaks, followed by Asia-1 and A; Serotype C has not been detected in India since 1995."),

        ("Foot and Mouth Disease Virus (FMDV) is rapidly inactivated below which pH threshold?",
         ["Below pH 6.0 (acid-labile)", "Below pH 2.0", "Below pH 8.0", "It is acid-stable down to pH 1.0"],
         0, "Unlike Enteroviruses, Aphthoviruses (FMDV) are remarkably acid-labile and are promptly inactivated below pH 6.0 (and above pH 9.0), which is why post-mortem lactic acid buildup in rigor mortis inactivates the virus in skeletal muscle."),

        ("The rabies virus genome consists of which type of nucleic acid?",
         ["Negative-sense single-stranded unsegmented RNA (-ssRNA)", "Positive-sense single-stranded RNA (+ssRNA)", "Double-stranded RNA (dsRNA)", "Single-stranded DNA (ssDNA)"],
         0, "Rabies virus (Lyssavirus, Rhabdoviridae) contains a bullet-shaped enveloped negative-sense single-stranded RNA genome encoding N, P, M, G, and L proteins."),

        ("Which rabies viral structural protein binds to the nicotinic acetylcholine receptor (nAChR) and NCAM on host neuronal synapses, and is the sole target of neutralizing antibodies?",
         ["Glycoprotein (G protein)", "Nucleoprotein (N protein)", "Matrix protein (M protein)", "Phosphoprotein (P protein)"],
         0, "The surface trimeric spike Glycoprotein (G) mediates attachment to host neural receptors and membrane fusion, and induces virus-neutralizing antibodies essential for protective immunity."),

        ("The gold standard test recommended by WHO and WOAH (OIE) for post-mortem confirmation of Rabies in brain tissue is:",
         ["Direct Fluorescent Antibody Test (dFAT)", "Seller's stain for Negri bodies", "Mouse Inoculation Test (MIT)", "Enzyme-linked immunosorbent assay (ELISA)"],
         0, "Direct FAT on fresh impression smears of Ammon's horn, cerebellum, and medulla using fluorescein isothiocyanate (FITC)-conjugated anti-rabies globulin is the international diagnostic gold standard."),

        ("The 'Seller’s stain' for demonstration of Negri bodies in rabies impression smears contains:",
         ["Basic fuchsin and Methylene blue in absolute methyl alcohol", "Crystal violet and Safranin", "Carbol fuchsin and Malachite green", "Hematoxylin and Eosin"],
         0, "Seller's stain combines basic fuchsin and methylene blue in acetone-free absolute methanol, fixing and staining simultaneously to yield magenta-pink Negri bodies with dark-blue basophilic inner granules in blue cytoplasm."),

        ("Peste des Petits Ruminants (PPR) virus belongs to which genus in the family Paramyxoviridae?",
         ["Morbillivirus", "Avulavirus", "Respirovirus", "Henipavirus"],
         0, "PPR virus is a Morbillivirus closely related to Rinderpest virus, Canine Distemper virus, and Measles virus. It causes stomatitis-pneumoenteritis complex in sheep and goats."),

        ("The live attenuated homologous vaccine strain universally used for control and eradication of PPR in India is:",
         ["Sungri 96 (PPRV / Sungri / 1996)", "Nigeria 75/1", "Mukteswar strain", "Kabete 'O' strain"],
         0, "The indigenously developed Sungri 96 vaccine (developed by ICAR-IVRI) provides lifelong immunity against all 4 lineages of PPRV in small ruminants across India."),

        ("Canine Parvovirus 2 (CPV-2) targets rapidly dividing cells with high mitotic index, primarily destroying:",
         ["Intestinal crypt enterocytes and bone marrow lymphoid progenitor cells", "Renal glomerular podocytes", "Hepatic biliary epithelium", "Respiratory ciliated columnar cells"],
         0, "CPV-2 requires host cell DNA polymerases in S-phase for replication, selectively destroying the regenerative intestinal crypts of Lieberkühn (causing villous collapse) and myeloid marrow precursors (causing severe leukopenia)."),

        ("The original Canine Parvovirus-2 (CPV-2) emerged in 1978 as a host-range variant of which feline virus?",
         ["Feline Panleukopenia Virus (FPV)", "Feline Infectious Peritonitis Virus (FIPV)", "Feline Calicivirus (FCV)", "Feline Leukemia Virus (FeLV)"],
         0, "CPV-2 evolved from FPV via 5-6 amino acid mutations in the VP2 capsid gene, which allowed the virus to bind canine transferrin receptor-1 (TfR)."),

        ("The primary structural capsid protein of Canine Parvovirus that determines host range, receptor binding, and antigenicity (including 2a, 2b, 2c variants) is:",
         ["VP2", "VP1", "NS1", "NS2"],
         0, "VP2 comprises 90% of the non-enveloped icosahedral capsid of Parvoviruses; subtle amino acid substitutions at residue 426 distinguish variants 2a (Asn), 2b (Asp), and 2c (Glu)."),

        ("Which virus family is characterized by a reverse transcriptase enzyme converting an RNA genome into proviral DNA that integrates into host chromosomes?",
         ["Retroviridae", "Reoviridae", "Rhabdoviridae", "Coronaviridae"],
         0, "Retroviruses (e.g. Equine Infectious Anemia, Bovine Leukemia Virus, FeLV, Jaagsiekte) use RNA-dependent DNA polymerase (reverse transcriptase) to synthesize double-stranded DNA from their diploid RNA genome."),

        ("The 'Coggins test' is the official regulatory agar-gel immunodiffusion (AGID) test for diagnosing:",
         ["Equine Infectious Anemia (EIA / Swamp Fever)", "African Horse Sickness", "Equine Viral Arteritis", "Glanders"],
         0, "Developed by Dr. Leroy Coggins in 1970, the Coggins test detects serum antibodies against the major internal p26 core protein of Equine Infectious Anemia lentivirus."),

        ("Infectious Canine Hepatitis (ICH) in dogs and Rubarth's disease in foxes is caused by:",
         ["Canine Adenovirus type 1 (CAV-1)", "Canine Adenovirus type 2 (CAV-2)", "Canine Herpesvirus 1", "Canine Coronavirus"],
         0, "CAV-1 causes hepatitis and endothelial necrosis with corneal edema ('blue eye'), whereas CAV-2 is associated with infectious tracheobronchitis (kennel cough) and is used in vaccines to avoid immune-complex uveitis."),

        # 66-80: Avian Virology, Arboviruses & Swine Viruses
        ("The Newcastle Disease Virus (NDV) belongs to which family and genus?",
         ["Paramyxoviridae, Orthoavulavirus (Avian orthoavulavirus 1)", "Picornaviridae, Avihepatovirus", "Orthomyxoviridae, Influenzavirus A", "Birnaviridae, Avibirnavirus"],
         0, "NDV (Avian Paramyxovirus-1 / APMV-1) is classified under family Paramyxoviridae, genus Orthoavulavirus."),

        ("The virulence of Newcastle Disease Virus strains (velogenic vs lentogenic) is primarily determined by the amino acid sequence at the cleavage site of which surface glycoprotein?",
         ["Fusion (F) protein", "Hemagglutinin-Neuraminidase (HN) protein", "Matrix (M) protein", "Nucleocapsid (NP) protein"],
         0, "Virulent (velogenic/mesogenic) NDV strains have multiple basic amino acids (Arg/Lys) at the F0 cleavage site (cleaved by ubiquitous intracellular furin), allowing systemic multi-organ dissemination."),

        ("The 'Intracerebral Pathogenicity Index' (ICPI) in day-old chicks for velogenic Newcastle Disease Virus strains is typically close to:",
         ["> 1.5 to 2.0 (maximum 2.0)", "0.0 to 0.5", "0.5 to 1.0", "Negative"],
         0, "ICPI scores range from 0.0 (avirulent/lentogenic, e.g. Hitchner B1 / LaSota) to 2.0 (most virulent velogenic strains, e.g. Texas GB, Hertfordshire). An ICPI >= 0.7 defines notifiable NDV."),

        ("Infectious Bursal Disease (IBD / Gumboro disease) virus belongs to which family and possesses which genome structure?",
         ["Birnaviridae, bisegmented double-stranded RNA (dsRNA)", "Coronaviridae, positive-sense ssRNA", "Parvoviridae, ssDNA", "Reoviridae, 10-segmented dsRNA"],
         0, "IBDV is a non-enveloped Birnavirus with a bisegmented double-stranded RNA genome (Segment A encodes VP2-VP4-VP3 and VP5; Segment B encodes VP1 RNA polymerase)."),

        ("The major protective antigen and target of neutralizing antibodies in Infectious Bursal Disease Virus (IBDV) is:",
         ["VP2 capsid protein (hypervariable loop domain)", "VP1 viral polymerase", "VP3 inner capsid protein", "VP4 viral protease"],
         0, "VP2 forms the outer surface trimeric spikes of the icosahedral capsid; mutations within its hypervariable region (aa 206 to 350) generate very virulent (vvIBDV) antigenic variants."),

        ("Marek’s Disease in poultry is caused by:",
         ["Gallid alphaherpesvirus 2 (MDV-1)", "Gallid alphaherpesvirus 1 (Infectious Laryngotracheitis)", "Avian leukosis virus", "Gallid alphaherpesvirus 3"],
         0, "Marek's Disease is a lymphoproliferative, oncogenic alphaherpesvirus (MDV-1) causing T-cell lymphoma, sciatic nerve enlargement, 'range paralysis', and grey eye in chickens."),

        ("The vaccine strain 'HVT' widely used against Marek's Disease is derived from:",
         ["Herpesvirus of Turkeys (Meleagrid alphaherpesvirus 1 / MDV-3)", "Attenuated MDV-1 CVI988/Rispens", "Quail herpesvirus", "Pigeon herpesvirus"],
         0, "HVT (serotype 3) is naturally non-pathogenic in chickens and induces solid cross-protective immunity against oncogenic serotype 1 MDV strains."),

        ("Classical Swine Fever (Hog Cholera) virus belongs to the genus Pestivirus in which viral family?",
         ["Flaviviridae", "Arteriviridae", "Asfarviridae", "Coronaviridae"],
         0, "CSFV is a lipid-enveloped, positive-sense single-stranded RNA virus classified in the genus Pestivirus along with Bovine Viral Diarrhea Virus (BVDV-1, BVDV-2) and Border Disease Virus (BDV)."),

        ("African Swine Fever Virus (ASFV) is unique among all animal DNA viruses because:",
         ["It is the only known arbovirus with a double-stranded DNA genome (family Asfarviridae)", "It has a circular single-stranded DNA genome", "It replicates exclusively in the nucleus", "It lacks a lipid envelope"],
         0, "ASFV is a large, enveloped icosahedral double-stranded DNA virus (family Asfarviridae) and is the only known DNA virus transmitted biologically by arthropod vectors (soft ticks of genus Ornithodoros)."),

        ("Bluetongue virus in sheep and cattle belongs to the genus Orbivirus (family Reoviridae) and is transmitted biologically by:",
         ["Culicoides biting midges", "Aedes mosquitoes", "Ixodes ticks", "Stomoxys calcitrans (stable flies)"],
         0, "Bluetongue virus (containing 10 dsRNA segments) is transmitted by biting midges of the genus Culicoides (e.g. C. oxystoma, C. imicola), producing cyanosis of the tongue, coronitis, and pulmonary edema."),

        # 81-95: Immunology & Serology
        ("The predominant immunoglobulin isotype in normal adult bovine serum is:",
         ["IgG1", "IgG2", "IgM", "IgA"],
         0, "In cattle (unlike humans and rodents where IgG2 or IgG1 dominate differently), IgG1 is the major immunoglobulin subclass in both serum (approx. 50-60% of total IgG) and colostrum/milk."),

        ("In ruminants, the selective transfer of antibodies from maternal circulation into colostrum across mammary alveolar epithelial cells is mediated specifically by:",
         ["IgG1 via neonatal Fc receptor (FcRn)", "IgA via polymeric Ig receptor (pIgR)", "IgM non-specifically", "IgE via Fc-epsilon receptor"],
         0, "Unlike humans where colostrum is rich in secretory IgA, ruminant colostrum is dominated by IgG1 (over 80-90% of colostral Ig), actively translocated from maternal serum via FcRn receptors on mammary epithelium."),

        ("Secretory component (SC) of Secretory IgA (sIgA) is derived from:",
         ["Polymeric immunoglobulin receptor (pIgR) on mucosal epithelial cells during transcytosis", "Plasma cells synthesizing the heavy chain", "J-chain polypeptide", "Dendritic cells"],
         0, "Dimeric IgA binds pIgR on the basolateral surface of enterocytes; after vesicular endocytosis, the receptor is cleaved, leaving the secretory component bound to protect sIgA against luminal proteases."),

        ("Which immunoglobulin isotype exists as a pentamer linked by a J (joining) chain, possesses 10 antigen-binding sites, and is the most efficient at activating the classical complement pathway?",
         ["IgM", "IgG", "IgA", "IgE"],
         0, "Pentameric IgM has high avidity and multiple Fc domains; binding of a single IgM molecule to an antigen surface can expose C1q binding sites and trigger the classical complement cascade."),

        ("The 'C1q' subcomponent of the classical complement pathway binds directly to which domain of antigen-bound antibodies?",
         ["CH2 domain of IgG and CH3 domain of IgM", "Fab fragment", "Hypervariable CDR3 loops", "Light chain constant domain"],
         0, "C1q binds to the CH2 domain of IgG (especially IgG1 and IgG3) or the CH3 domain of IgM following antigen binding, triggering conformational activation of C1r and C1s esterases."),

        ("The 'Membrane Attack Complex' (MAC) that forms lytic transmembrane channels in target microbial membranes is composed of:",
         ["C5b, C6, C7, C8, and multiple C9 molecules (C5b-9 complex)", "C3b, Bb, and properdin", "C4b, C2a, and C3b", "C1q, C1r, and C1s"],
         0, "C5 convertase cleaves C5 into C5a and C5b; C5b recruits C6 and C7 to insert into lipid bilayers, C8 stabilizes it, and 10-16 molecules of C9 polymerize to form a 10 nm hydrophilic pore (MAC)."),

        ("Major Histocompatibility Complex (MHC) Class I molecules present endogenous peptide antigens to:",
         ["CD8+ Cytotoxic T lymphocytes (CTLs)", "CD4+ T helper lymphocytes", "B lymphocytes", "Natural Killer cells only"],
         0, "MHC Class I molecules (alpha chain + beta-2-microglobulin) present intracellular peptides (e.g. viral antigens) to CD8+ cytotoxic T cells, whereas MHC Class II molecules present exogenous peptides to CD4+ Th cells."),

        ("Type I Hypersensitivity (immediate / anaphylactic) is mediated primarily by:",
         ["IgE cross-linking on mast cells and basophils triggering degranulation", "Complement-fixing IgG/IgM antibodies", "Deposition of antigen-antibody immune complexes", "Sensitized CD4+ Th1 cells and macrophages"],
         0, "Allergen-induced cross-linking of specific IgE bound to high-affinity Fc-epsilon-RI on mast cells and basophils triggers immediate exocytosis of histamine, heparin, leukotrienes, and prostaglandins."),

        ("The 'Arthus reaction' is a localized cutaneous manifestation of which type of hypersensitivity?",
         ["Type III Hypersensitivity (Immune Complex-mediated)", "Type I Hypersensitivity (Anaphylactic)", "Type II Hypersensitivity (Cytotoxic)", "Type IV Hypersensitivity (Delayed-type)"],
         0, "The Arthus reaction occurs when soluble antigen is injected into an animal with high levels of circulating IgG; local immune complex deposition activates complement, attracting neutrophils and producing necrotizing vasculitis."),

        ("The Tuberculin skin test is a classic clinical example of:",
         ["Type IV Hypersensitivity (Delayed-Type Cell-Mediated Hypersensitivity / DTH)", "Type I Hypersensitivity", "Type II Hypersensitivity", "Type III Hypersensitivity"],
         0, "Tuberculin PPD triggers memory CD4+ Th1 cells to release IFN-gamma, recruiting and activating macrophages over 48 to 72 hours, resulting in induration and swelling."),

        ("In 'Hybridoma technology' for monoclonal antibody production (Kohler and Milstein, 1975), which selection medium is used to eliminate unfused myeloma cells?",
         ["HAT medium (Hypoxanthine, Aminopterin, Thymidine)", "MacConkey medium", "RPMI-1640 without serum", "Eosin Methylene Blue medium"],
         0, "Aminopterin blocks the de novo nucleotide synthesis pathway; myeloma cells lacking HGPRT cannot use the salvage pathway and die, whereas hybridomas survive using HGPRT from splenic B-cells."),

        ("Which adjuvant component in Freund's Complete Adjuvant (FCA) triggers intense cell-mediated immunity via NOD2 and Toll-like receptors?",
         ["Heat-killed dried Mycobacterium tuberculosis / M. butyricum cells in mineral oil", "Aluminium hydroxide gel", "Saponin Quil-A", "Lipopolysaccharide alone"],
         0, "Freund's Incomplete Adjuvant (FIA) is water-in-mineral-oil; Complete Adjuvant (FCA) contains killed Mycobacteria whose muramyl dipeptide (MDP) activates NOD2, driving potent Th1 responses."),

        # 96-100: Veterinary Mycology
        ("The 'cigarette ash' or 'chalky powdery' colony on Sabouraud Dextrose Agar with macroconidia shaped like canoes or cigar/pencils is typical of:",
         ["Trichophyton mentagrophytes", "Microsporum canis", "Aspergillus fumigatus", "Candida albicans"],
         0, "Trichophyton mentagrophytes produces powdery/granular colonies with abundant spherical microconidia and sparse cigar-shaped, thin-walled macroconidia, causing ringworm in rodents and horses."),

        ("The dermatophyte of dogs and cats that exhibits bright apple-green fluorescence under Wood's lamp (ultraviolet light at 365 nm) is:",
         ["Microsporum canis (due to pteridine pigment in hair shafts)", "Trichophyton verrucosum", "Trichophyton equinum", "Microsporum gypseum"],
         0, "About 50% of Microsporum canis strains produce pteridine metabolites in infected hair shafts that emit characteristic bright yellow-green fluorescence under Wood's lamp."),

        ("The 'germ tube test' in fetal bovine serum incubated at 37°C for 2-3 hours is a rapid diagnostic test for:",
         ["Candida albicans", "Cryptococcus neoformans", "Rhizopus oryzae", "Blastomyces dermatitidis"],
         0, "Candida albicans produces true germ tubes (slender tube-like hyphal outgrowths without constrictions at the mother blastoconidium junction) within 2-3 hours in serum."),

        ("The thick mucopolysaccharide capsule of Cryptococcus neoformans is clearly demonstrated microscopically by negative staining with:",
         ["India ink (Nigrosin)", "Gram stain", "Acid-fast stain", "Giemsa stain"],
         0, "India ink particles cannot penetrate the glucuronoxylomannan (GXM) capsule of Cryptococcus neoformans, highlighting the yeast as a clear translucent halo against a dark carbon background."),

        ("Aflatoxins, potent hepatotoxic and carcinogenic mycotoxins commonly contaminating groundnuts and maize, are produced by:",
         ["Aspergillus flavus and Aspergillus parasiticus", "Fusarium moniliforme", "Penicillium roqueforti", "Claviceps purpurea"],
         0, "Aspergillus flavus and A. parasiticus produce Aflatoxins B1, B2, G1, and G2; Aflatoxin B1 is converted by hepatic CYP450 to exo-8,9-epoxide, binding DNA and causing hepatocellular carcinoma.")
    ]

    more_vmc_pyqs = [
        # Fill remaining slots up to 100
        ("The 'ring test' or Ring precipitation test of Ascoli for Anthrax is based on which immunological reaction?",
         ["Precipitation (soluble antigen reacting with hyperimmune serum)", "Direct agglutination", "Hemagglutination inhibition", "Complement fixation"],
         0, "Ascoli test is a classic precipitation reaction in a capillary tube where soluble thermostable polysaccharide antigen forms a visible white precipitin ring at the interface with specific antiserum."),

        ("Which genus of bacteria is characteristically cell wall-less, highly pleomorphic, and completely resistant to beta-lactam antibiotics like penicillin?",
         ["Mycoplasma", "Mycobacterium", "Brucella", "Listeria"],
         0, "Mycoplasma species lack a peptidoglycan cell wall (surrounded only by a triple-layered sterol-containing cell membrane), making them innately resistant to all beta-lactams and vancomycin."),

        ("The primary viral agent of 'Equine Influenza' belongs to which type of Influenza virus?",
         ["Influenzavirus A (H3N8 and historically H7N7)", "Influenzavirus B", "Influenzavirus C", "Influenzavirus D"],
         0, "Equine influenza is caused by two subtypes of Influenza A virus: H7N7 (equi-1, now considered extinct) and H3N8 (equi-2, Florida clades 1 and 2)."),

        ("The 'interferon' most potent in activating macrophages and promoting MHC Class II expression is:",
         ["Interferon-gamma (IFN-gamma, Type II interferon)", "Interferon-alpha", "Interferon-beta", "Interferon-lambda"],
         0, "IFN-gamma (secreted by Th1 and NK cells) is the quintessential macrophage-activating factor, upregulating phagocytosis, oxidative burst, and MHC-II expression."),

        ("The specific receptor for Foot and Mouth Disease Virus on host epithelial cells is:",
         ["Integrins (specifically alpha-v beta-6 integrin)", "Sialic acid", "CD46", "Transferrin receptor"],
         0, "FMDV utilizes its conserved Arg-Gly-Asp (RGD) tripeptide motif located on the flexible G-H loop of capsid protein VP1 to bind alpha-v integrins (predominantly alpha-v beta-6)."),

        ("The 'swarming phenomenon' (concentric waves of spreading growth across non-inhibitory agar media) is characteristic of:",
         ["Proteus mirabilis and Proteus vulgaris", "Pseudomonas aeruginosa", "Klebsiella pneumoniae", "Salmonella enterica"],
         0, "Proteus species undergo cyclical differentiation from short swimmer cells into elongated, hyperflagellated swarmer cells, migrating synchronously to form concentric terraced rings."),

        ("Bovine Viral Diarrhea Virus (BVDV) produces which neurological congenital anomaly in calves infected transplacentally between days 100 to 150 of gestation?",
         ["Cerebellar hypoplasia", "Hydranencephaly", "Spina bifida", "Anencephaly"],
         0, "Transplacental infection of the bovine fetus with BVDV during mid-gestation selectively attacks the external germinal layer of the cerebellum, resulting in cerebellar hypoplasia, ataxia, and tremors."),

        ("The 'Quellung reaction' (capsular swelling phenomenon observed under brightfield or phase contrast microscopy) is produced by:",
         ["Antigenic cross-linking of bacterial capsule by homologous anticapsular antibodies increasing its refractive index", "Cell wall lysis by lysozyme", "Endospore germination", "Flagellar agglutination"],
         0, "In the Neufeld Quellung reaction, mixing encapsulated bacteria with specific polyvalent or monovalent antiserum causes the capsule to appear sharply outlined and swollen due to changed refractive index.")
    ]

    pyqs.extend(more_vmc_pyqs)

    final_list = []
    for idx, item in enumerate(pyqs[:100]):
        final_list.append({
            "id": f"pyq_vmc_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "2nd_year",
            "subjectId": "vmc",
            "topic": "Veterinary Microbiology (ICAR PG PYQ)",
            "questionText": item[0],
            "options": item[1],
            "correctOptionIndex": item[2],
            "explanation": item[3],
            "difficulty": "Hard",
            "tags": ["ICAR PG PYQ", "Microbiology", "High-Yield PYQ"],
            "createdAt": 1774000100000 + idx
        })
    return final_list

if __name__ == "__main__":
    qs = get_vmc_pyqs()
    print(f"Loaded {len(qs)} Veterinary Microbiology PYQ questions.")
