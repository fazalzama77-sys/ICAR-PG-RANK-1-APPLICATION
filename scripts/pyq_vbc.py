# scripts/pyq_vbc.py
# 100 ICAR AIEEA PG (M.V.Sc.) Previous Year Question (PYQ) Style MCQs for Veterinary Biochemistry (VBC)

def get_vbc_pyqs():
    pyqs = [
        # 1-15: Carbohydrate Metabolism & Ruminant Gluconeogenesis
        ("The principal rate-limiting and committed enzyme of glycolysis in animal tissues is:",
         ["Phosphofructokinase-1 (PFK-1)", "Hexokinase", "Pyruvate kinase", "Glyceraldehyde-3-phosphate dehydrogenase"],
         0, "PFK-1 catalyzes the irreversible phosphorylation of Fructose-6-phosphate to Fructose-1,6-bisphosphate. It is allosterically activated by AMP and Fructose-2,6-bisphosphate, and inhibited by ATP and citrate."),

        ("In ruminants, what is the single most important volatile fatty acid (VFA) that serves as the major precursor for endogenous gluconeogenesis?",
         ["Propionate (Propionic acid)", "Acetate", "Butyrate", "Isovalerate"],
         0, "Propionate is the only major glucogenic VFA produced in the rumen, supplying up to 60-80% of the total glucose requirements of the ruminant through hepatic gluconeogenesis."),

        ("The enzymatic conversion of Propionyl-CoA to Methylmalonyl-CoA in ruminant liver requires which vitamin as an essential cofactor?",
         ["Biotin (Vitamin B7)", "Thiamine (Vitamin B1)", "Pyridoxine (Vitamin B6)", "Cobalamin (Vitamin B12)"],
         0, "Propionyl-CoA carboxylase is an ATP-dependent biotin-containing enzyme that fixes CO2 onto propionyl-CoA to form D-methylmalonyl-CoA."),

        ("The conversion of L-Methylmalonyl-CoA to Succinyl-CoA (which enters the TCA cycle for gluconeogenesis) is catalyzed by Methylmalonyl-CoA mutase, which strictly requires:",
         ["Vitamin B12 (Deoxyadenosylcobalamin)", "Folic acid (Tetrahydrofolate)", "Ascorbic acid", "Riboflavin (FAD)"],
         0, "Methylmalonyl-CoA mutase utilizes deoxyadenosylcobalamin (active coenzyme form of Vitamin B12). Cobalt deficiency in ruminants impairs this enzyme, producing severe emaciation and hypoglycemia ('Pine disease')."),

        ("Which enzyme of gluconeogenesis is located exclusively inside the mitochondrial matrix and requires biotin and acetyl-CoA as an obligatory allosteric activator?",
         ["Pyruvate carboxylase", "Phosphoenolpyruvate carboxykinase (PEPCK)", "Fructose-1,6-bisphosphatase", "Glucose-6-phosphatase"],
         0, "Pyruvate carboxylase carboxylates pyruvate to oxaloacetate inside mitochondria; it is completely inactive without its allosteric activator, Acetyl-CoA."),

        ("Glucose-6-phosphatase, the terminal enzyme of gluconeogenesis and glycogenolysis that releases free glucose into blood, is present in:",
         ["Liver and renal tubular cortex, but absent in skeletal muscle", "Skeletal muscle and heart only", "Adipose tissue and brain", "RBCs and platelets"],
         0, "Skeletal muscle lacks Glucose-6-phosphatase; hence, muscle glycogen cannot contribute directly to blood glucose, but can only be utilized internally or converted to lactate (Cori cycle)."),

        ("The Pyruvate Dehydrogenase (PDH) multi-enzyme complex requires which five coenzymes for its catalytic cycle?",
         ["TPP, Lipoic acid, Coenzyme A, FAD, and NAD+", "Biotin, Cobalamin, THF, PLP, and NADP+", "Ascorbate, Carnitine, CoQ, FAD, and ATP", "PLP, Biotin, TPP, FMN, and NADH"],
         0, "PDH complex consists of E1 (pyruvate decarboxylase: TPP), E2 (dihydrolipoyl transacetylase: Lipoamide & CoA-SH), and E3 (dihydrolipoyl dehydrogenase: FAD & NAD+)."),

        ("Which intermediate of the Citric Acid (TCA) cycle is utilized for the synthesis of heme?",
         ["Succinyl-CoA", "Alpha-ketoglutarate", "Oxaloacetate", "Citrate"],
         0, "Succinyl-CoA condenses with Glycine in the rate-limiting step of porphyrin/heme biosynthesis, catalyzed by ALA synthase in the presence of Pyridoxal phosphate (PLP)."),

        ("The only substrate-level phosphorylation reaction occurring in the Citric Acid Cycle is catalyzed by:",
         ["Succinyl-CoA synthetase (Succinate thiokinase)", "Isocitrate dehydrogenase", "Succinate dehydrogenase", "Malate dehydrogenase"],
         0, "Succinyl-CoA synthetase cleaves the high-energy thioester bond of Succinyl-CoA to produce Succinate and GTP (which transfers its high-energy phosphate to ADP via nucleoside diphosphate kinase)."),

        ("Succinate dehydrogenase, the only TCA cycle enzyme embedded in the inner mitochondrial membrane (forming Complex II of the ETC), is competitively inhibited by:",
         ["Malonate", "Fluoroacetate", "Rotenone", "Cyanide"],
         0, "Malonate is a structural analog of succinate with three carbons (-OOC-CH2-COO-) and competitively inhibits succinate dehydrogenase."),

        ("The rate-limiting and committed enzyme of the Pentose Phosphate Pathway (Hexose Monophosphate Shunt) is:",
         ["Glucose-6-phosphate dehydrogenase (G6PD)", "6-Phosphogluconate dehydrogenase", "Transketolase", "Transaldolase"],
         0, "G6PD catalyzes the irreversible oxidation of Glucose-6-phosphate to 6-Phosphoglucono-delta-lactone with the generation of NADPH."),

        ("The essential metabolic role of NADPH generated by the HMP shunt in erythrocytes is to:",
         ["Maintain Glutathione in its reduced state (GSH) via Glutathione reductase to detoxify H2O2", "Provide ATP for Na+/K+ ATPase", "Synthesize glycogen", "Phosphorylate hemoglobin"],
         0, "NADPH is utilized by Glutathione reductase to reduce oxidized glutathione (GSSG) to GSH, which in turn acts as a substrate for Glutathione peroxidase to neutralize lipid hydroperoxides and H2O2."),

        ("Transketolase, an important enzyme in the non-oxidative reversible phase of the HMP shunt, requires which coenzyme?",
         ["Thiamine pyrophosphate (TPP)", "Pyridoxal phosphate (PLP)", "Biotin", "Niacin"],
         0, "Transketolase transfers 2-carbon ketol groups from xylulose-5-P to ribose-5-P and strictly requires TPP. Erythrocyte transketolase activity is a standard clinical assay for Thiamine (B1) status."),

        ("Domestic animals (cattle, sheep, dogs, cats, horses, pigs) can synthesize ascorbic acid (Vitamin C) from glucose, whereas guinea pigs and primates cannot, because the latter lack which enzyme?",
         ["L-Gulonolactone oxidase", "UDP-glucose dehydrogenase", "L-Gulonate dehydrogenase", "Aldonolactonase"],
         0, "L-Gulonolactone oxidase catalyzes the final step in ascorbic acid synthesis from L-gulonolactone. Mutations in its gene render guinea pigs, fruit bats, and primates dependent on dietary Vitamin C."),

        ("Glycogen phosphorylase, the key enzyme of glycogen breakdown, requires which cofactor tightly bound to each subunit?",
         ["Pyridoxal-5'-phosphate (PLP / Vitamin B6)", "Thiamine pyrophosphate", "Flavin adenine dinucleotide", "Cobalamin"],
         0, "Unlike other PLP-dependent enzymes which act on amino acids via Schiff base intermediates, glycogen phosphorylase uses the phosphate group of PLP as an acid-base catalyst for phosphorolysis."),

        # 16-30: Lipid Metabolism, Beta-Oxidation & Ketogenesis
        ("Long-chain fatty acyl-CoA molecules are transported across the inner mitochondrial membrane for beta-oxidation via the:",
         ["Carnitine shuttle system (CPT-I, Carnitine-acylcarnitine translocase, and CPT-II)", "Citrate-malate shuttle", "Glycerol-3-phosphate shuttle", "Malate-aspartate shuttle"],
         0, "Carnitine palmitoyltransferase-1 (CPT-I) on the outer mitochondrial membrane conjugates acyl-CoA to carnitine; translocase shuttles it across, and CPT-II on the inner face reconstitutes fatty acyl-CoA."),

        ("The primary allosteric inhibitor of Carnitine Palmitoyltransferase-I (CPT-I), preventing simultaneous fatty acid oxidation during de novo lipogenesis, is:",
         ["Malonyl-CoA", "Citrate", "Acetyl-CoA", "Acetoacetyl-CoA"],
         0, "Malonyl-CoA (synthesized by Acetyl-CoA carboxylase in the cytoplasm) potently inhibits CPT-I, ensuring newly synthesized fatty acids are not immediately transported into mitochondria for oxidation."),

        ("The complete beta-oxidation of one molecule of Palmitic acid (16:0) yields how many net moles of ATP (assuming P/O ratios of 2.5 for NADH and 1.5 for FADH2)?",
         ["106 ATP (108 produced minus 2 used for activation)", "129 ATP", "96 ATP", "36 ATP"],
         0, "7 rounds of beta-oxidation yield 7 FADH2 (10.5 ATP), 7 NADH (17.5 ATP), and 8 Acetyl-CoA (80 ATP) = 108 ATP. Subtracting 2 ATP equivalents for fatty acid activation yields 106 net ATP."),

        ("The rate-limiting enzyme of ketogenesis occurring in the mitochondrial matrix of hepatocytes is:",
         ["HMG-CoA synthase (mitochondrial)", "HMG-CoA reductase", "Thiolase", "Acetoacetate decarboxylase"],
         0, "Mitochondrial HMG-CoA synthase condenses acetoacetyl-CoA with acetyl-CoA to form 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA), the committed step of ketogenesis."),

        ("Which ketone body does NOT react in the Rothera’s nitroprusside test commonly used for detecting clinical ketosis in bovine milk and urine?",
         ["Beta-hydroxybutyrate", "Acetoacetate", "Acetone", "Both acetoacetate and acetone"],
         0, "Rothera's test utilizes sodium nitroprusside in alkaline conditions, which reacts with the keto group of Acetoacetate and Acetone, but does NOT react with Beta-hydroxybutyrate (which lacks a ketone group)."),

        ("Why can the liver NOT utilize ketone bodies as an energy source, despite being the sole organ producing them?",
         ["The liver lacks the enzyme Thiophorase (Beta-ketoacyl-CoA transferase / SCOT)", "The liver lacks HMG-CoA lyase", "The liver cannot transport ketone bodies", "The liver lacks thiolase"],
         0, "The liver lacks succinyl-CoA:3-ketoacid CoA transferase (thiophorase/SCOT), which transfers CoA from succinyl-CoA to acetoacetate; hence, ketone bodies are exported to extrahepatic tissues."),

        ("Bovine Ketosis (Acetonemia) in high-yielding dairy cows during early lactation is primarily triggered by:",
         ["Negative energy balance leading to depletion of oxaloacetate for gluconeogenesis and overflow of acetyl-CoA into ketogenesis", "Excessive carbohydrate intake", "Insulin hypersecretion", "Inadequate dietary protein"],
         0, "High milk yield demands massive amounts of glucose for lactose synthesis. Oxaloacetate is siphoned into gluconeogenesis, leaving insufficient OAA to condense with Acetyl-CoA from lipolysis, driving ketogenesis."),

        ("The committed and rate-limiting enzyme of de novo fatty acid synthesis in the cytoplasm is:",
         ["Acetyl-CoA carboxylase (ACC)", "Fatty acid synthase (FAS)", "ATP-citrate lyase", "Malonyl transacylase"],
         0, "Acetyl-CoA carboxylase (ACC) is a biotin-dependent enzyme that carboxylates acetyl-CoA to malonyl-CoA; it is allosterically activated by citrate and inhibited by palmitoyl-CoA."),

        ("The multi-enzyme Fatty Acid Synthase (FAS) complex in mammalian and avian tissues carries the growing fatty acyl chain attached to the phosphopantetheine group of:",
         ["Acyl Carrier Protein (ACP)", "Enoyl reductase", "Ketoacyl synthase", "Thioesterase"],
         0, "The 4'-phosphopantetheine prosthetic group of ACP acts as a flexible 2 nm long 'swinging arm' transferring the acyl intermediates between consecutive catalytic centers of the FAS complex."),

        ("The primary biological donor of reducing equivalents (NADPH) for de novo fatty acid biosynthesis in the cytosol is:",
         ["Malic enzyme and the HMP shunt (G6PD / 6-PGD)", "Glycolysis (GAPDH)", "TCA cycle", "Beta-oxidation"],
         0, "Cytosolic NADPH for lipogenesis is derived primarily from the Pentose Phosphate Pathway (G6PD and 6-PGD) and the Malic enzyme (NADP+-dependent malate dehydrogenase)."),

        ("The rate-limiting enzyme of cholesterol biosynthesis, targeted pharmacologically by statins, is:",
         ["HMG-CoA reductase (microsomal / ER)", "HMG-CoA synthase", "Squalene synthase", "7-alpha-hydroxylase"],
         0, "HMG-CoA reductase in the endoplasmic reticulum reduces HMG-CoA to Mevalonate using 2 molecules of NADPH; it is feedback-inhibited by cholesterol and competitively inhibited by statins."),

        ("Which lipoprotein is responsible for 'Reverse Cholesterol Transport', transporting excess cholesterol from peripheral tissues back to the liver for excretion in bile?",
         ["High-Density Lipoprotein (HDL)", "Low-Density Lipoprotein (LDL)", "Very-Low-Density Lipoprotein (VLDL)", "Chylomicrons"],
         0, "HDL (containing ApoA-I) acquires free cholesterol from peripheral cell membranes, esterifies it via Lecithin-Cholesterol Acyltransferase (LCAT), and transports it back to the liver."),

        ("The apolipoprotein that acts as an essential cofactor for Lipoprotein Lipase (LPL) on capillary endothelial surfaces, promoting clearance of triglycerides from chylomicrons and VLDL, is:",
         ["ApoC-II", "ApoB-100", "ApoA-I", "ApoE"],
         0, "ApoC-II on chylomicrons and VLDL activates endothelial Lipoprotein Lipase (LPL), hydrolyzing core triglycerides into free fatty acids and glycerol."),

        ("Which apolipoprotein is exclusively synthesized in the intestinal enterocytes and is essential for the assembly and secretion of chylomicrons?",
         ["ApoB-48", "ApoB-100", "ApoE", "ApoA-IV"],
         0, "ApoB-48 represents the N-terminal 48% of the ApoB gene transcript generated by post-transcriptional RNA editing (cytidine deaminase C->U conversion creating a stop codon UAA in intestinal mRNA)."),

        ("Brown adipose tissue produces non-shivering thermogenesis in newborn lambs and calves through the action of:",
         ["Thermogenin (Uncoupling Protein-1 / UCP-1)", "ATP synthase activation", "Inhibition of complex IV", "Rapid fatty acid synthesis"],
         0, "UCP-1 (Thermogenin) dissipates the proton gradient across the inner mitochondrial membrane, allowing protons to re-enter the matrix without generating ATP, releasing energy purely as heat."),

        # 31-45: Protein, Amino Acids & Urea Cycle
        ("All aminotransferases (transaminases) require which coenzyme derived from Vitamin B6?",
         ["Pyridoxal-5'-phosphate (PLP)", "Thiamine pyrophosphate (TPP)", "Flavin mononucleotide (FMN)", "Tetrahydrofolate (THF)"],
         0, "PLP forms a covalent Schiff base with the epsilon-amino group of a lysine residue in the active site and acts as a reversible transient carrier of amino groups (converting to pyridoxamine phosphate)."),

        ("Which two amino acids do NOT undergo transamination in animal tissues and must be catabolized by direct deamination or other pathways?",
         ["Lysine and Threonine", "Alanine and Aspartate", "Glutamate and Glutamine", "Leucine and Isoleucine"],
         0, "Lysine and threonine do not participate in transamination; lysine is degraded via the saccharopine pathway and threonine is metabolized by threonine dehydratase or threonine aldolase."),

        ("The oxidative deamination of L-glutamate to alpha-ketoglutarate and free ammonia in the mitochondrial matrix is catalyzed by:",
         ["Glutamate dehydrogenase (GDH)", "Aspartate aminotransferase", "Glutaminase", "Glutamine synthetase"],
         0, "Glutamate dehydrogenase (GDH) is an allosteric mitochondrial enzyme unusual in its ability to utilize either NAD+ (for oxidative deamination) or NADP+ (for reductive amination)."),

        ("The primary rate-limiting and committed enzyme of the Urea Cycle in mammalian hepatocytes is:",
         ["Carbamoyl Phosphate Synthetase I (CPS-I)", "Ornithine transcarbamylase (OTC)", "Argininosuccinate synthetase", "Arginase"],
         0, "CPS-I is located in the mitochondrial matrix and condenses NH4+ and HCO3- with 2 ATP to form carbamoyl phosphate; it has an absolute requirement for N-acetylglutamate (NAG) as an allosteric activator."),

        ("The obligatory allosteric activator of Carbamoyl Phosphate Synthetase I (CPS-I) in the urea cycle is:",
         ["N-Acetylglutamate (NAG)", "Acetyl-CoA", "Citrate", "Arginine"],
         0, "N-Acetylglutamate (NAG) is synthesized from acetyl-CoA and glutamate by NAG synthase (which itself is allosterically activated by arginine, signaling high amino acid abundance)."),

        ("In the Urea Cycle, the two nitrogen atoms present in the urea molecule are derived directly from:",
         ["One from free Ammonia (NH4+) and one from Aspartate", "Both from free Ammonia", "Both from Glutamine", "One from Alanine and one from Glycine"],
         0, "One nitrogen enters as free ammonium ion (via CPS-I in mitochondria) and the second nitrogen enters as the amino group of Aspartate (via Argininosuccinate synthetase in the cytosol)."),

        ("The net energetic cost for the synthesis of one molecule of urea in the urea cycle is:",
         ["4 high-energy phosphate bonds (equivalent to 4 ATP hydrolyzed to 2 ADP + 2 Pi and 1 AMP + PPi)", "2 ATP", "1 ATP", "6 ATP"],
         0, "CPS-I consumes 2 ATP (yielding 2 ADP + 2 Pi) and Argininosuccinate synthetase consumes 1 ATP (cleaved to AMP + PPi; subsequent pyrophosphatase hydrolysis yields 2 high-energy bonds). Total cost = 4 ATP equivalents."),

        ("Why do birds and terrestrial reptiles excrete nitrogen primarily as Uric acid (uricotelism) rather than Urea (ureotelism)?",
         ["They lack functional carbamoyl phosphate synthetase I and arginase in their liver, conserving water by precipitating semisolid uric acid", "They lack kidneys", "They do not consume protein", "Urea is too non-toxic for egg incubation"],
         0, "Uricotelic animals lack a functional hepatic urea cycle; excreting uric acid requires only 1-3 ml of water per gram of nitrogen compared to 40-50 ml for urea, conserving water inside cleidoic eggs."),

        ("Which amino acid serves as the common precursor for the biosynthesis of the neurotransmitters Dopamine, Norepinephrine, and Epinephrine?",
         ["L-Tyrosine (derived from Phenylalanine)", "L-Tryptophan", "L-Histidine", "L-Arginine"],
         0, "Phenylalanine is hydroxylated to Tyrosine by PAH; Tyrosine is converted to DOPA by tyrosine hydroxylase, followed by decarboxylation to dopamine and subsequent hydroxylation to norepinephrine and epinephrine."),

        ("The primary metabolic defect in Classical Phenylketonuria (PKU) is an inherited deficiency of:",
         ["Phenylalanine hydroxylase (PAH) or its cofactor Tetrahydrobiopterin (BH4)", "Tyrosinase", "Homogentisate oxidase", "Branched-chain alpha-keto acid dehydrogenase"],
         0, "Deficiency of hepatic phenylalanine hydroxylase (PAH) or BH4 regeneration prevents the conversion of Phe to Tyr, causing toxic accumulation of phenylalanine and phenylketones (phenylpyruvate, phenyllactate)."),

        ("The genetic condition 'Alkaptonuria' (characterized by urine turning dark black on exposure to air and alkapton deposition in cartilage) is caused by deficiency of:",
         ["Homogentisate 1,2-dioxygenase (Homogentisic acid oxidase)", "Fumarylacetoacetate hydrolase", "Tyrosine transaminase", "DOPA decarboxylase"],
         0, "Homogentisate accumulates in tissues and is oxidized to benzoquinone acetic acid polymers that deposit in connective tissues (ochronosis) and darken urine upon standing or alkalinization."),

        ("Maple Syrup Urine Disease (MSUD) in calves and human infants is caused by an enzymatic defect in:",
         ["Branched-Chain Alpha-Keto Acid Dehydrogenase (BCKDH) complex", "Pyruvate dehydrogenase", "Alpha-ketoglutarate dehydrogenase", "Propionyl-CoA carboxylase"],
         0, "Deficiency of mitochondrial BCKDH leads to the accumulation of branched-chain amino acids (Leucine, Isoleucine, Valine) and their corresponding alpha-keto acids, producing a sweet burnt-sugar odor in urine and encephalopathy."),

        ("Which amino acid is the direct precursor for the synthesis of the inhibitory neurotransmitter GABA (Gamma-Aminobutyric Acid)?",
         ["L-Glutamate (via Glutamate decarboxylase requiring PLP)", "L-Glycine", "L-Aspartate", "L-Serine"],
         0, "Glutamate decarboxylase (GAD), a PLP-dependent enzyme, removes the alpha-carboxyl group of L-glutamate to generate the major central inhibitory neurotransmitter GABA."),

        ("S-Adenosylmethionine (SAM), the 'universal methyl donor' in biochemical methylation reactions (e.g. epinephrine synthesis, DNA methylation), is generated from:",
         ["L-Methionine and ATP", "L-Cysteine and GTP", "L-Serine and THF", "Choline and betaine"],
         0, "Methionine adenosyltransferase (MAT) condenses ATP and methionine, transferring the adenosyl group to methionine sulfur to form the highly reactive sulfonium intermediate SAM."),

        ("Creatine, the precursor of high-energy phosphocreatine in skeletal muscle, is synthesized in a multi-organ pathway involving which three amino acids?",
         ["Glycine, Arginine, and Methionine (as SAM)", "Alanine, Valine, and Leucine", "Lysine, Proline, and Glutamate", "Histidine, Cysteine, and Tryptophan"],
         0, "Guanidinoacetate is formed in the kidney from Arginine and Glycine (via AGAT); it is transported to the liver and methylated by SAM (via GAMT) to produce Creatine."),

        # 46-60: Nucleic Acid Metabolism & Molecular Genetics
        ("In de novo purine nucleotide biosynthesis, the purine ring is assembled directly on a pre-existing molecule of:",
         ["5-Phosphoribosyl-1-pyrophosphate (PRPP)", "Ribulose-5-phosphate", "Glucose-6-phosphate", "Deoxyribose-5-phosphate"],
         0, "Purine synthesis builds the bicyclic ring atom-by-atom directly onto PRPP, beginning with PRPP amidotransferase (the committed rate-limiting step inhibited by IMP, AMP, and GMP)."),

        ("The pharmacological agent 'Allopurinol' used in managing hyperuricemia and gout acts as a suicide/mechanism-based inhibitor of which enzyme?",
         ["Xanthine oxidase", "Hypoxanthine-guanine phosphoribosyltransferase (HGPRT)", "Adenosine deaminase", "Ribonucleotide reductase"],
         0, "Allopurinol is oxidized by Xanthine oxidase to oxypurinol (alloxanthine), which remains tightly bound to the molybdenum center of xanthine oxidase, irreversibly inactivating the enzyme."),

        ("The enzyme 'Ribonucleotide Reductase' (which reduces ribonucleotides to deoxyribonucleotides for DNA replication) acts at the level of:",
         ["Ribonucleoside diphosphates (NDPs -> dNDPs)", "Ribonucleoside monophosphates (NMPs -> dNMPs)", "Ribonucleoside triphosphates (NTPs -> dNTPs)", "Free nitrogenous bases"],
         0, "Ribonucleotide reductase (RNR) reduces ribonucleoside diphosphates (ADP, GDP, CDP, UDP) into dADP, dGDP, dCDP, and dUDP; it requires reduced thioredoxin or glutaredoxin."),

        ("Which DNA polymerase in Escherichia coli is primarily responsible for the continuous leading strand and discontinuous lagging strand replication?",
         ["DNA Polymerase III", "DNA Polymerase I", "DNA Polymerase II", "DNA Polymerase IV"],
         0, "DNA Pol III holoenzyme has high processivity (due to the beta-clamp) and high catalytic rate, serving as the main replicative enzyme in E. coli."),

        ("The 5' to 3' exonuclease activity (essential for RNA primer removal and DNA repair during replication) in E. coli is uniquely present in:",
         ["DNA Polymerase I", "DNA Polymerase III", "DNA Polymerase II", "DNA Ligase"],
         0, "Only DNA Polymerase I possesses 5'->3' exonuclease activity (nick translation) enabling it to excise ribonucleotide primers and replace them with deoxyribonucleotides."),

        ("In prokaryotic transcription, the 'sigma factor' of RNA polymerase holoenzyme is required specifically for:",
         ["Specific promoter recognition and initiation of transcription", "Elongation of RNA transcript", "Rho-dependent termination", "Proofreading excision of misincorporated NTPs"],
         0, "The core RNA polymerase (alpha-2, beta, beta', omega) possesses catalytic activity, but requires the sigma factor to recognize the -10 (Pribnow box) and -35 promoter consensus sequences."),

        ("Which eukaryotic RNA polymerase is responsible for the synthesis of messenger RNA (mRNA) and is specifically inhibited by low concentrations of alpha-amanitin (from death cap mushroom)?",
         ["RNA Polymerase II", "RNA Polymerase I", "RNA Polymerase III", "Mitochondrial RNA polymerase"],
         0, "RNA Pol II synthesizes pre-mRNA and most snRNAs, and is exquisitely sensitive to alpha-amanitin; RNA Pol I (rRNA) is insensitive, and Pol III (tRNA, 5S rRNA) is moderately sensitive."),

        ("The post-transcriptional '5'-capping' of eukaryotic mRNA consists of which unique chemical modification?",
         ["7-Methylguanosine attached via an unusual 5'-to-5' triphosphate bridge", "Polyadenylic acid tail", "Pseudouridine substitution", "Inosine insertion"],
         0, "The 5' cap (m7GpppN) is added cotranscriptionally by guanylyltransferase and guanine-7-methyltransferase, protecting mRNA from 5' exonucleolytic degradation and facilitating ribosome binding."),

        ("The 'Wobble Hypothesis' proposed by Francis Crick states that non-Watson-Crick base pairing can occur between the:",
         ["3' base of the mRNA codon and the 5' base of the tRNA anticodon", "5' base of the codon and 3' base of the anticodon", "Middle base of both codon and anticodon", "Any position randomly"],
         0, "Conformational flexibility at the 5' wobble position of the tRNA anticodon allows it to pair with multiple alternative bases at the 3' position of the mRNA codon (e.g. Inosine can pair with U, C, or A)."),

        ("Which of the following codons functions as both the universal 'Start Codon' for translation and codes for Methionine?",
         ["AUG", "UAA", "UAG", "UGA"],
         0, "AUG specifies Methionine (N-formylmethionine in prokaryotes/mitochondria) and serves as the initiator codon recognized by the initiator tRNA."),

        ("The three universal 'Stop / Nonsense Codons' that signal the termination of translation in the standard genetic code are:",
         ["UAA (ochre), UAG (amber), and UGA (opal)", "AUG, GUG, and CUG", "UAA, UGG, and UGA", "AAA, UAA, and CAA"],
         0, "UAA, UAG, and UGA do not code for any amino acid and are recognized by peptide release factors (RF1, RF2 in prokaryotes; eRF1 in eukaryotes), triggering peptidyl-tRNA hydrolysis."),

        ("The peptidyl transferase activity that catalyzes peptide bond formation during ribosomal translation is mediated by:",
         ["A catalytic ribozyme (23S rRNA in prokaryotes / 28S rRNA in eukaryotes)", "Ribosomal protein L27", "Elongation Factor G (EF-G)", "Aminoacyl-tRNA synthetase"],
         0, "Peptidyl transferase is not a protein enzyme but a catalytic ribozyme embedded within the peptidyl transferase center of the large ribosomal subunit RNA."),

        ("In molecular biology, 'Type II Restriction Endonucleases' are invaluable tools for recombinant DNA cloning because they:",
         ["Recognize specific symmetrical (palindromic) nucleotide sequences and cleave DNA at precise positions without requiring ATP", "Cleave randomly far from their recognition site", "Require ATP for cleavage", "Degrade single-stranded RNA"],
         0, "Type II restriction enzymes (e.g. EcoRI, HindIII, BamHI) cleave within or adjacent to palindromic 4-8 bp recognition sites, producing defined sticky or blunt ends without ATP dependence."),

        ("In the Polymerase Chain Reaction (PCR), the optimum temperature typically used for the extension step with Taq DNA polymerase is:",
         ["72°C", "94°C", "55°C", "37°C"],
         0, "Standard PCR cycle involves: Denaturation (94-95°C), Primer Annealing (50-60°C), and Extension (72°C), which is the optimum catalytic temperature for thermophilic Thermus aquaticus (Taq) polymerase."),

        ("The blotting technique used specifically for the detection and sizing of specific RNA sequences using labeled DNA/RNA probes is known as:",
         ["Northern blotting", "Southern blotting", "Western blotting", "Eastern blotting"],
         0, "Southern blot is for DNA, Northern blot is for RNA, Western blot is for proteins (using antibodies), and Eastern blot is for post-translational modifications."),

        # 61-75: Enzyme Kinetics, Bioenergetics & ETC
        ("In Michaelis-Menten enzyme kinetics, the Michaelis constant (Km) is defined as:",
         ["The substrate concentration [S] at which the reaction velocity is half of Vmax", "The maximum velocity of the reaction", "The turnover number (kcat)", "The dissociation constant of the inhibitor"],
         0, "Km has units of concentration (mM or µM) and equals the substrate concentration needed to achieve 1/2 Vmax; a lower Km indicates higher enzyme affinity for the substrate."),

        ("In a Lineweaver-Burk (double reciprocal) plot of 1/v versus 1/[S], the intercept on the y-axis equals:",
         ["1 / Vmax", "-1 / Km", "Km / Vmax", "Vmax / Km"],
         0, "In the linear Lineweaver-Burk equation (1/v = (Km/Vmax)(1/[S]) + 1/Vmax), the y-intercept is 1/Vmax and the x-intercept is -1/Km."),

        ("A classic 'Competitive Inhibitor' of an enzyme produces which characteristic change in kinetic parameters?",
         ["Increases Km (decreases apparent affinity) while Vmax remains unchanged", "Decreases Vmax while Km remains unchanged", "Decreases both Km and Vmax in equal proportion", "Increases both Km and Vmax"],
         0, "A competitive inhibitor competes with the substrate for the free active site; high substrate concentrations outcompete the inhibitor, so Vmax is reachable but higher [S] is required (Km increases)."),

        ("A 'Non-Competitive Inhibitor' binds to both the free enzyme and enzyme-substrate complex at an allosteric site, producing which kinetic effect?",
         ["Decreases Vmax while Km remains unchanged", "Increases Km while Vmax remains unchanged", "Decreases both Km and Vmax", "Increases Vmax and decreases Km"],
         0, "Because the inhibitor does not interfere with substrate binding, Km remains unaffected; however, it reduces the catalytic efficiency of the enzyme, lowering Vmax."),

        ("Which complex of the mitochondrial Electron Transport Chain does NOT pump protons across the inner mitochondrial membrane into the intermembrane space?",
         ["Complex II (Succinate-CoQ oxidoreductase)", "Complex I (NADH-CoQ oxidoreductase)", "Complex III (CoQ-cytochrome c oxidoreductase)", "Complex IV (Cytochrome c oxidase)"],
         0, "Complexes I, III, and IV pump protons (4 H+, 4 H+, and 2 H+ per pair of electrons respectively). Complex II (succinate dehydrogenase) transfers electrons from succinate to CoQ without proton pumping."),

        ("Complex IV (Cytochrome c oxidase) contains which two essential redox metal prosthetic groups?",
         ["Heme iron (cytochromes a and a3) and Copper ions (CuA and CuB)", "Heme iron and Magnesium", "Flavin and Zinc", "Iron-sulfur clusters only"],
         0, "Cytochrome c oxidase contains two heme groups (heme a and heme a3) and two copper centers (CuA and CuB) that transfer 4 electrons to molecular O2 to form two H2O molecules."),

        ("The deadly poison 'Cyanide' (CN-) and Carbon Monoxide (CO) inhibit cellular respiration by binding specifically to:",
         ["The ferric (Fe3+) and ferrous (Fe2+) iron of Cytochrome a-a3 in Complex IV", "Coenzyme Q", "Complex I NADH dehydrogenase", "ATP synthase F1 head"],
         0, "Cyanide binds tightly to the ferric iron (Fe3+) of cytochrome a3 in Complex IV, halting the entire electron transport chain and aerobic ATP generation within seconds."),

        ("The antibiotic 'Oligomycin' inhibits mitochondrial oxidative phosphorylation by specifically blocking:",
         ["The F0 proton channel of ATP Synthase (Complex V)", "Complex I electron transport", "Complex III cytochrome b", "Adenine nucleotide translocase (ANT)"],
         0, "Oligomycin binds the c-subunit ring of the F0 domain of ATP synthase, blocking proton translocation back into the matrix and arresting ATP synthesis."),

        ("Chemical uncouplers of oxidative phosphorylation (such as 2,4-Dinitrophenol / 2,4-DNP) cause:",
         ["Continued electron transport and oxygen consumption without ATP synthesis, releasing energy as heat", "Complete arrest of electron transport", "Stimulation of ATP synthesis", "Inhibition of TCA cycle enzymes"],
         0, "Uncouplers are lipophilic weak acids that carry protons across the inner mitochondrial membrane, collapsing the proton motive force; electron transport runs at maximum speed but all energy is lost as heat."),

        ("According to the Chemiosmotic Hypothesis of Peter Mitchell, ATP synthesis by Complex V is directly driven by:",
         ["The proton-motive force (electrochemical proton gradient across the inner mitochondrial membrane)", "Substrate-level phosphorylation of ADP", "Direct conformational coupling with Complex IV", "High mitochondrial matrix calcium levels"],
         0, "Protons pumped into the intermembrane space by Complexes I, III, and IV generate a transmembrane pH gradient and membrane electrical potential (proton-motive force) that drives the rotary catalytic motor of ATP synthase."),

        # 76-90: Clinical Diagnostic Biochemistry & Organ Function Tests
        ("In dogs and cats, which serum enzyme is the most specific indicator of acute hepatocellular injury/necrosis?",
         ["Alanine Aminotransferase (ALT / SGPT)", "Aspartate Aminotransferase (AST / SGOT)", "Alkaline Phosphatase (ALP)", "Creatine Kinase (CK)"],
         0, "ALT is primarily localized in the cytoplasm of canine and feline hepatocytes; leakage into serum occurs rapidly with altered membrane permeability or hepatocellular necrosis."),

        ("Why is serum ALT NOT a useful diagnostic marker for hepatocellular necrosis in horses, cattle, and sheep?",
         ["Large animal hepatocytes contain very low basal activity of ALT, rendering it non-diagnostic", "Large animal serum degrades ALT rapidly", "Large animals lack the ALT gene", "ALT is bound to albumin in large animals"],
         0, "In ruminants and equines, hepatocellular ALT activity is negligible; Sorbitol Dehydrogenase (SDH) and Glutamate Dehydrogenase (GLDH) are used instead as liver-specific leakage markers."),

        ("The most sensitive and liver-specific serum enzyme for detecting acute hepatocellular necrosis in horses and cattle is:",
         ["Sorbitol Dehydrogenase (SDH / Iditol Dehydrogenase)", "Alanine Aminotransferase (ALT)", "Alkaline Phosphatase (ALP)", "Lipase"],
         0, "SDH is highly liver-specific in all domestic species, particularly horses and cattle where ALT is useless; its short serum half-life (<12-24 h) makes it an excellent indicator of active/ongoing liver necrosis."),

        ("Gamma-Glutamyltransferase (GGT) is a membrane-bound brush-border enzyme whose marked elevation in serum is primarily indicative of:",
         ["Cholestasis, biliary hyperplasia, and bile duct obstruction", "Skeletal muscle trauma", "Pancreatitis", "Glomerulonephritis"],
         0, "GGT is located on the canalicular and ductular epithelial membranes of hepatocytes; cholestasis induces GGT synthesis and bile salt solubilization releases it into serum."),

        ("In newborn calves, puppies, and kittens, high serum activity of GGT is clinically utilized as a definitive marker of:",
         ["Adequate passive transfer of colostral immunoglobulins", "Congenital liver disease", "Bile duct atresia", "Rickets"],
         0, "Maternal colostrum contains extremely high concentrations of GGT (up to several thousand times serum levels); absorption of colostral GGT parallels IgG uptake through neonatal enterocytes."),

        ("The 'Corticosteroid-induced Isoenzyme of Alkaline Phosphatase' (C-ALP) is unique to which domestic animal species?",
         ["Dog (Canine)", "Cat", "Horse", "Cow"],
         0, "Dogs uniquely possess a specific alkaline phosphatase isoenzyme (C-ALP) induced by endogenous or exogenous glucocorticoids (e.g. Cushing's syndrome or prednisone therapy)."),

        ("The most sensitive, specific, and gold-standard biomarker for evaluating acute skeletal muscle necrosis (e.g. exertional rhabdomyolysis / tying-up in horses, capture myopathy, white muscle disease) is:",
         ["Creatine Kinase (CK)", "Alkaline Phosphatase (ALP)", "Amylase", "Lipase"],
         0, "Creatine Kinase (specifically CK-MM cytosolic isoenzyme) is exceptionally specific for striated muscle; injury triggers massive release into blood within 1-6 hours."),

        ("Cardiac Troponin I (cTnI) is the diagnostic biomarker of choice in veterinary medicine for detecting:",
         ["Myocardial injury, necrosis, or active myocarditis", "Hepatic cirrhosis", "Pancreatic insufficiency", "Renal tubular necrosis"],
         0, "Cardiac Troponin I (cTnI) is structural and exclusively expressed in cardiomyocytes; its elevation in blood indicates irreversible myocardial membrane disruption or necrosis."),

        ("The serum creatinine concentration is widely used to assess the Glomerular Filtration Rate (GFR) because:",
         ["It is produced at a constant rate from muscle creatine and phosphocreatine, freely filtered by the glomerulus, and neither significantly reabsorbed nor secreted", "It is actively secreted by proximal tubules", "It reflects dietary carbohydrate intake", "It is synthesized by the liver proportionally to protein intake"],
         0, "Creatinine is an end-product of muscle phosphocreatine breakdown; since daily production is steady and renal excretion is purely glomerular without tubular reabsorption, serum creatinine inversely mirrors GFR."),

        ("The 'Anion Gap' in clinical blood gas analysis is calculated using which formula?",
         ["[Na+ + K+] - [Cl- + HCO3-]", "[Na+ + Cl-] - [K+ + HCO3-]", "[Na+ + HCO3-] - [Cl- + K+]", "[Cl- + HCO3-] - [Na+ + K+]"],
         0, "The serum anion gap represents unmeasured anions (proteins, organic acids like lactate and ketones, sulfates, phosphates); normal reference range in dogs/cats is 12-24 mEq/L."),

        # 91-100: Vitamins, Minerals & Trace Element Deficiencies
        ("The visual pigment Rhodopsin present in retinal rod cells consists of the apoprotein Opsin covalently bound to:",
         ["11-cis-retinal", "All-trans-retinal", "Retinoic acid", "Beta-carotene"],
         0, "11-cis-retinal is covalently attached to a lysine residue of opsin. Absorption of a photon causes photoisomerization of 11-cis-retinal to all-trans-retinal, triggering the visual phototransduction cascade."),

        ("The active hormonal form of Vitamin D synthesized in the proximal convoluted tubules of the kidney by 1-alpha-hydroxylase is:",
         ["1,25-Dihydroxycholecalciferol [Calcitriol / 1,25-(OH)2-D3]", "25-Hydroxycholecalciferol [Calcidiol]", "7-Dehydrocholesterol", "Ergocalciferol"],
         0, "Liver 25-hydroxylase produces 25-(OH)-D3 (circulating storage form); renal 1-alpha-hydroxylase (activated by PTH and inhibited by FGF-23 and hyperphosphatemia) converts it to active 1,25-(OH)2-D3."),

        ("Vitamin E (alpha-tocopherol) and Selenium act synergistically in biological membranes because:",
         ["Vitamin E breaks peroxyl free radical chain reactions in lipid bilayers while Selenium is an essential component of cytosolic Glutathione Peroxidase", "Vitamin E oxidizes selenium", "Selenium synthesizes Vitamin E in vivo", "Both chelate calcium ions"],
         0, "Alpha-tocopherol intercepts lipid peroxyl radicals (LOO•) preventing propagation of lipid peroxidation, while selenium-dependent Glutathione Peroxidase (containing selenocysteine) reduces toxic H2O2 and lipid peroxides to harmless alcohols."),

        ("Sweet clover poisoning (dicoumarol toxicosis) and warfarin rodenticide poisoning in animals produce severe coagulopathies by inhibiting:",
         ["Vitamin K epoxide reductase (VKOR)", "Thrombin directly", "Fibrinogen synthesis", "Factor VIII activation"],
         0, "Dicoumarol and warfarin competitively inhibit VKOR and quinone reductase, preventing regeneration of hydroquinone (active Vitamin K) required for post-translational gamma-carboxylation of clotting factors II, VII, IX, and X."),

        ("'Polioencephalomalacia' (PEM / Cerebrocortical necrosis) in ruminants is clinically caused by a functional deficiency of:",
         ["Thiamine (Vitamin B1) or excess dietary sulfur", "Cobalamin (Vitamin B12)", "Riboflavin (Vitamin B2)", "Niacin"],
         0, "Thiamine deficiency (secondary to high ruminal bacterial thiaminases, amprolium toxicity, or high sulfur intake generating H2S) starves brain astrocytes and neurons of ATP by crippling PDH and alpha-KGDH."),

        ("'Curled-toe paralysis' in growing broiler chicks is pathognomonic for dietary deficiency of:",
         ["Riboflavin (Vitamin B2)", "Thiamine (Vitamin B1)", "Pyridoxine (Vitamin B6)", "Pantothenic acid"],
         0, "Riboflavin deficiency produces sciatic and brachial nerve myelin sheath degeneration and Schwann cell proliferation, causing flexor spasms and characteristic inward curling of toes."),

        ("'Black tongue' in dogs and pellagra in humans and pigs are classic deficiency syndromes of:",
         ["Niacin (Nicotinic acid / Vitamin B3) or its precursor Tryptophan", "Biotin", "Ascorbic acid", "Folic acid"],
         0, "Niacin is required for NAD+ and NADP+ synthesis. In dogs, deficiency produces severe necrotic ulceration of the tongue mucosa, foul-smelling drooling, and enteritis ('canine black tongue')."),

        ("'Grass Tetany' (Hypomagnesemic tetany) in lactating cattle grazing lush green spring pastures is precipitated primarily by:",
         ["Low blood magnesium levels caused by high dietary Potassium (K+) and Nitrogen interfering with ruminal magnesium absorption", "Hypocalcemia alone", "Vitamin D toxicity", "Hyperphosphatemia"],
         0, "Lush pastures are rich in potassium and nitrogen; high ruminal K+ depolarizes the apical membrane of ruminal epithelium, impairing active magnesium transport via potential-dependent Mg channels."),

        ("'Enzootic Ataxia' and 'Swayback' in newborn and young lambs characterized by demyelination of the spinal cord and cerebral white matter is caused by deficiency of:",
         ["Copper (Cu)", "Zinc (Zn)", "Manganese (Mn)", "Iron (Fe)"],
         0, "Copper is an essential component of Cytochrome c oxidase (required for myelin maintenance) and lysyl oxidase; secondary Cu deficiency is exacerbated by high dietary molybdenum and sulfur (forming insoluble tetrathiomolybdates)."),

        ("'Parakeratosis' in swine, characterized by non-inflammatory hyperkeratinized crusty skin lesions on limbs and snout, is caused by deficiency of which trace mineral?",
         ["Zinc (Zn)", "Selenium (Se)", "Iron (Fe)", "Cobalt (Co)"],
         0, "Zinc is a catalytic cofactor for alkaline phosphatase, carbonic anhydrase, and DNA/RNA polymerases. High dietary Calcium (excess limestone) or phytates bind Zinc in the intestine, precipitating severe parakeratosis."),

        # 91-100: Additional High-Yield PYQs
        ("The enzyme responsible for the conversion of Glucose to Sorbitol in the polyol pathway (implicated in diabetic cataractogenesis) is:",
         ["Aldose Reductase (utilizing NADPH)", "Sorbitol dehydrogenase", "Hexokinase", "Glucose-6-phosphatase"],
         0, "In sustained hyperglycemia, aldose reductase converts excess glucose to sorbitol; sorbitol cannot readily diffuse out of lens fibers, generating hyperosmotic swelling and cataractous opacification."),

        ("In iron transport and metabolism, which plasma beta-1 globulin is responsible for transporting ferric iron (Fe3+) in systemic circulation?",
         ["Transferrin", "Ferritin", "Hemosiderin", "Ceruloplasmin"],
         0, "Apotransferrin binds two atoms of ferric iron (Fe3+) with high affinity to form Transferrin, delivering iron to proliferating cells via receptor-mediated endocytosis."),

        ("The primary storage form of iron in hepatocytes, splenic macrophages, and bone marrow is:",
         ["Ferritin", "Transferrin", "Hemoglobin", "Myoglobin"],
         0, "Ferritin consists of a hollow spherical shell of 24 apoferritin subunits surrounding an internal crystalline core of up to 4500 ferric iron atoms (hydrated ferric oxide-phosphate)."),

        ("The rate-limiting and committed enzyme of porphyrin and heme biosynthesis in hepatocytes is:",
         ["Delta-Aminolevulinic Acid Synthase (ALA Synthase / ALAS-1)", "ALA Dehydratase", "Porphobilinogen deaminase", "Ferrochelatase"],
         0, "ALAS-1 is located in the mitochondrial matrix, condenses Succinyl-CoA and Glycine in the presence of PLP, and is tightly feedback-regulated by free intracellular heme."),

        ("Which amino acid is the primary precursor for the synthesis of Thyroid hormones (T3 and T4) within thyroglobulin in thyroid follicles?",
         ["L-Tyrosine", "L-Tryptophan", "L-Phenylalanine", "L-Histidine"],
         0, "Thyroid peroxidase (TPO) oxidizes iodide (I-) and iodinates tyrosyl residues in thyroglobulin to form MIT and DIT, which couple to synthesize Triiodothyronine (T3) and Thyroxine (T4)."),

        ("The intracellular secondary messenger cyclic AMP (cAMP) is degraded and inactivated into 5'-AMP by which enzyme?",
         ["Phosphodiesterase (PDE)", "Adenylate cyclase", "Protein kinase A (PKA)", "Phospholipase C (PLC)"],
         0, "Phosphodiesterases hydrolyze the 3',5'-cyclic phosphate bond of cAMP to form inactive 5'-AMP; methylxanthines (theobromine, caffeine, theophylline) competitively inhibit PDE, prolonging cAMP signaling."),

        ("Which trace element is an essential catalytic component of the enzyme Glutathione Peroxidase (GSH-Px)?",
         ["Selenium (Se, as Selenocysteine)", "Zinc (Zn)", "Copper (Cu)", "Manganese (Mn)"],
         0, "Glutathione peroxidase incorporates selenocysteine (the 21st amino acid encoded by the UGA codon with a SECIS element) into its active catalytic site to reduce harmful hydroperoxides."),

        ("The remethylation of Homocysteine to Methionine in animal tissues requires which two vitamins acting cooperatively?",
         ["Vitamin B12 (Methylcobalamin) and Folic Acid (N5-methyl-THF)", "Vitamin B6 and Biotin", "Vitamin C and Niacin", "Vitamin B1 and Riboflavin"],
         0, "Methionine synthase transfers a methyl group from N5-methyl-tetrahydrofolate to Cobalamin (forming methylcobalamin), which subsequently methylates homocysteine to regenerate methionine."),

        ("In collagen biosynthesis, the post-translational hydroxylation of Proline and Lysine residues strictly requires:",
         ["Ascorbic Acid (Vitamin C), Ferrous iron (Fe2+), and Alpha-ketoglutarate", "Vitamin D and Calcium", "Vitamin A and Zinc", "Vitamin E and Selenium"],
         0, "Prolyl and lysyl hydroxylases maintain Fe2+ in the reduced state using Ascorbic acid; without Vitamin C, unstable non-hydroxylated collagen triple helices fail to cross-link (scurvy)."),

        ("In small animal veterinary practice, marked elevations of serum Amylase and Lipase along with elevated Spec cPL (canine pancreatic lipase immunoreactivity) are diagnostic for:",
         ["Acute Pancreatitis", "Exocrine Pancreatic Insufficiency (EPI)", "Bile duct obstruction", "Renal failure only"],
         0, "Acute pancreatitis in dogs triggers premature intra-acinar zymogen activation, causing autodigestion of pancreatic parenchyma and massive leakage of pancreatic lipase and amylase into circulation.")
    ]

    final_list = []
    for idx, item in enumerate(pyqs[:100]):
        final_list.append({
            "id": f"pyq_vbc_{idx+1:03d}",
            "domain": "animal_science",
            "year": "2nd_year",
            "subjectId": "vbc",
            "topic": "Veterinary Biochemistry (ICAR PG PYQ)",
            "questionText": item[0],
            "options": item[1],
            "correctOptionIndex": item[2],
            "explanation": item[3],
            "difficulty": "Hard",
            "tags": ["ICAR PG PYQ", "Biochemistry", "High-Yield PYQ"],
            "createdAt": 1774000200000 + idx
        })
    return final_list

if __name__ == "__main__":
    qs = get_vbc_pyqs()
    print(f"Loaded {len(qs)} Veterinary Biochemistry PYQ questions.")
