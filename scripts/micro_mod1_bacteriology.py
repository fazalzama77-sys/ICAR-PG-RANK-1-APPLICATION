# scripts/micro_mod1_bacteriology.py
# Module 1: Systematic Bacteriology (90 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module1_questions():
    qs = [
        # 1-10: Bacillus anthracis & Clostridium species
        ("In Bacillus anthracis, the antiphagocytic polypeptide capsule is encoded on plasmid pXO2 and is uniquely composed of:",
         ["Poly-D-glutamic acid", "Hyaluronic acid", "Dextran polymers", "Lipopolysaccharide"],
         0, "Unlike almost all other bacterial capsules which are polysaccharides, the capsule of B. anthracis is a homopolymer of poly-D-glutamic acid encoded by the capBCADE operon on plasmid pXO2, conferring complete resistance to phagocytosis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The tripartite exotoxin of Bacillus anthracis is encoded on plasmid pXO1 and consists of which three distinct synergistic proteins?",
         ["Protective Antigen (PA), Lethal Factor (LF), and Edema Factor (EF)", "Alpha toxin, Beta toxin, and Epsilon toxin", "Tetanospasmin, Tetanolysin, and Streptolysin", "Endotoxin, Enterotoxin, and Neurotoxin"],
         0, "Plasmid pXO1 encodes the anthrax toxin triad: Protective Antigen (PA, 83 kDa, binds host receptors CMG2/TEM8 and facilitates translocation), Lethal Factor (LF, zinc metalloprotease inactivating MAPKKs), and Edema Factor (EF, calmodulin-activated adenylate cyclase).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("McFadyean's reaction, a rapid presumptive diagnostic test for Anthrax in blood smears, utilizes which polychrome dye to demonstrate pink capsules around blue bacilli?",
         ["Polychrome Methylene Blue (Loeffler's alkaline methylene blue aged with potassium carbonate)", "Gram's crystal violet", "Ziehl-Neelsen carbol fuchsin", "India ink"],
         0, "McFadyean's stain (aged polychrome methylene blue containing oxidative breakdown products like azure B) stains the square-ended vegetative anthrax bacilli deep blue, enveloped by an amorphous reddish-purple/pink capsular halo.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The Ascoli thermoprecipitin test, utilized to confirm anthrax in putrefied or tanned animal tissues and hides, is based on which immunological reaction?",
         ["Ring precipitation reaction in a narrow tube between boiled tissue saline extract and hyperimmune anthrax antiserum", "Direct slide agglutination of red blood cells", "Complement fixation test", "Fluorescent antibody test on intact bacteria"],
         0, "Ascoli's test detects heat-stable polysaccharide cell wall antigens extracted from decomposed tissue by boiling in saline; when layered over anti-anthrax serum in a tube, a visible white precipitate ring forms at the liquid interface within minutes.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("The 'String of Pearls' reaction, used to distinguish Bacillus anthracis from other non-pathogenic environmental Bacillus species (such as B. cereus), is performed on:",
         ["Nutrient agar containing 0.05 to 0.5 units/mL of penicillin, where B. anthracis swells into round, spherical pearl-like chains within 3-6 hours", "MacConkey agar without salt", "Blood agar with 10% sodium chloride", "Sabouraud dextrose agar"],
         0, "B. anthracis is exquisitely sensitive to penicillin; subinhibitory penicillin concentrations cause cell wall lysis, transforming rods into large, spherical, refringent 'pearls' strung in chains within hours, whereas B. cereus is resistant.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The lethal action of Tetanospasmin (tetanus neurotoxin from Clostridium tetani) on the central nervous system occurs through which molecular mechanism?",
         ["Retrograde axonal transport to inhibitory Renshaw interneurons, where its zinc endopeptidase light chain cleaves synaptobrevin (VAMP-2), blocking release of GABA and glycine", "Direct irreversible blockade of post-synaptic nicotinic acetylcholine receptors at motor endplates", "Degradation of myelin sheaths by phospholipase C", "Continuous stimulation of dopamine receptors"],
         0, "Tetanospasmin enters peripheral motor nerve terminals, undergoes retrograde trans-synaptic transport to inhibitory Renshaw interneurons in the spinal cord, and cleaves synaptobrevin (VAMP-2), preventing exocytosis of inhibitory neurotransmitters (glycine/GABA), causing spastic tetanic paralysis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Clostridium botulinum neurotoxin produces flaccid paralysis by acting at the peripheral neuromuscular junction to block the release of:",
         ["Acetylcholine (ACh) from pre-synaptic cholinergic motor nerve terminals", "Norepinephrine from post-ganglionic sympathetic fibers", "Serotonin from platelets", "Histamine from tissue mast cells"],
         0, "Botulinum neurotoxin (BoNT) enters the pre-synaptic motor terminal and cleaves SNARE proteins (SNAP-25, syntaxin, or synaptobrevin), permanently preventing acetylcholine vesicle fusion and docking, causing generalized flaccid muscular paralysis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The Nagler reaction is an in vitro diagnostic agar plate test utilized for the rapid identification of Clostridium perfringens based on the inhibition of which enzyme by specific antitoxin?",
         ["Alpha-toxin (Phospholipase C / Lecithinase)", "Beta-toxin (pore-forming cytolysin)", "Epsilon-toxin (permease)", "Iota-toxin"],
         0, "C. perfringens alpha-toxin hydrolyzes lecithin in egg-yolk agar, producing a zone of opalescence (turbid halo) around colonies; spreading specific anti-alpha-toxin antiserum on one half of the plate completely neutralizes and inhibits this halo (Nagler positive).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("In 'Enterotoxemia' (Pulpy Kidney Disease) of sheep caused by Clostridium perfringens Type D, the protoxin that is cleaved and activated by trypsin in the intestinal lumen is:",
         ["Epsilon protoxin", "Alpha protoxin", "Delta toxin", "Theta toxin (perfringolysin O)"],
         0, "C. perfringens Type D secretes inactive epsilon protoxin into the intestine; pancreatic trypsin removes terminal residues, increasing its toxicity >1000-fold; active epsilon toxin binds vascular endothelium, increasing microvascular permeability in the brain and kidneys.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Clostridium chauvoei, the etiological agent of Blackleg in cattle and sheep, can be definitively differentiated from Clostridium septicum on liver impression smears because C. chauvoei:",
         ["Appears as single cells or pairs of pleomorphic rods, whereas C. septicum forms long filamentous chains (serpentine filaments)", "Is completely non-spore-forming", "Is Gram-negative", "Does not produce gas in muscle tissue"],
         0, "On the surface of the liver of infected guinea pigs or affected carcasses, Clostridium septicum characteristically forms long, filamentous, multinucleate chains, whereas Clostridium chauvoei occurs singly, in pairs, or in small clusters.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        # 11-20: Corynebacterium, Listeria, Erysipelothrix
        ("In Corynebacterium pseudotuberculosis, the primary exotoxin responsible for increasing vascular permeability and promoting systemic spread from local lesions is:",
         ["Phospholipase D (PLD)", "Diphtheria toxin", "Streptolysin O", "Pneumolysin"],
         0, "Phospholipase D (PLD) hydrolyzes sphingomyelin in host endothelial membranes, increasing microvascular permeability and permitting the bacteria to disseminate via lymphatic channels to regional lymph nodes, causing Caseous Lymphadenitis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Listeria monocytogenes exhibits characteristic 'tumbling motility' when incubated in semi-solid motility medium at:",
         ["22°C to 25°C (room temperature), but is non-motile at 37°C due to temperature-dependent flagellar repression", "37°C exclusively", "42°C", "56°C"],
         0, "Listeria monocytogenes expresses 4 peritrichous flagella regulated by the MogR repressor and GmaR anti-repressor at 20-25°C, exhibiting characteristic end-over-end tumbling motility; at 37°C, flagellar expression is downregulated.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The primary virulence factor utilized by intracellular Listeria monocytogenes to escape from the phagolysosome into the host cell cytoplasm is:",
         ["Listeriolysin O (LLO, a cholesterol-dependent cytolysin)", "Lecithinase C", "Protein A", "Catalase"],
         0, "After phagocytosis, the acidic pH of the phagolysosome activates Listeriolysin O (LLO) along with two phospholipases (PlcA and PlcB), which selectively form pores in the phagosomal membrane, allowing bacterial escape into the nutrient-rich cytosol.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Anton's test, used to verify the virulence of Listeria monocytogenes in the laboratory, is performed by instilling a bacterial suspension into the conjunctival sac of which laboratory animal?",
         ["Rabbit or Guinea pig, producing purulent keratoconjunctivitis within 24 to 48 hours", "White mouse, producing paralysis", "Hamster, producing subcutaneous edema", "Pigeon, producing encephalitis"],
         0, "Anton's eye test is a classical biological assay for virulent Listeria monocytogenes; instillation into the conjunctival sac of a rabbit or guinea pig produces severe purulent keratoconjunctivitis within 24-36 hours.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("In semi-solid motility agar, Listeria monocytogenes produces a pathognomonic macroscopic growth pattern beneath the surface resembling a(n):",
         ["Umbrella or parachute shape", "Inverted fir-tree", "Test-tube brush", "Medusa head"],
         0, "Because L. monocytogenes is microaerophilic to facultatively anaerobic, flagellated bacteria swim away from the surface towards optimal oxygen tension, creating a distinctive 2-5 mm sub-surface 'umbrella' or 'parachute' zone of turbidity.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The CAMP test (Christie, Atkins, Munch-Petersen) produces an enhanced, arrowhead-shaped zone of complete beta-hemolysis when Listeria monocytogenes is streaked perpendicular to:",
         ["Beta-lysin-producing Staphylococcus aureus on sheep blood agar", "Streptococcus agalactiae", "Bacillus cereus", "Pseudomonas aeruginosa"],
         0, "Listeriolysin O synergizes with the beta-hemolysin (sphingomyelinase C) of Staphylococcus aureus; streaking them perpendicular to each other on sheep blood agar produces an enhanced arrowhead zone of complete beta-hemolysis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Erysipelothrix rhusiopathiae produces a pathognomonic macroscopic growth appearance in 12% gelatin stab cultures incubated at 22°C, known as:",
         ["'Test-tube brush' or 'lamp-brush' pattern with lateral filamentous radiating projections", "Inverted Christmas tree liquefaction", "Complete rapid saccate liquefaction", "Surface pellicle only"],
         0, "In nutrient gelatin stab cultures, E. rhusiopathiae grows along the inoculation stab line and extends fine horizontal filamentous outgrowths without liquefying gelatin, resembling a bottle brush or lamp brush.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Erysipelothrix rhusiopathiae is uniquely distinguished biochemically from Listeria and Corynebacterium on Triple Sugar Iron (TSI) agar because Erysipelothrix:",
         ["Produces Hydrogen Sulfide (H2S), turning the agar butt jet black along the stab line", "Is strongly catalase-positive", "Liquefies gelatin within 2 hours", "Ferments lactose with gas production"],
         0, "Erysipelothrix rhusiopathiae is a slender Gram-positive non-sporing rod that is catalase-negative and uniquely produces H2S in TSI agar (black butt), whereas Listeria and Corynebacterium are catalase-positive and H2S-negative.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The primary surface protective antigen and major virulence factor of Erysipelothrix rhusiopathiae is:",
         ["Neuraminidase (sialidase) and SpaA (surface protective antigen A)", "Lecithinase", "Protein G", "Teichoic acid"],
         0, "SpaA is the major surface-exposed protective antigen targeted by host protective antibodies, while neuraminidase cleaves sialic acid from host endothelial cells, facilitating adherence and microvascular thrombosis.",
         False, "Systematic Bacteriology"),

        ("Cold enrichment (storage of homogenized tissue samples in nutrient broth at 4°C for several weeks prior to subculture) is a classic bacteriological isolation technique used for:",
         ["Listeria monocytogenes", "Bacillus anthracis", "Brucella abortus", "Pasteurella multocida"],
         0, "Listeria monocytogenes is psychrotrophic and can slowly multiply at 4°C, whereas competing environmental and commensal bacteria are arrested or die at refrigeration temperatures, enriching the sample for Listeria.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        # 21-30: Mycobacteria, Actinomycetes, Dermatophilus
        ("The property of 'Acid-Fastness' displayed by Mycobacterium species during Ziehl-Neelsen staining is conferred by the presence of high concentrations of:",
         ["Mycolic acids (long-chain beta-hydroxy branched fatty acids) in the cell wall", "Peptidoglycan cross-links", "Dipicolinic acid in the cytoplasm", "Calcium carbonate"],
         0, "Mycobacterial cell walls contain up to 60% lipids, predominantly high-molecular-weight mycolic acids (C60 to C90); when stained with heated carbol fuchsin, the dye complexes with mycolic acids and resists decolorization by 3% acid-alcohol.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The primary selective solid culture medium universally utilized for the primary isolation of Mycobacterium bovis and M. tuberculosis is:",
         ["Lowenstein-Jensen (LJ) medium (egg-based medium containing malachite green)", "MacConkey agar", "Eosin Methylene Blue (EMB) agar", "Tellurite blood agar"],
         0, "Lowenstein-Jensen medium consists of whole homogenized eggs, potato starch, glycerol/pyruvate, and malachite green; malachite green inhibits contaminating Gram-positive and Gram-negative bacteria while supporting slow mycobacterial growth.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("In the laboratory culture of Mycobacterium bovis, which carbon supplement must be added to Lowenstein-Jensen medium to stimulate growth, while avoiding glycerol?",
         ["Sodium pyruvate (0.5%)", "Glucose 2%", "Lactose 1%", "Maltose 5%"],
         0, "M. bovis is dysgonic (grows poorly) on standard glycerol-containing media; the substitution of glycerol with 0.5% sodium pyruvate markedly enhances the growth rate and colonial size of M. bovis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Mycobacterium avium subsp. paratuberculosis (MAP) is an obligate fastidious pathogen that strictly requires which iron-chelating growth factor (siderophore) for primary in vitro cultivation?",
         ["Mycobactin (e.g. Mycobactin J)", "Hemin (X factor)", "NAD (V factor)", "Nicotinic acid"],
         0, "MAP lacks the biosynthetic pathway to synthesize its own iron-chelating mycobactin; culture media (such as Herrold's egg yolk medium) must be supplemented with Mycobactin J to transport ferric iron across its lipidic cell wall.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The Single Intradermal Comparative Cervical Tuberculin (SICCT) test in cattle is read at 72 hours post-injection, and a positive bovine tuberculosis diagnosis is confirmed when:",
         ["The increase in skin-fold thickness at the Bovine PPD site exceeds the increase at the Avian PPD site by 4 mm or more", "Both sites show equal swelling of 2 mm", "The Avian PPD site exceeds the Bovine site by 5 mm", "Skin-fold thickness decreases by 2 mm"],
         0, "In the SICCT test, 0.1 mL of Avian PPD and Bovine PPD are injected intradermally at separate cervical sites; an animal is positive if the bovine reaction exceeds the avian reaction by >= 4 mm with clinical signs of edema or heat.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Actinomyces bovis, the causative agent of 'Lumpy Jaw' in cattle, is morphologically and physiologically characterized as a:",
         ["Gram-positive, non-acid-fast, microaerophilic to anaerobic branching filamentous rod that forms sulfur granules in vivo", "Gram-negative aerobic motile bacillus", "Strictly acid-fast spore-forming coccus", "Cell-wall-free intracellular bacterium"],
         0, "Actinomyces bovis is a microaerophilic Gram-positive rod that forms delicate branching filaments; in vivo colonies form dense mineralized clusters ('sulfur granules') in mandibular bone granulomas.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Actinobacillus lignieresii differs fundamentally from Actinomyces bovis in that Actinobacillus lignieresii is:",
         ["Gram-negative, aerobic to facultatively anaerobic, non-branching coccobacillus that typically invades soft tissues (tongue, lymph nodes)", "Gram-positive and strictly anaerobic", "Acid-fast", "Spore-forming"],
         0, "Actinobacillus lignieresii (wooden tongue) is a Gram-negative facultative rod that invades soft tissues (tongue), whereas Actinomyces bovis (lumpy jaw) is a Gram-positive branching anaerobe that invades bony tissues (mandible).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Dermatophilus congolensis, the etiological agent of 'Rain Rot' / 'Streptothricosis' in cattle and horses, displays which distinctive microscopic morphology on Giemsa-stained crust smears?",
         ["Branching filamentous hyphae that divide transversely and longitudinally to form parallel rows of coccoid zoospores resembling 'train tracks' / 'tram tracks'", "Single giant sporangia with endospores", "Encapsulated diplococci in pairs", "Large spiral organisms with terminal hooks"],
         0, "Dermatophilus congolensis has a unique life cycle: branching mycelial filaments undergo both transverse and longitudinal septation, forming 2 to 8 parallel rows of flagellated motile coccoid zoospores resembling miniature train tracks.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Nocardia asteroides, causing pyogranulomatous pleuritis and mastitis in domestic animals, is distinguished from Actinomyces by being:",
         ["Strictly aerobic and partially (weakly) acid-fast with modified Kinyoun staining", "Strictly anaerobic and non-acid-fast", "Gram-negative", "Penicillin-sensitive in all strains"],
         0, "Nocardia species are environmental, strictly aerobic actinomycetes possessing short-chain mycolic acids (nocardomycolic acids), rendering them partially/weakly acid-fast when decolorized with 1% sulfuric acid, whereas Actinomyces is non-acid-fast and microaerophilic.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The primary diagnostic method for detecting Trueperella pyogenes (formerly Arcanobacterium pyogenes) in suppurative lesions is observing:",
         ["Tiny pinpoint colonies on sheep blood agar surrounded by a narrow zone of beta-hemolysis at 48 hours, Gram-positive pleomorphic diphtheroid rods, and strong gelatinase activity", "Large spreading swarming colonies", "Medusa-head colonies on plain agar", "Green pigmentation on MacConkey agar"],
         0, "Trueperella pyogenes is a common commensal pyogen in ruminants; it forms tiny colonies showing slow beta-hemolysis on blood agar at 48h, produces pyolysin (PLO, a cholesterol-dependent cytolysin), and is catalase-negative and gelatinase-positive.",
         False, "Systematic Bacteriology"),

        # 31-40: Brucella, Pasteurella, Mannheimia
        ("In cattle, the tissue tropism of Brucella abortus for the gravid placenta, chorionic cotyledons, and fetal fluids is directly mediated by the presence of:",
         ["Erythritol (a 4-carbon polyhydric alcohol synthesized by the bovine placenta)", "Glycogen", "Sialic acid", "Fructose"],
         0, "The ungulate placenta and fetal fluids synthesize erythritol, which serves as a preferred growth stimulant for Brucella abortus, melitensis, and suis, driving logarithmic bacterial multiplication and acute placentitis in late gestation.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The Rose Bengal Plate Test (RBPT), a widely used rapid screening test for Bovine Brucellosis, utilizes an antigen buffered to an acidic pH of 3.65 in order to:",
         ["Prevent non-specific agglutination caused by IgM antibodies, allowing specific IgG1 antibodies to agglutinate", "Inactivate complement components C1 to C9", "Lyse contaminating red blood cells", "Dissolve the bacterial cell wall"],
         0, "Buffering the Rose Bengal antigen to pH 3.65 inhibits non-specific agglutination mediated by pentameric IgM and cross-reacting antibodies (e.g. Yersinia enterocolitica O:9), ensuring high specificity for protective IgG1.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("In the Milk Ring Test (MRT) for herd screening of Bovine Brucellosis, a positive pooled milk sample is indicated by:",
         ["A distinct dark blue or purple ring forming in the cream layer at the top of the milk column, with a white milk column underneath", "Uniform purple color throughout the entire tube", "A purple pellet at the bottom of the tube", "Complete curdling of milk without color change"],
         0, "Brucella abortus antigen is stained with hematoxylin (blue/purple); milk fat globules adsorb fat-soluble agglutinins (IgA/IgM), rising to the surface to form a cream layer. In positive milk, the stained antigen aggregates and rises into the cream layer, forming a purple ring.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Which species of Brucella is characteristically 'rough' (lacks the O-antigen smooth lipopolysaccharide side chain) in its natural virulent wild-type state?",
         ["Brucella canis (and Brucella ovis)", "Brucella abortus", "Brucella melitensis", "Brucella suis"],
         0, "While B. abortus, melitensis, and suis naturally express smooth lipopolysaccharide (S-LPS) containing perosamine O-chains, Brucella canis and Brucella ovis are naturally rough (R-LPS), lacking the O-polysaccharide chain.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Hemorrhagic Septicemia (HS) in cattle and water buffaloes in Asia and Africa is caused by which specific capsular serotypes of Pasteurella multocida?",
         ["Carter's capsular Type B (B:2 in Asia) and Type E (E:2 in Africa)", "Type A (A:1)", "Type D (D:1)", "Type F"],
         0, "Under Carter's indirect hemagglutination capsular typing and Heddleston's somatic typing, Asian hemorrhagic septicemia is caused by P. multocida serotype B:2, while African HS is caused by serotype E:2.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("In blood and tissue smears from cattle dying of acute Hemorrhagic Septicemia, Pasteurella multocida exhibits pathognomonic staining as:",
         ["Gram-negative coccobacilli showing distinct 'bipolar staining' (dense terminal coloration with a clear center) with Leishman, Giemsa, or Methylene Blue", "Gram-positive square-ended rods in long chains", "Acid-fast beaded filaments", "Large encapsulated diplococci"],
         0, "Pasteurella multocida is a small (0.3 x 1.5 um) Gram-negative ovoid rod; on Romanowsky-stained blood smears (Giemsa/Leishman), it characteristically concentrates dye at both poles ('bipolar safety-pin appearance').",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Atrophic Rhinitis (AR) in swine is caused by the synergistic action of which two respiratory pathogens?",
         ["Toxigenic Pasteurella multocida (capsular Type D producing dermonecrotic toxin) and Bordetella bronchiseptica", "Mycoplasma hyopneumoniae and Actinobacillus pleuropneumoniae", "Streptococcus suis and Haemophilus parasuis", "Swine Influenza Virus and PRRSV"],
         0, "Bordetella bronchiseptica colonizes the nasal mucosa, producing mild rhinitis and facilitating mucosal penetration by Pasteurella multocida Type D; P. multocida dermonecrotic toxin (PMT) stimulates osteoclasts and suppresses osteoblasts, resorbing nasal turbinates.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Mannheimia haemolytica is distinguished biochemically and culturally from Pasteurella multocida because Mannheimia haemolytica:",
         ["Produces narrow zones of beta-hemolysis on sheep blood agar and grows on MacConkey agar (lactose-fermenting pink colonies)", "Is completely non-hemolytic and does not grow on MacConkey agar", "Produces indole from tryptophan", "Is strictly anaerobic"],
         0, "Pasteurella multocida does not grow on MacConkey agar and is non-hemolytic, whereas Mannheimia haemolytica produces beta-hemolysis on bovine/ovine blood agar, grows as small pink colonies on MacConkey agar, and is indole-negative.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The principal virulence factor of Mannheimia haemolytica responsible for acute pulmonary necrosis in Bovine Respiratory Disease Complex (BRDC) is:",
         ["Leukotoxin (LKT), an RTX family pore-forming cytolysin targeting CD11a/CD18 (LFA-1) on ruminant leukocytes", "Enterotoxin A", "Capsular polysaccharide exclusively", "Hyaluronidase"],
         0, "M. haemolytica leukotoxin (LKT) specifically targets beta-2 integrins (LFA-1 / CD11a/CD18) on ruminant neutrophils and alveolar macrophages, causing intracellular calcium influx, respiratory burst activation, cytolysis, and severe fibrinous pleuropneumonia.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The laboratory animal of choice used for the biological isolation and virulence typing of Pasteurella multocida from clinical field samples is:",
         ["White mouse (Mus musculus), which dies within 18 to 24 hours of subcutaneous inoculation with pure septicemia", "Guinea pig", "Adult rabbit", "Hamster"],
         0, "Mice are exceptionally sensitive to virulent Pasteurella multocida; subcutaneous inoculation of <10 colony-forming units causes fatal bacteremia and death within 18-24 hours, yielding pure cultures from heart blood.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        # 41-50: Enterobacteriaceae: Salmonella, E. coli, Klebsiella
        ("In the Kauffmann-White classification scheme for Salmonella, serovars are classified based on the antigenic variation of which cellular structures?",
         ["O (somatic lipopolysaccharide) antigens, H (flagellar phase 1 and phase 2) antigens, and Vi (capsular virulence) antigens", "Capsular polysaccharides only", "Pili proteins only", "Cell wall peptidoglycan cross-links"],
         0, "The Kauffmann-White diagnostic scheme differentiates over 2,500 Salmonella serotypes based on somatic O-antigens (oligosaccharide repeats), flagellar H-antigens (often biphasic: phase 1 and phase 2), and capsular Vi (virulence) polysaccharides.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Salmonella enterica serovar Dublin is of paramount veterinary significance because it is the host-adapted serovar of:",
         ["Cattle, causing severe neonatal septicemia, dry gangrene of extremities, and chronic carrier states in adult dairy cows", "Swine exclusively", "Horses", "Poultry"],
         0, "Salmonella Dublin is host-adapted to cattle; in calves, it causes severe septicemia, pneumonia, and terminal dry gangrene of ear tips/tail, while infected cows become lifelong latent carriers harboring organisms in the gallbladder and mesenteric lymph nodes.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("On differential selective media, Salmonella species are distinguished from typical commensal Escherichia coli because Salmonella is:",
         ["Lactose non-fermenting (pale translucent colonies on MacConkey) and produces Hydrogen Sulfide (H2S, black centers on XLD and Hektoen enteric agar)", "Lactose fermenting (bright pink on MacConkey)", "Urease positive within 2 hours", "Completely non-motile in all serotypes"],
         0, "Unlike E. coli (which ferments lactose, forming pink colonies on MacConkey agar without H2S), Salmonella is lactose-negative (colorless colonies on MacConkey) and produces H2S from thiosulfate, forming black colonies on XLD and TSI.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Neonatal colibacillosis (white scours) in calves under 5 days of age is caused by Enterotoxigenic E. coli (ETEC) expressing which specific fimbrial adhesin that binds to intestinal enterocytes?",
         ["F5 (K99) fimbriae", "F4 (K88) fimbriae", "F18 fimbriae", "P fimbriae"],
         0, "Calf ETEC strains produce F5 (K99) fimbriae that attach to specific glycoprotein receptors on the microvilli of enterocytes in calves during the first 3-5 days of life (receptors are lost as the calf matures).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Post-weaning diarrhea and Edema Disease in nursery piglets are caused by specific E. coli strains expressing which fimbrial adhesins and exotoxins?",
         ["F18 (or F4/K88) fimbriae and Shiga toxin 2e (Stx2e / Verotoxin)", "K99 and heat-labile toxin", "Type 1 pili and hemolysin only", "CFA/I fimbriae and cholera toxin"],
         0, "Edema disease is caused by STEC strains expressing F18 fimbriae that colonize the porcine small intestine and produce Stx2e (Shiga toxin 2e), which enters the bloodstream, destroying endothelial cells in arterioles and causing subcutaneous, palpebral, and mesocolic edema.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("On Eosin Methylene Blue (EMB) agar, lactose-fermenting Escherichia coli colonies produce a pathognomonic macroscopic appearance of:",
         ["A distinctive dark colony with a brilliant green metallic sheen", "Colorless translucent colonies", "Mucoid pink colonies", "Jet-black colonies with red halos"],
         0, "Rapid fermentation of lactose by E. coli drops the pH, precipitating eosin and methylene blue dyes as an insoluble complex, imparting a diagnostic green metallic sheen to the colonies under reflected light.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("The standard IMViC biochemical series used to differentiate Escherichia coli from Enterobacter and Klebsiella yields which reaction profile for typical E. coli?",
         ["Indole positive (+), Methyl Red positive (+), Voges-Proskauer negative (-), Citrate negative (-)  [+ + - -]", "Indole (-), MR (-), VP (+), Citrate (+) [- - + +]", "Indole (+), MR (-), VP (+), Citrate (-)", "Indole (-), MR (+), VP (-), Citrate (+)"],
         0, "E. coli splits tryptophan to indole (+), ferments glucose via the mixed-acid pathway maintaining pH < 4.4 (+ for Methyl Red), does not produce acetoin (- for VP), and cannot utilize citrate as sole carbon source (- for Citrate): [+ + - -].",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Klebsiella pneumoniae causes acute, severe coliform mastitis in dairy cattle and is culturally recognized by forming colonies that are:",
         ["Extremely large, highly mucoid, viscous, and lactose-fermenting on MacConkey agar due to an abundant polysaccharide capsule", "Small, dry, chalky, and non-lactose fermenting", "Swarming in concentric waves across the plate", "Green-pigmented with a fruity odor"],
         0, "Klebsiella pneumoniae synthesizes a massive, thick capsule of complex acidic polysaccharides; colonies on agar are conspicuously large, dome-shaped, glistening, and strings of slime adhere to inoculation loops when touched.",
         False, "Systematic Bacteriology"),

        ("The distinctive 'swarming phenomenon' (concentric waves of cyclic film-like spreading across moist non-inhibitory blood agar plates) is characteristic of:",
         ["Proteus mirabilis and Proteus vulgaris", "Escherichia coli", "Salmonella enterica", "Pseudomonas aeruginosa"],
         0, "Proteus species exhibit cyclic differentiation between short vegetative 'swimmer' cells in liquid and elongated, hyperflagellated, multinucleated 'swarmer' cells on solid agar, producing periodic concentric rings of growth.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Yersinia enterocolitica and Yersinia pseudotuberculosis exhibit which temperature-dependent motility characteristic?",
         ["Motile via peritrichous flagella at 22°C to 28°C, but completely non-motile at 37°C", "Motile at 37°C but non-motile at 22°C", "Non-motile at all temperatures", "Gliding motility at 42°C"],
         0, "Like Listeria, Yersinia species synthesize flagella and express motility at ambient room temperatures (22-28°C), whereas at physiological mammalian body temperature (37°C), flagellar synthesis is repressed.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        # 51-60: Pseudomonas, Burkholderia, Campylobacter, Helicobacter
        ("Pseudomonas aeruginosa is an opportunistic pathogen of veterinary importance that produces which two characteristic diagnostic pigments?",
         ["Pyocyanin (blue-green phenazine pigment) and Pyoverdine (yellow-green fluorescent siderophore)", "Prodigiosin and Melanin", "Bacteriochlorophyll and Carotenoid", "Violacein and Hematin"],
         0, "Pseudomonas aeruginosa produces pyocyanin (a blue-green redox-active phenazine pigment that stimulates superoxide generation) and pyoverdine (a water-soluble yellow-green fluorescent siderophore that fluoresces under UV light).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The characteristic sensory odor described for cultures and wound exudates containing Pseudomonas aeruginosa is:",
         ["A sweet, fruity, grape-like or corn-taco odor (due to 2-aminoacetophenone production)", "A foul putrid odor of rotting meat", "A pungent ammonia odor", "An odor of rancid butter"],
         0, "Pseudomonas aeruginosa metabolizes amino acids to synthesize 2-aminoacetophenone, which imparts a distinctive sweet, aromatic, fruity grape-like or corn-tortilla odor.",
         False, "Systematic Bacteriology"),

        ("In horses, Glanders is caused by Burkholderia mallei, which is morphologically and culturally distinguished from other pseudomonads because B. mallei is:",
         ["Strictly non-motile (lacks flagella) and is an obligate parasite of equids", "Actively motile with lophotrichous flagella", "Gram-positive", "A strict spore-former"],
         0, "Unlike Burkholderia pseudomallei (the motile environmental saprophyte causing Melioidosis), Burkholderia mallei is non-motile, has no environmental reservoir outside infected equids, and causes chronic contagious granulomatous nodules.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The official diagnostic allergic skin test for Glanders in horses is the Mallein test, and the preferred international method of administration is the:",
         ["Intradermo-palpebral test (injection of 0.1 mL mallein into the skin of the lower eyelid, causing marked edema and purulent conjunctivitis at 48 hours)", "Subcutaneous thermal test", "Cervical skin pinch test", "Caudal fold test"],
         0, "The intradermo-palpebral test is the standard OIE-recognized method: 0.1 mL of mallein is injected into the lower eyelid; in infected horses, a positive delayed-type hypersensitivity reaction produces severe, marked eyelid swelling and purulent discharge.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Burkholderia pseudomallei, the etiological agent of Melioidosis ('Whitmore's disease') in domestic animals and humans in Southeast Asia and Northern Australia, is characteristically culturally identified by:",
         ["A distinctive wrinkled, corrugated, dry 'cornflower' colonial morphology on Ashdown's selective medium", "Smooth, wet, mucoid colonies on plain agar", "Failure to grow on any media without blood", "Production of brilliant red pigments"],
         0, "On Ashdown's agar (containing crystal violet and gentamicin), B. pseudomallei colonies take up crystal violet, turning purple, and develop a diagnostic wrinkled, corrugated surface resembling a miniature cornflower.",
         False, "Systematic Bacteriology"),

        ("Campylobacter fetus subsp. venerealis causes Bovine Venereal Campylobacteriosis, characterized pathologically by:",
         ["Infertility, prolonged estrous cycles, and early embryonic death, transmitted venereally without clinical signs in the bull", "Severe late-term abortion storms in >80% of cows with retainment of cotyledons", "Acute orchitis and purulent urethritis in the bull", "Ulcerative stomatitis in calves"],
         0, "Campylobacter fetus subsp. venerealis is harbored subclinically in the preputial crypts of mature bulls; during coitus, it is transferred to cows, establishing mild endometritis and salpingitis that prevents blastocyst implantation (early embryonic death).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The microscopic morphology and motility of Campylobacter species in wet mounts from freshly aborted fetal abomasal contents are characterized as:",
         ["Gram-negative curved, gull-wing, comma-shaped or spiral rods showing rapid 'darting' or corkscrew motility", "Straight square-ended rods with tumbling motility", "Branching filaments with gliding motility", "Chains of non-motile cocci"],
         0, "Campylobacters possess a single polar unsheathed flagellum at one or both ends, imparting rapid, erratic, darting motility; under phase-contrast or Gram stain, two joined curved cells form a diagnostic 'gull-wing' or 'flying seagull' shape.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The microaerophilic gaseous environment required for optimal laboratory cultivation of Campylobacter species consists of approximately:",
         ["5% O2, 10% CO2, and 85% N2", "21% O2 and 0.04% CO2 (atmospheric air)", "Strictly 0% O2 (anaerobic jar with hydrogen)", "100% Carbon dioxide"],
         0, "Campylobacters are microaerophiles; they require reduced oxygen tension (5% O2) with elevated carbon dioxide (10% CO2) and inert nitrogen (85% N2), and are inhibited by atmospheric oxygen concentrations.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Helicobacter mustelae is an established pathogenic gastric bacterium causing chronic gastritis and peptic ulceration in which domestic animal species?",
         ["Ferrets", "Cats", "Dogs", "Horses"],
         0, "Helicobacter mustelae colonizes the gastric mucosa of virtually all adult ferrets, utilizing high urease activity to neutralize stomach acid and cause chronic lymphoplasmacytic gastritis and bleeding pyloric ulcers.",
         False, "Systematic Bacteriology"),

        ("Lawsonia intracellularis is an obligate intracellular bacterium of veterinary importance that causes 'Porcine Proliferative Enteropathy' (ileitis), targeting which cell population?",
         ["Immature dividing crypt epithelial cells of the ileum, causing marked crypt hyperplasia without goblet cells", "Surface enterocytes on villus tips", "Brunner's glands of the duodenum", "Peyer's patch B-lymphocytes"],
         0, "Lawsonia intracellularis invades and multiplies freely within the cytoplasm of immature enterocytes in the crypts of Lieberkühn, inhibiting maturation and driving continuous hyperplasia of the crypt epithelium ('garden-hose ileum').",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        # 61-70: Spirochaetes & Mycoplasmatales
        ("In Leptospira interrogans, the definitive serological gold standard reference test recommended by the WOAH (OIE) for diagnosing leptospirosis is the:",
         ["Microscopic Agglutination Test (MAT) using live cultured leptospiral serovars", "Enzyme-Linked Immunosorbent Assay (ELISA)", "Rose Bengal Plate Test", "Complement Fixation Test"],
         0, "The Microscopic Agglutination Test (MAT) involves incubating serial dilutions of patient serum with live cultures of reference leptospiral serovars, followed by dark-field microscopic examination for 50% agglutination.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Direct visualization of Leptospira in urine or blood smears under light microscopy requires which specialized optical system?",
         ["Dark-field microscopy (Dark-ground illumination)", "Standard bright-field microscopy with Gram stain", "Phase-contrast microscopy of dried smears", "Fluorescent microscopy without dyes"],
         0, "Because Leptospira are exceptionally thin spirochaetes (0.1 um wide by 6-20 um long), their refractive index is nearly identical to glass and water; dark-field microscopy scatters light from their coiled helical bodies, rendering them brightly visible against a black background.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("The primary specialized culture medium employed for the in vitro propagation of Leptospira species is:",
         ["Ellinghausen-McCullough-Johnson-Harris (EMJH) medium containing bovine serum albumin and Tween-80", "Lowenstein-Jensen medium", "MacConkey agar", "Chocolate agar"],
         0, "Leptospires utilize long-chain fatty acids as their sole carbon and energy source; EMJH semisolid or liquid medium provides Tween-80 (polyoxyethylene sorbitan monooleate) as a lipid source, buffered with BSA.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("In swine, 'Swine Dysentery' (mucohemorrhagic colitis) is caused by which strongly beta-hemolytic anaerobic spirochaete?",
         ["Brachyspira hyodysenteriae", "Brachyspira pilosicoli", "Treponema pallidum", "Borrelia burgdorferi"],
         0, "Brachyspira hyodysenteriae is a fastidious, oxygen-tolerant anaerobic spirochaete that produces strong beta-hemolysis on blood agar; it invades colonic goblet cells and crypts, causing extensive mucohemorrhagic colitis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Lyme Disease in dogs, horses, and humans is caused by Borrelia burgdorferi and is transmitted by which tick vector?",
         ["Ixodes scapularis and Ixodes ricinus (hard ticks)", "Rhipicephalus sanguineus", "Dermacentor variabilis", "Argas persicus"],
         0, "Borrelia burgdorferi is transmitted by the bite of nymphal and adult black-legged deer ticks belonging to the Ixodes ricinus complex (Ixodes scapularis in North America, I. ricinus in Europe), requiring >24-48 hours of tick attachment.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Mycoplasma species differ fundamentally from all other true bacteria because they:",
         ["Completely lack a rigid peptidoglycan cell wall and incorporate sterols (cholesterol) into their triple-layered plasma membrane", "Possess a thick waxy mycolic acid wall", "Are obligate intracellular parasites of mitochondria", "Produce heat-resistant endospores"],
         0, "Mycoplasmatales lack peptidoglycan cell wall genes; their bounding membrane is a sterol-containing trilaminar plasma membrane, rendering them pleomorphic, completely resistant to beta-lactam antibiotics (penicillins), and sensitive to osmotic lysis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("On specialized solid agar media (such as Hayflick's or PPLO agar), colonies of Mycoplasma species typically display which pathognomonic macroscopic appearance?",
         ["'Fried-egg' appearance (a dense central core embedded in the agar surrounded by a flat translucent peripheral zone)", "Smooth mucoid dome-shaped colonies", "Medusa-head colonies", "Spreading swarming colonies"],
         0, "Because Mycoplasmas lack cell walls, multiplying cells grow downward into the microscopic interstices of the agar gel to form a dense central core, while surface replication produces a pale, flat outer zone ('fried-egg colony').",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Contagious Caprine Pleuropneumonia (CCPP), a devastating respiratory disease of goats, is caused by:",
         ["Mycoplasma capricolum subsp. capripneumoniae", "Mycoplasma mycoides subsp. mycoides", "Mycoplasma bovis", "Mycoplasma agalactiae"],
         0, "CCPP is strictly caused by Mycoplasma capricolum subsp. capripneumoniae (formerly Mycoplasma strain F38), producing severe serofibrinous pleuropneumonia with high morbidity (>90%) and mortality in goats.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Contagious Agalactia of sheep and goats, characterized by the syndrome of mastitis, arthritis, and keratoconjunctivitis, is predominantly caused by:",
         ["Mycoplasma agalactiae", "Mycoplasma mycoides subsp. capri", "Mycoplasma putrefaciens", "Mycoplasma conjunctivae"],
         0, "Mycoplasma agalactiae produces the classic triad: interstitial mastitis with loss of milk secretion (agalactia), fibrinous polyarthritis (swollen carpal/tarsal joints), and keratitis in small ruminants.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The laboratory test based on sensitivity to Digitonin is routinely employed in veterinary microbiology to distinguish:",
         ["Sterol-requiring Mycoplasmataceae (sensitive to digitonin) from non-sterol-requiring Acholeplasmataceae (resistant to digitonin)", "Gram-positive bacteria from Gram-negative bacteria", "Aerobic bacteria from anaerobic bacteria", "Spore-forming from non-spore-forming bacteria"],
         0, "Digitonin forms an insoluble complex with membrane cholesterol; true Mycoplasmas require cholesterol for membrane stability and are lysed/inhibited by digitonin discs, whereas Acholeplasma species do not require cholesterol and are resistant.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        # 71-80: Staphylococci, Streptococci
        ("Staphylococcus aureus is definitively differentiated from commensal coagulase-negative staphylococci (such as S. epidermidis) by the production of:",
         ["Coagulase enzyme (converting rabbit or bovine plasma fibrinogen to fibrin clot)", "Catalase enzyme", "Oxidase enzyme", "Lecithinase"],
         0, "Coagulase production (both slide coagulase / clumping factor and tube coagulase / free staphylocoagulase) is the universally accepted standard diagnostic marker of pathogenicity differentiating S. aureus from coagulase-negative staphylococci.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("In bovine mastitis diagnostics, Staphylococcus aureus colonies on sheep blood agar characteristically exhibit 'Double-Zone Hemolysis' produced by the synergistic action of:",
         ["Alpha-toxin (complete inner zone of clear hemolysis) and Beta-toxin (outer wide zone of incomplete hot-cold hemolysis / sphingomyelinase)", "Beta-toxin and Gamma-toxin", "Delta-toxin and Leukocidin", "Enterotoxin A and TSST-1"],
         0, "Staphylococcus aureus secretes alpha-toxin (pore-forming cytolysin causing complete clear lysis close to the colony) and beta-toxin (sphingomyelinase C causing an outer zone of incomplete lysis that completes upon chilling at 4°C: hot-cold hemolysis).",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Protein A, a major cell wall virulence factor of Staphylococcus aureus, enhances immune evasion by binding to the:",
         ["Fc region of host IgG antibodies, orienting the antibody backwards and preventing opsonophagocytosis by neutrophils", "Fab antigen-binding fragment of IgM", "C3b complement component", "T-cell receptor"],
         0, "Protein A binds specifically to the Fc portion of IgG molecules (leaving Fab sites pointing outward away from the bacterium), preventing Fc receptor recognition by phagocytes and blocking classical complement pathway activation.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Staphylococcus pseudintermedius has emerged as the premier pyogenic pathogen causing canine pyoderma and otitis externa, and differs from S. aureus because S. pseudintermedius is:",
         ["Coagulase-positive, VP (acetoin) negative, and ONPG negative", "Strictly coagulase-negative", "Gram-negative", "An obligate anaerobe"],
         0, "S. pseudintermedius is the principal coagulase-positive staphylococcus of dogs and cats; it is differentiated from S. aureus biochemically because S. pseudintermedius is Voges-Proskauer (acetoin) negative and ONPG negative, whereas S. aureus is VP positive.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The Lancefield serological grouping of beta-hemolytic Streptococci (Groups A through V) is based on the immunological extraction and identification of:",
         ["Cell wall C-carbohydrate (polysaccharide) antigens", "M protein antigens", "Capsular hyaluronic acid", "Streptolysin O"],
         0, "Rebecca Lancefield classified beta-hemolytic streptococci based on group-specific carbohydrate antigens ('C-substance') located in the cell wall, extracted using hot hydrochloric acid or formamide and identified by precipitation.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Streptococcus equi subsp. equi, the causative agent of 'Strangles' in horses, belongs to which Lancefield group?",
         ["Lancefield Group C", "Lancefield Group A", "Lancefield Group B", "Lancefield Group D"],
         0, "Streptococcus equi subsp. equi, along with S. equi subsp. zooepidemicus and S. dysgalactiae, possesses the Lancefield Group C carbohydrate antigen; it causes acute suppurative lymphadenitis of submandibular and retropharyngeal lymph nodes.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Streptococcus agalactiae, an obligate pathogen of the bovine mammary gland causing chronic contagious mastitis, belongs to Lancefield Group B and is identified by a positive:",
         ["CAMP test (synergistic arrowhead beta-hemolysis with Staph aureus beta-lysin)", "Coagulase test", "Catalase test", "Oxidase test"],
         0, "Streptococcus agalactiae secretes the CAMP factor (a heat-stable 23.5 kDa extracellular protein) that interacts with staphylococcal beta-hemolysin on sheep blood agar, producing an expanded arrowhead-shaped zone of complete hemolysis.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("In sheep and goats, contagious agalactia caused by bacterial mastitis where milk turns purulent with yellow flakes is commonly caused by:",
         ["Streptococcus uberis and Streptococcus dysgalactiae", "Bacillus subtilis", "Lactobacillus acidophilus", "Proteus vulgaris"],
         0, "Environmental streptococci (S. uberis and S. dysgalactiae) are major etiological agents of clinical and subclinical bovine and small ruminant mastitis, surviving in straw bedding and teat skin.",
         False, "Systematic Bacteriology"),

        ("Enterococcus faecalis and Enterococcus faecium (formerly Group D streptococci) are distinguished from other streptococci by their ability to:",
         ["Hydrolyze esculin in the presence of 40% bile salts (Bile-Esculin positive) and grow in 6.5% NaCl broth", "Produce catalase", "Grow on Cetrimide agar", "Produce gas from lactose"],
         0, "Enterococci are exceptionally hardy: they tolerate 40% bile, hydrolyze esculin to esculetin (which turns ferric citrate agar black), and grow luxuriantly in 6.5% NaCl broth and at pH 9.6.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("The 'Optochin sensitivity test' (ethylhydrocupreine hydrochloride disc) is used in veterinary diagnostic microbiology to differentiate:",
         ["Optochin-sensitive Streptococcus pneumoniae from optochin-resistant alpha-hemolytic Viridans streptococci", "Staphylococcus from Micrococcus", "Bacillus from Clostridium", "E. coli from Salmonella"],
         0, "Streptococcus pneumoniae is bile-soluble and exquisitely sensitive to optochin discs (zone of inhibition >= 14 mm on blood agar), whereas oral viridans streptococci are optochin-resistant.",
         False, "Systematic Bacteriology"),

        # 81-90: Fastidious Gram-negatives, Rickettsia, Chlamydia
        ("Glaesserella parasuis (formerly Haemophilus parasuis) is the etiological agent of 'Glässer's Disease' in nursery pigs, characterized pathologically by:",
         ["Severe fibrinous polyserositis (polyarthritis, pleuritis, pericarditis, and peritonitis)", "Atrophic rhinitis with facial distortion", "Acute hemorrhagic enteritis", "Necrotic hepatitis with target lesions"],
         0, "Glaesserella parasuis is a fastidious V-factor (NAD) dependent coccobacillus; systemic dissemination in non-immune piglets produces acute, severe fibrinopurulent inflammation across all serosal cavities ('fibrinous polyserositis').",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Taylorella equigenitalis, the causative agent of Contagious Equine Metritis (CEM), is culturally isolated on chocolate agar incubated under 5-10% CO2 and is biochemically:",
         ["Strongly Oxidase positive, Catalase positive, and Phosphatase positive, but inert to all carbohydrate fermentations", "Lactose fermenting with gas", "Urease positive", "Coagulase positive"],
         0, "Taylorella equigenitalis is an unreactive, fastidious microaerophilic Gram-negative coccobacillus; it does not ferment any sugars, but gives rapid, intense positive reactions for cytochrome oxidase, catalase, and alkaline phosphatase.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Avian Chlamydiosis (Psittacosis / Ornithosis) is caused by Chlamydia psittaci, which possesses a biphasic developmental cycle consisting of which two distinct morphological forms?",
         ["Infectious, metabolically inert 'Elementary Bodies' (EB) and non-infectious, intracellular multiplying 'Reticulate Bodies' (RB)", "Trophozoites and cysts", "Sporozoites and merozoites", "Vegetative cells and endospores"],
         0, "Elementary bodies (EBs, 0.3 um) are rigid, extracellular, environmentally stable, and infectious; once endocytosed by host cells, they reorganize into larger, non-infectious, metabolically active Reticulate bodies (RBs, 1.0 um) that replicate by binary fission.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Coxiella burnetii, the causative agent of Q Fever in ruminants and humans, is exceptionally resistant to environmental heat, desiccation, and disinfectants because it forms:",
         ["A small, condensed, spore-like cell form termed the 'Small Cell Variant' (SCV)", "A poly-D-glutamic acid capsule", "A thick peptidoglycan cell wall like Bacillus", "Endospores containing dipicolinic acid"],
         0, "Coxiella burnetii transitions between a metabolically active Large Cell Variant (LCV) and a condensed, dehydrated Small Cell Variant (SCV) that possesses condensed chromatin and disulfide-crosslinked envelope proteins, resisting harsh physical conditions.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("In dogs, Canine Monocytic Ehrlichiosis is caused by Ehrlichia canis, which infects and forms characteristic intracytoplasmic morulae inside:",
         ["Monocytes and Macrophages", "Erythrocytes exclusively", "Neutrophils and Eosinophils", "Platelets only"],
         0, "Ehrlichia canis is transmitted by the brown dog tick Rhipicephalus sanguineus; it selectively parasitizes circulating monocytes, forming membrane-bound microcolonies called 'morulae' that stain dark blue with Giemsa.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Anaplasma marginale causes Bovine Anaplasmosis ('Gall Sickness') and is microscopic observed on Giemsa-stained blood smears as:",
         ["Dense, spherical, dark purple inclusion bodies located on or near the periphery (margin) of erythrocytes", "Intra-erythrocytic paired piriform bodies", "Extracellular comma-shaped flagellates", "Large morulae in neutrophils"],
         0, "Anaplasma marginale is an obligate intra-erythrocytic bacterium; on thin blood films stained with Giemsa, it appears as 0.3-0.5 um dark-staining spherical bodies located at the extreme periphery of bovine RBCs.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Anaplasma centrale differs from Anaplasma marginale in that Anaplasma centrale:",
         ["Produces mild or subclinical anemia, exhibits inclusion bodies located centrally within erythrocytes, and is used as a live vaccine in cattle", "Is fatal in 90% of cattle", "Is transmitted exclusively by lice", "Lacks DNA"],
         0, "Theiler discovered Anaplasma centrale; its inclusion bodies sit near the center of erythrocytes, causing mild anemia, and it has been used globally for over a century as a live heterologous vaccine against virulent A. marginale.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Canine Infectious Cyclic Thrombocytopenia is caused by which tick-borne intracellular organism that selectively infects blood platelets?",
         ["Anaplasma platys", "Ehrlichia canis", "Babesia gibsoni", "Rickettsia rickettsii"],
         0, "Anaplasma platys (formerly Ehrlichia platys) is unique in parasitizing canine blood platelets (thrombocytes), forming basophilic morulae that induce cyclic episodes of profound thrombocytopenia.",
         True, "Systematic Bacteriology (ICAR PG PYQ)"),

        ("Rocky Mountain Spotted Fever in dogs and humans is caused by Rickettsia rickettsii, which exhibits a primary cellular tropism for:",
         ["Vascular endothelial cells, causing acute necrotizing vasculitis and petechial hemorrhages", "Renal glomerular podocytes", "Hepatic Kupffer cells", "Skeletal myocytes"],
         0, "Rickettsia rickettsii invades and replicates within endothelial cells lining arterioles, capillaries, and venules, causing widespread endothelial necrosis, microvascular thrombosis, increased permeability, and petechial rashes.",
         False, "Systematic Bacteriology"),

        ("The 'Satellite Phenomenon' is a classic bacteriological culture characteristic of Actinobacillus pleuropneumoniae and Glaesserella parasuis, observed when grown on sheep blood agar near a nurse streak of:",
         ["Staphylococcus aureus, which secretes excess V-factor (NAD) required for satellite colony growth", "Bacillus anthracis", "Escherichia coli", "Pseudomonas aeruginosa"],
         0, "Sheep blood contains NAD-hydrolyzing enzymes (NADase), but lacks free V-factor; when S. aureus is streaked across the plate, it lyses RBCs and synthesizes excess NAD (V-factor), permitting fastidious V-dependent bacteria to grow as tiny 'satellite' colonies adjacent to the staphylococcal streak.",
         True, "Systematic Bacteriology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module1_questions()
    print(f"Microbiology Module 1 loaded: {len(qs)} questions")
