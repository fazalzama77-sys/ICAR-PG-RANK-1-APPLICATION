# scripts/micro_mod2_virology.py
# Module 2: Systematic Virology (80 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module2_questions():
    qs = [
        # 1-10: Picornaviridae (FMD) & Paramyxoviridae (PPR, NDV)
        ("Foot and Mouth Disease Virus (FMDV) belongs to the genus Aphthovirus (family Picornaviridae) and exists globally as how many distinct immunological serotypes with no cross-protection?",
         ["7 serotypes: O, A, C, SAT 1, SAT 2, SAT 3, and Asia 1", "3 serotypes: 1, 2, and 3", "5 serotypes", "12 serotypes"],
         0, "FMDV has 7 serotypes: Euro-Asian types (O, A, C, Asia 1) and South African Territories types (SAT 1, SAT 2, SAT 3); immunity against one serotype confers zero cross-protection against the others.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In India, which serotype of Foot and Mouth Disease Virus accounts for the overwhelming majority (>85-90%) of field outbreaks?",
         ["Serotype O (predominantly the Ind2001 lineage)", "Serotype Asia 1", "Serotype A", "Serotype C"],
         0, "Epidemiological surveillance by the ICAR-Directorate on Foot and Mouth Disease confirms that Serotype O is responsible for >85-90% of all confirmed clinical outbreaks in Indian livestock.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Foot and Mouth Disease Virus is distinguished from other animal picornaviruses (such as Swine Vesicular Disease Virus) by its extreme sensitivity to:",
         ["Acidic pH, being rapidly and completely inactivated below pH 6.0", "Ether and chloroform (lipid solvents)", "Freezing at -70°C", "Alkaline pH above 11.0"],
         0, "Aphthoviruses are acid-labile: exposure to pH below 6.5-6.8 leads to rapid dissociation of the 140S intact capsid into 12S pentamers and free RNA, whereas enteroviruses (like SVDV) are stable down to pH 3.0.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The primary cell-surface attachment receptor on host epithelial cells recognized by the conserved Arg-Gly-Asp (RGD) loop on the VP1 capsid protein of FMDV is:",
         ["Integrins (specifically alpha-v beta-6 and alpha-v beta-3)", "Sialic acid residues", "CD46", "Nicotinic acetylcholine receptors"],
         0, "The highly variable VP1 capsid protein of FMDV possesses a flexible, exposed G-H loop containing a conserved RGD motif that binds with high affinity to alpha-v integrins (especially alpha-v beta-6 on epithelial cells).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The primary diagnostic laboratory test recommended by WOAH for differentiating FMD-vaccinated animals from naturally infected animals (DIVA strategy) is the detection of antibodies against:",
         ["Non-Structural Proteins (NSPs, such as 3ABC, 3AB, 3D)", "Structural capsid protein VP1", "Capsid protein VP2", "Capsid protein VP4"],
         0, "Purified inactivated FMD vaccines contain only structural capsid proteins (VP1-4); active viral replication inside infected animals produces non-structural proteins (NSPs: 2C, 3A, 3B, 3ABC, 3D); anti-3ABC antibodies indicate natural infection.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Peste des Petits Ruminants (PPR / 'Goat Plague') is caused by a Morbillivirus (family Paramyxoviridae) and the widely used live attenuated cell-culture vaccine in India is derived from which strain?",
         ["Sungri 96 (PPRV / Sungri / 96)", "Nigeria 75/1", "Kabete 'O'", "Mukteswar strain"],
         0, "In India, the homologous live attenuated PPR vaccine developed by the Indian Veterinary Research Institute (IVRI) is based on the indigenous lineage IV strain Sungri 96, conferring long-lasting protective immunity.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Rinderpest ('Cattle Plague'), a catastrophic morbillivirus disease of artiodactyls, was officially declared globally eradicated by the FAO and WOAH in which historic year?",
         ["2011", "1995", "2001", "2018"],
         0, "Following a coordinated global eradication campaign, the World Organisation for Animal Health (WOAH) and FAO officially declared global freedom from Rinderpest in May-June 2011, making it the first animal disease eradicated.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Newcastle Disease Virus (NDV / Avian Paramyxovirus-1) carries two major surface glycoproteins embedded in its lipid envelope that mediate attachment and penetration:",
         ["Hemagglutinin-Neuraminidase (HN) protein and Fusion (F) protein", "Glycoprotein G and Glycoprotein M", "Spike (S) protein and Hemagglutinin-esterase (HE)", "gp120 and gp41"],
         0, "The HN glycoprotein mediates attachment to sialic acid receptors and has neuraminidase activity to release budding virions; the F glycoprotein mediates viral envelope fusion with the host cell plasma membrane.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The live lentogenic vaccine strain of Newcastle Disease Virus most commonly administered to day-old chicks via eye-drops or drinking water is:",
         ["LaSota or B1 (Hitchner B1) strain", "Mukteswar (R2B) strain", "Komarov strain", "Roakin strain"],
         0, "Hitchner B1 and LaSota are natural lentogenic (low-virulence) NDV strains used globally as mild, safe primary vaccines in young chicks, whereas Mukteswar (R2B) is a mesogenic booster strain used in older birds.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Canine Distemper Virus (CDV), a member of the genus Morbillivirus, causes 'hard pad disease' (hyperkeratosis of footpads and nose) by replicating in:",
         ["Epithelial keratinocytes of the stratum spinosum and basal layer, alongside lymphoid and central nervous system cells", "Osteoblasts of the metaphysis", "Skeletal muscle fibers only", "Erythrocytes"],
         0, "CDV is pantropic: it initially replicates in macrophages and lymphocytes (via CD150/SLAM receptor), then spreads to epithelial tissues throughout the body (via Nectin-4 receptor), producing marked hyperkeratosis of digital footpads.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 11-20: Rhabdoviridae (Rabies) & Poxviridae
        ("Rabies virus (genus Lyssavirus, family Rhabdoviridae) has a characteristic bullet-shaped morphology and contains a single-stranded RNA genome of:",
         ["Negative-sense, unsegmented RNA (-ssRNA)", "Positive-sense, unsegmented RNA (+ssRNA)", "Segmented double-stranded RNA", "Ambisenese circular RNA"],
         0, "Rabies virus virions are bullet-shaped (75 x 180 nm) containing an unsegmented, negative-sense, single-stranded RNA genome (-ssRNA, approximately 12 kb) encoding five structural proteins: N, P, M, G, and L.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The surface glycoprotein G of Rabies virus mediates viral attachment to peripheral host cells by binding with high affinity to which neuronal receptor?",
         ["Nicotinic Acetylcholine Receptor (nAChR) at the neuromuscular junction (and NCAM / p75NTR)", "Dopamine D2 receptor", "Beta-2 adrenergic receptor", "GABA-A receptor"],
         0, "Rabies virus glycoprotein G binds to nicotinic acetylcholine receptors (nAChR) concentrated on post-synaptic muscle membranes at the neuromuscular junction, as well as NCAM and p75NTR on peripheral nerve axons.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Centripetal spread of Rabies virus from the peripheral site of an animal bite to the central nervous system occurs exclusively via:",
         ["Retrograde fast axonal transport within sensory or motor axoplasm at a rate of 50 to 100 mm per day", "Viremia and blood-borne delivery across the blood-brain barrier", "Lymphatic drainage to the thoracic duct", "Direct invasion through cerebrospinal fluid pathways"],
         0, "Rabies virus enters motor or sensory nerve endings and ascends centripetally via retrograde axonal transport within axoplasm at a rate of 12-100 mm/day; the virus is insulated from neutralizing antibodies throughout neural transport.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In rabies diagnostics, the historical distinction between 'Street Virus' and 'Fixed Virus' created by Louis Pasteur is that Fixed Virus:",
         ["Has a shortened, fixed incubation period (4 to 6 days), lacks pathogenicity for dogs by peripheral routes, and fails to produce Negri bodies", "Has a highly variable incubation period (up to months) and produces large Negri bodies", "Is excreted in high titers in saliva", "Can replicate in mosquito cells"],
         0, "Pasteur serially passaged street rabies virus through rabbit brains over 50 times, selecting a 'fixed' neurotropic mutant that kills rabbits in a fixed 4-6 days, produces no Negri bodies, and cannot cause rabies when injected subcutaneously.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The international gold standard diagnostic test recommended by the World Health Organization (WHO) and WOAH for post-mortem confirmation of Rabies in brain tissue is the:",
         ["Direct Fluorescent Antibody Test (dFAT) on fresh impression smears of hippocampus, cerebellum, and medulla", "Enzyme-Linked Immunosorbent Assay (ELISA)", "Histological Seller's staining of formalin-fixed tissue", "Polymerase Chain Reaction (PCR) alone"],
         0, "The direct FAT (dFAT) uses FITC-conjugated polyclonal or monoclonal antibodies against rabies nucleoprotein on fresh, unfixed brain smears (Ammon's horn, cerebellum, brainstem), exhibiting >99% diagnostic sensitivity and specificity.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Poxviruses (family Poxviridae) are biologically exceptional among all animal DNA viruses because they:",
         ["Replicate their large double-stranded DNA genome entirely within the cytoplasm of host cells using their own viral DNA-dependent RNA polymerase", "Replicate within the host cell nucleus and bud through the nuclear envelope", "Possess a single-stranded RNA genome", "Lack an envelope in all forms"],
         0, "Poxviruses are large (300 nm) brick-shaped dsDNA viruses that encode all required transcription and replication enzymes (including viral DNA-dependent RNA polymerase), enabling complete autonomous transcription in the host cell cytoplasm.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Lumpy Skin Disease (LSD) of cattle and water buffaloes is caused by a Capripoxvirus that is primarily transmitted between animals by:",
         ["Hematophagous mechanical insect vectors (such as stable flies Stomoxys calcitrans, mosquitoes, and Rhipicephalus ticks)", "Aerosol droplets across long distances", "Venereal transmission only", "Water-borne ingestion of spores"],
         0, "Capripoxviruses are primarily transmitted mechanically by biting arthropods, including blood-feeding stable flies (Stomoxys calcitrans), mosquitoes (Aedes, Culex), and hard ticks (Rhipicephalus, Amblyomma), with direct contact being inefficient.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Sheeppox and Goatpox are malignant, high-mortality viral diseases of small ruminants characterized by the histological presence of diagnostic 'Sheeppox cells' (cells of Borrel), which are:",
         ["Vacuolated, ballooned dermal histiocytes containing intracytoplasmic eosinophilic inclusion bodies", "Multinucleated syncytia with Cowdry Type A intranuclear inclusions", "Neoplastic T-lymphocytes", "Degenerated mast cells with lost granules"],
         0, "In cutaneous and pulmonary pox lesions in sheep, 'cells of Borrel' (or sheeppox cells) are large, vacuolated, transformed histiocytic macrophages containing pale, round, intracytoplasmic eosinophilic inclusion bodies.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Bovine Papular Stomatitis and Pseudocowpox (milker's nodules) in cattle are caused by members of which genus in the family Poxviridae?",
         ["Parapoxvirus (ovoid virions with a criss-cross spiral filament pattern)", "Orthopoxvirus", "Capripoxvirus", "Avipoxvirus"],
         0, "Parapoxviruses (including Orf virus, Bovine Papular Stomatitis virus, and Pseudocowpox virus) are ovoid, have a surface showing a characteristic criss-cross thread-like coil, and induce proliferative epidermal lesions.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Swinepox Virus, a member of the genus Suipoxvirus, is mechanically transmitted within pig herds primarily by which ectoparasite?",
         ["Haematopinus suis (the hog louse)", "Sarcoptes scabiei var. suis", "Ctenocephalides canis", "Dermanyssus gallinae"],
         0, "The sucking hog louse (Haematopinus suis) is the major mechanical vector of Swinepox virus; eradication of lice from swine facilities effectively halts transmission of swinepox.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 21-30: Herpesviridae & Parvoviridae
        ("A fundamental biological characteristic common to all members of the family Herpesviridae is their ability to establish lifelong:",
         ["Latent infection in host sensory ganglia or lymphoid tissues, with periodic reactivations", "Persistent viremia without antibodies", "Continuous shedding from the liver", "Integration into the host telomere in all cases"],
         0, "Herpesviruses establish lifelong latency following primary infection (e.g. Alphaherpesviruses in sensory ganglia like the trigeminal ganglion; Gammaherpesviruses in lymphocytes), reactivating during periods of corticosteroid release or physiological stress.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Infectious Bovine Rhinotracheitis (IBR) virus (Bovine alphaherpesvirus 1 / BHV-1) establishes lifelong latency primarily within neurons of which anatomical structure?",
         ["Trigeminal ganglion (following respiratory infection) and Sacral ganglion (following genital infection)", "Ventral horn motor neurons of the cervical spinal cord", "Hippocampus", "Dorsal root ganglia of thoracic segments exclusively"],
         0, "BHV-1 ascends sensory axons following nasal or ocular exposure to establish lifelong viral latency as circular episomal DNA within the sensory neurons of the trigeminal ganglion, and within sacral ganglia following venereal IPV infection.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Pseudorabies (Aujeszky's Disease) is caused by Suid alphaherpesvirus 1, in which swine serve as the natural reservoir, but in cattle, dogs, and cats it produces the fatal syndrome known as:",
         ["'Mad Itch' (intense localized pruritus leading to frenzied self-mutilation and acute death)", "Chronic abortion without nervous signs", "Persistent diarrhea with intestinal marbling", "Severe arthritis with joint swelling"],
         0, "In dead-end non-porcine hosts (cattle, dogs, sheep, cats), Suid herpesvirus 1 exhibits virulent neurotropism, causing severe localized pruritus ('mad itch') where animals vigorously rub and chew skin down to the bone, dying within 24-48 hours.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Malignant Catarrhal Fever (MCF) in cattle and deer is an acute fatal lymphoproliferative panvasculitis caused by which gammaherpesviruses transmitted from carrier reservoir hosts?",
         ["Alcelaphine gammaherpesvirus 1 (wildebeest-associated) and Ovine gammaherpesvirus 2 (sheep-associated)", "Bovine herpesvirus 4", "Equine herpesvirus 1", "Gallid herpesvirus 1"],
         0, "MCF is caused by Alcelaphine herpesvirus 1 (wildebeest reservoir in Africa) and Ovine herpesvirus 2 (subclinical infection in domestic sheep worldwide); in cattle, it causes severe adventitial lymphoid vasculitis, bilateral corneal opacity ('white eye'), and erosive stomatitis.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Equine Herpesvirus 1 (EHV-1) causes 'abortion storms' in mares and Equine Herpesvirus Myeloencephalopathy (EHM), with the neurotropic strain linked to a specific point mutation in the:",
         ["DNA polymerase gene (ORF30, substitution N752D)", "Glycoprotein B gene", "Thymidine kinase gene", "Major capsid protein gene"],
         0, "A single nucleotide substitution (A2254G) in the viral DNA polymerase catalytic subunit gene (ORF30), resulting in an asparagine (N) to aspartic acid (D) substitution at amino acid position 752, increases viremia levels and EHM risk.",
         False, "Systematic Virology"),

        ("Canine Parvovirus Type 2 (CPV-2) and Feline Panleukopenia Virus (FPV) contain which type of nucleic acid genome?",
         ["Non-enveloped, negative-sense single-stranded linear DNA (-ssDNA)", "Enveloped double-stranded circular DNA", "Non-enveloped double-stranded segmented RNA", "Positive-sense single-stranded RNA"],
         0, "Parvoviruses are among the smallest animal viruses (~20-25 nm), consisting of an icosahedral non-enveloped capsid enclosing a single-stranded linear DNA genome of ~5 kb, requiring host cellular replication machinery in S-phase.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Canine Parvovirus-2 (CPV-2) emerged in 1978 as a host-range variant derived from Feline Panleukopenia Virus (FPV) through mutations in which viral structural protein?",
         ["VP2 capsid protein (the major capsid protein)", "VP1 unique region", "Non-structural protein NS1", "Non-structural protein NS2"],
         0, "The host-range switch of FPV to CPV-2 was determined by only a few key amino acid substitutions (Lys93Asn and Asp323Asn) on the surface of the VP2 capsid protein, allowing the virus to bind canine transferrin receptor (TfR).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Canine Parvovirus variants currently circulating globally (CPV-2a, CPV-2b, and CPV-2c) are classified based on the specific amino acid present at residue 426 of the VP2 protein, which is:",
         ["Asparagine in 2a, Aspartic acid in 2b, and Glutamic acid in 2c", "Alanine in 2a, Valine in 2b, Leucine in 2c", "Glycine in all", "Serine in 2a, Threonine in 2b, Proline in 2c"],
         0, "Residue 426 of VP2 sits at the apex of the threefold capsid spike: CPV-2a has Asn426, CPV-2b has Asp426, and CPV-2c has Glu426, altering antigenicity without changing clinical signs.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("A rapid, reliable bedside diagnostic test for confirming acute Canine Parvovirus in fecal samples based on viral erythrocyte agglutination is the:",
         ["Hemagglutination (HA) test using porcine or rhesus monkey erythrocytes at 4°C", "Milk ring test", "CAMP test", "Agar gel immunodiffusion"],
         0, "CPV-2 capsids agglutinate porcine and rhesus red blood cells at 4°C and neutral pH (6.8-7.2); fecal HA and fecal antigen ELISA are rapid, highly sensitive diagnostic field tests.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In young pups under 6 to 8 weeks of age infected in utero or during the neonatal period, Canine Parvovirus-2 can replicate in rapidly dividing cardiomyocytes, producing sudden death due to:",
         ["Acute non-suppurative necrotizing myocarditis with basophilic intranuclear inclusion bodies", "Severe vegetative valvular endocarditis", "Aortic dissection", "Acute fibrinous pericarditis"],
         0, "In neonatal pups, cardiomyocytes are actively dividing (unlike adult hearts); CPV-2 infection destroys cardiomyocytes, causing acute cardiac collapse and pulmonary edema with basophilic intranuclear inclusions.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 31-40: Retroviridae & Flaviviridae
        ("Retroviruses (family Retroviridae) are unique among animal RNA viruses because they replicate via a DNA intermediate catalyzed by the viral enzyme:",
         ["Reverse Transcriptase (RNA-dependent DNA polymerase with RNase H activity)", "DNA-dependent RNA polymerase", "RNA-dependent RNA polymerase", "Terminal deoxynucleotidyl transferase"],
         0, "Retroviruses package two copies of positive-sense ssRNA; upon entering the cell, viral Reverse Transcriptase synthesizes a complementary minus-strand DNA and hydrolyzes viral RNA (RNase H), synthesizing double-stranded proviral DNA that integrates into host chromosomes.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In horses, the official international gold standard serological test for Equine Infectious Anemia (EIA) required for racehorse certification is the:",
         ["Coggins Test (Agar Gel Immunodiffusion / AGID detecting antibodies against the p26 capsid protein)", "Western blot for gp120", "Serum neutralization test", "Latex agglutination"],
         0, "Developed by Dr. Leroy Coggins in 1970, the Coggins AGID test detects precipitating antibodies against the major internal group-specific structural core protein (p26) of EIA Lentivirus, exhibiting near 100% specificity.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Bovine Leukemia Virus (BLV) is classified in the genus Deltaretrovirus and is unique among oncogenic retroviruses because it induces B-cell lymphosarcoma in cattle without:",
         ["Carrying a viral oncogene (v-onc) and without insertional mutagenesis near a proto-oncogene (instead using Tax protein transactivation)", "Infecting white blood cells", "Producing any antibodies", "Integrating into host DNA"],
         0, "BLV lacks a viral oncogene; instead, its Tax regulatory protein transactivates cellular transcription factors (NF-kappaB), induces genomic instability, and downregulates p53 and DNA repair mechanisms, causing monoclonal B-cell transformation.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Feline Leukemia Virus (FeLV) and Feline Immunodeficiency Virus (FIV) belong to which respective genera of the family Retroviridae?",
         ["Gammaretrovirus (FeLV) and Lentivirus (FIV)", "Alpharetrovirus (FeLV) and Betaretrovirus (FIV)", "Deltaretrovirus (FeLV) and Spumavirus (FIV)", "Lentivirus for both"],
         0, "FeLV is a Gammaretrovirus causing lymphosarcoma, non-regenerative anemia, and myelosuppression, whereas FIV is a Lentivirus (feline AIDS) causing progressive depletion of CD4+ T-helper cells.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Jaagsiekte Sheep Retrovirus (JSRV), a Betaretrovirus, causes Ovine Pulmonary Adenocarcinoma (Jaagsiekte), in which neoplastic transformation of Type II pneumocytes is directly driven by the:",
         ["Viral envelope (Env) glycoprotein acting directly as an active oncoprotein", "Tax protein", "Reverse transcriptase", "Matrix protein"],
         0, "JSRV is unique in that its structural envelope (Env) glycoprotein itself functions as a dominant viral oncoprotein, activating the Akt/mTOR and MAPK/ERK oncogenic signaling cascades upon binding to host hyaluronidase-2 (HYAL2) receptors.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Classical Swine Fever Virus (CSFV / Hog Cholera) belongs to which viral genus and family?",
         ["Pestivirus (family Flaviviridae)", "Asfavirus (family Asfarviridae)", "Arterivirus (family Arteriviridae)", "Circovirus (family Circoviridae)"],
         0, "CSFV is an enveloped positive-sense single-stranded RNA virus belonging to the genus Pestivirus within the family Flaviviridae (closely related to Bovine Viral Diarrhea Virus and Border Disease Virus).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Bovine Viral Diarrhea Virus (BVDV) exists in two distinct biotypes in cell culture, termed Cytopathic (CP) and Non-Cytopathic (NCP), which are differentiated by:",
         ["Induction of vacuolation and lysis of cultured bovine cell monolayers (CP) versus absence of visible cytopathic effect (NCP)", "Genome size differences of 10-fold", "Different capsid symmetries", "Sensitivity to pasteurization"],
         0, "NCP BVDV replicates without causing observable morphological changes in cell cultures; CP BVDV arises by genomic insertion or recombination (expressing free NS3 / p80 serine protease), causing marked cell rounding, vacuolation, and lysis.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In pregnant cows infected with non-cytopathic BVDV between 40 and 120 days of gestation (prior to fetal immunocompetence), the newborn calf characteristically emerges as:",
         ["An immunotolerant, Persistently Infected (PI) calf that is seronegative for antibodies but continuously sheds massive amounts of BVDV for life", "A healthy calf with high protective antibody titers", "A mummified fetus in 100% of cases", "An animal permanently immune to all pestiviruses"],
         0, "Infection before fetal thymic development causes the fetal immune system to recognize the ncp BVDV antigens as 'self'; the surviving calf is born persistently infected (PI), lacks antibodies to that strain, and sheds billions of virions throughout its life.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Border Disease in sheep ('Hairy Shaker Disease' / 'Fuzzy Lamb Disease') is caused by an ovine pestivirus that produces:",
         ["Excessive birth coat hairiness (halo hairs), rhythmic muscle tremors due to hypomyelinogenesis, and skeletal defects in newborn lambs", "Acute bloody diarrhea with 100% mortality in adult ewes", "Purulent mastitis only", "Severe wool discoloration to green"],
         0, "In utero Border Disease virus infection destroys thyroid development and hair follicle primary growth (producing kemp-like 'hairy' fleece) and impairs oligodendrocyte myelin synthesis in the spinal cord, causing persistent tremors ('shakers').",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("West Nile Virus (WNV) is a mosquito-borne flavivirus maintained in an enzootic cycle between birds and ornithophilic Culex mosquitoes, in which horses and humans serve as:",
         ["Dead-end (incidental) hosts that develop clinical encephalomyelitis but do not develop viremia high enough to re-infect mosquitoes", "Primary reservoir hosts amplifying the virus", "The sole definitive hosts", "Mechanical tick-borne vectors"],
         0, "Horses and humans develop acute neurological disease following WNV infection, but their peripheral viremia is transient and low-titer (<10^5 PFU/mL), insufficient to infect biting Culex mosquitoes, making them dead-end hosts.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 41-50: Asfarviridae, Reoviridae, Birnaviridae
        ("African Swine Fever Virus (ASFV) is of immense taxonomic significance in virology because it is the only known virus that is both:",
         ["A large double-stranded DNA arbovirus (transmitted by arthropod vectors) and the sole member of the family Asfarviridae", "A retrovirus that infects ticks", "A circular single-stranded RNA virus", "An insect poxvirus"],
         0, "ASFV is the only known DNA arbovirus: a large (200 nm) enveloped icosahedral double-stranded DNA virus belonging to the nucleocytoplasmic large DNA virus (NCLDV) group and the sole representative of the family Asfarviridae.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The primary biological soft tick vector responsible for maintaining African Swine Fever Virus in the sylvatic cycle in warthogs and soft tick burrows is:",
         ["Ornithodoros moubata (and Ornithodoros erraticus)", "Rhipicephalus appendiculatus", "Ixodes ricinus", "Argas persicus"],
         0, "Soft ticks of the genus Ornithodoros (O. moubata complex in sub-Saharan Africa and O. erraticus in the Mediterranean basin) are the natural biological vectors and reservoirs of ASFV, where the virus replicates and undergoes transovarial and transstadial transmission.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("African Swine Fever Virus replicates predominantly in cells of which host lineage, causing massive cytokine storm and apoptosis of uninfected lymphocytes?",
         ["Monocytes and tissue Macrophages", "B-lymphocytes directly", "CD8+ T-cells directly", "Vascular smooth muscle cells"],
         0, "ASFV infects monocytes and macrophages via receptor-mediated endocytosis, triggering massive dysregulated secretion of pro-inflammatory cytokines (TNF-alpha, IL-1, IL-6), inducing bystander apoptosis of uninfected lymphocytes and severe lymphopenia.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Bluetongue Virus (BTV), a major arboviral pathogen of sheep and ruminants (genus Orbivirus, family Reoviridae), possesses a genome consisting of:",
         ["10 segments of double-stranded RNA (dsRNA)", "7 segments of single-stranded RNA", "A single linear double-stranded DNA", "12 segments of positive-sense RNA"],
         0, "Orbiviruses contain a non-enveloped multi-layered icosahedral capsid enclosing 10 discrete double-stranded RNA (dsRNA) segments (designated VP1 through VP7 and NS1 through NS4).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The biological transmission of Bluetongue Virus between ruminants in field outbreaks is exclusively mediated by the bites of infected:",
         ["Culicoides biting midges ('no-see-ums' / punkies)", "Simulium blackflies", "Stomoxys stable flies", "Tabanus horseflies"],
         0, "Bluetongue is non-contagious between animals by direct contact; it is transmitted biologically by adult female biting midges of the genus Culicoides (e.g. C. oxystoma, C. imicola, C. sonorensis), where the virus replicates in salivary glands.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The pathognomonic clinical sign giving 'Bluetongue' its name is cyanosis of the tongue in sheep, which is caused by:",
         ["Endothelial cell infection leading to microvascular thrombosis, ischemia, and venous congestion of the oral mucosa and tongue", "Direct bacterial toxin production", "Severe methemoglobinemia from plant poisoning", "Hypertrophy of lingual papillae"],
         0, "BTV replicates primarily in vascular endothelial cells and mononuclear phagocytes; microvascular injury leads to thrombosis, hemorrhage, localized tissue ischemia, and severe cyanosis of the tongue and coronary band ('coronitis').",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("African Horse Sickness Virus (AHSV), causing devastating mortality (>90%) in horses, is closely related to Bluetongue Virus and also belongs to the genus:",
         ["Orbivirus (family Reoviridae)", "Aphthovirus", "Flavivirus", "Rhabdovirus"],
         0, "AHSV is an Orbivirus with 10 dsRNA segments, transmitted by Culicoides biting midges, producing four clinical forms: pulmonary (dunkop, acute fatal pulmonary edema), cardiac (dikkop, head/neck edema), mixed, and horse sickness fever.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Infectious Bursal Disease Virus (IBDV / Gumboro) belongs to the family Birnaviridae and possesses which unique genomic structure?",
         ["Bi-segmented double-stranded RNA (Segment A and Segment B)", "Tri-segmented negative-sense RNA", "Single-stranded linear DNA", "10 segments of double-stranded RNA"],
         0, "Birnaviruses possess a non-enveloped icosahedral capsid containing two segments of double-stranded RNA: Segment A (3.2 kb, encoding VP2-VP4-VP3 polyprotein and VP5) and Segment B (2.8 kb, encoding the VP1 RNA-dependent RNA polymerase).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The primary host-protective neutralizing epitope of Infectious Bursal Disease Virus (IBDV) resides within the hypervariable region of which structural protein?",
         ["VP2 capsid protein (specifically loops Pbc and Pde between amino acids 206 and 350)", "VP3 internal protein", "VP4 protease", "VP1 polymerase"],
         0, "VP2 is the major structural capsid protein; its outer hypervariable domain (HVR, residues 206-350) contains the critical conformational neutralizing epitopes; point mutations in this region allow antigenic drift and give rise to 'very virulent' (vvIBDV) strains.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Infectious Bursal Disease Virus strains that broke through maternal antibody immunity in vaccinated flocks in Europe and Asia starting in the late 1980s are designated as:",
         ["Very Virulent IBDV (vvIBDV)", "Classical virulent strains", "Variant A strains", "Lentogenic strains"],
         0, "vvIBDV strains (such as European strain UK661) exhibit high mortality (up to 60-70% in layers) and can penetrate high levels of maternally derived neutralizing antibodies, characterized by specific signature amino acid residues in the VP2 HVR.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 51-60: Coronaviridae, Circoviridae, Arteriviridae
        ("Coronaviruses (family Coronaviridae) are enveloped positive-sense single-stranded RNA viruses characterized on negative-stain electron microscopy by:",
         ["Large, club-shaped or petal-shaped surface peplomers (Spike glycoproteins) forming a solar corona or halo appearance", "A smooth spherical non-enveloped surface", "A bullet-shaped envelope", "Brick-shaped complex outer coat"],
         0, "Coronaviruses derive their name from the Latin 'corona' (crown), referring to the prominent 20-nm bulbous, club-shaped homotrimeric Spike (S) glycoprotein projections radiating from their spherical lipid envelope under electron microscopy.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In cats, Feline Infectious Peritonitis (FIP) arises in individual cats not through direct horizontal transmission of FIP virus, but via:",
         ["Spontaneous internal mutation of ubiquitous enteric Feline Coronavirus (FECV) within an infected cat, acquiring tropism for monocytes and macrophages", "Direct bite transmission from wild felids", "Contaminated drinking water containing viral cysts", "Inhalation of fungal spores"],
         0, "FIP is an immune-mediated disease caused when relatively harmless feline enteric coronavirus (FECV) mutates in vivo (mutations in 3c and S genes), enabling high-affinity replication inside monocytes and systemic pyogranulomatous vasculitis.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Porcine Epidemic Diarrhea Virus (PEDV) and Transmissible Gastroenteritis Virus (TGEV) are swine enteropathogenic coronaviruses that cause watery diarrhea in neonatal piglets by destroying:",
         ["Villus absorptive enterocytes of the small intestine, leading to marked villus atrophy and osmotic malabsorption", "Gastric parietal cells", "Pancreatic beta cells", "Colonic goblet cells exclusively"],
         0, "PEDV and TGEV infect mature enterocytes on jejunal and ileal villi, causing rapid cell lysis, villus blunting (villus:crypt ratio drops from 7:1 down to 1:1), loss of digestive enzymes (lactase), and severe fatal dehydration in piglets <10 days.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Porcine Circovirus Type 2 (PCV2), the causative agent of Postweaning Multisystemic Wasting Syndrome (PMWS), belongs to the family Circoviridae, which represents the:",
         ["Smallest autonomously replicating DNA viruses in animals, containing a circular single-stranded DNA (ssDNA) genome of only 1.7 kb", "Largest known animal viruses", "Only retroviruses affecting pigs", "Only segmented DNA viruses"],
         0, "Circoviruses are minuscule (17 nm), non-enveloped, icosahedral virions enclosing an ambisense circular single-stranded DNA genome (~1.76 kb) encoding only two major proteins: Rep (replication-associated protein) and Cap (capsid protein).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The pathognomonic microscopic lesion in lymphoid tissues of weanling pigs with Porcine Circovirus-Associated Disease (PCVAD / PMWS) is:",
         ["Lymphoid depletion with replacement by histiocytes and multinucleated giant cells containing grape-like basophilic intracytoplasmic inclusion bodies", "Severe neutrophilic abscesses in lymphoid follicles", "Extensive caseous necrosis with Langhans cells", "Total absence of histiocytes"],
         0, "PCV2 causes massive depletion of B and T lymphocytes in lymph nodes and spleen, accompanied by intense granulomatous infiltration with multinucleated giant cells containing pathognomonic clusters of globular, botryoid (grape-like) basophilic inclusions.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Porcine Reproductive and Respiratory Syndrome Virus (PRRSV / 'Blue Ear Disease') belongs to which family of positive-sense ssRNA viruses?",
         ["Arteriviridae", "Coronaviridae", "Picornaviridae", "Flaviviridae"],
         0, "PRRSV belongs to the family Arteriviridae (order Nidovirales); it exhibits a selective tropism for porcine alveolar macrophages (PAMs) expressing CD163 and sialoadhesin (CD169), causing reproductive failure in sows and pneumonia in piglets.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Equine Viral Arteritis (EVA) is caused by an Arterivirus that causes acute fever, conjunctivitis, edema of limbs and prepuce, and abortion in mares, with the virus establishing a long-term carrier state in:",
         ["The reproductive tract (ampullae of the vas deferens) of stallions, shed continuously in semen in a testosterone-dependent manner", "The guttural pouches of mares", "The thyroid gland", "The intestinal crypts"],
         0, "Up to 30-70% of stallions infected with EVA virus become chronic asymptomatic carriers that shed the virus in semen for years; the carrier state is strictly testosterone-dependent, and castration eliminates shedding within weeks.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Infectious Bronchitis Virus (IBV) of chickens belongs to which genus within the family Coronaviridae?",
         ["Gammacoronavirus", "Alphacoronavirus", "Betacoronavirus", "Deltacoronavirus"],
         0, "Coronaviruses are classified into 4 genera: Alphacoronavirus and Betacoronavirus (infecting mammals), and Gammacoronavirus and Deltacoronavirus (infecting predominantly avian species; IBV is the prototype Gammacoronavirus).",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Bovine Coronavirus (BCoV) is unique among coronaviruses because it possesses an additional surface spike projection exhibiting hemagglutinating and esterase activity, designated as the:",
         ["Hemagglutinin-Esterase (HE) glycoprotein", "Neuraminidase", "Fusion protein", "Matrix glycoprotein"],
         0, "In addition to the large Spike (S) protein, BCoV (a Betacoronavirus 1) possesses a short, dimeric Hemagglutinin-Esterase (HE) glycoprotein peplomer that binds 9-O-acetylated sialic acids and acts as a receptor-destroying enzyme.",
         False, "Systematic Virology"),

        ("Bovine Respiratory Syncytial Virus (BRSV) belongs to the family Pneumoviridae (genus Orthopneumovirus) and is characterized on cell cultures by forming:",
         ["Large multinucleated syncytia (giant cells) with eosinophilic intracytoplasmic inclusion bodies", "Intranuclear Cowdry Type A inclusions", "Medusa-head colonies", "Complete loss of cell membrane"],
         0, "BRSV expresses an F (fusion) glycoprotein that causes adjacent infected cell membranes to fuse, producing large multinucleated syncytial cells with round, eosinophilic intracytoplasmic inclusions.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 61-70: Orthomyxoviruses & Avian Viral diseases
        ("Influenza A viruses (family Orthomyxoviridae) possess an unsegmented or segmented negative-sense ssRNA genome consisting of:",
         ["8 discrete RNA segments", "10 segments", "12 segments", "A single continuous RNA strand"],
         0, "Influenza A viruses contain 8 negative-sense, single-stranded RNA segments encoding at least 11-12 proteins: PB2, PB1, PA, HA, NP, NA, M1/M2, and NS1/NEP.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("In Avian Influenza epidemiology, 'Antigenic Shift' differs from 'Antigenic Drift' because Antigenic Shift:",
         ["Is a sudden, major genetic reassortment resulting from genetic exchange of complete RNA segments between different influenza subtypes in a co-infected host cell", "Involves minor point mutations in hemagglutinin accumulated over time", "Occurs only in DNA viruses", "Never produces pandemic strains"],
         0, "Because the genome is segmented, co-infection of a single cell by two distinct Influenza A viruses allows reassortment of intact RNA segments (Antigenic Shift), creating novel subtype combinations (e.g. H5N1, H7N9) against which the population has no immunity.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The primary avian reservoir hosts maintaining the global genetic diversity of Influenza A viruses without typically developing clinical disease are:",
         ["Wild aquatic waterfowl (Anseriformes: ducks, geese, swans; and Charadriiformes: gulls, shorebirds)", "Passerine songbirds", "Domestic turkeys", "Commercial broiler chickens"],
         0, "Wild aquatic birds (especially dabbling ducks) are the primordial natural reservoirs for all 16 Hemagglutinin (H1-H16) and 9 Neuraminidase (N1-N9) subtypes of Influenza A viruses, where viruses replicate asymptomatically in the intestinal tract.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("The molecular diagnostic hallmark distinguishing Highly Pathogenic Avian Influenza (HPAI) from Low Pathogenic Avian Influenza (LPAI) strains in poultry is:",
         ["Presence of multiple basic amino acids (arginine and lysine) at the Hemagglutinin cleavage site, permitting cleavage by ubiquitous intracellular furin-like proteases", "Deletion of the M2 ion channel", "Duplication of the neuraminidase stalk", "Loss of the nucleoprotein"],
         0, "LPAI viruses possess a monobasic cleavage site (single arginine) cleaved only by extracellular trypsin-like proteases in respiratory and enteric tracts; HPAI viruses acquire multiple basic amino acids, allowing systemic cleavage by intracellular furin proteases, causing multi-organ endothelial necrosis.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Equine Influenza Virus (EIV), a major cause of contagious acute respiratory coughing and fever in horses, is currently represented globally by which active circulating subtype?",
         ["H3N8 (Florida sublineage clades 1 and 2)", "H7N7 (primate influenza)", "H1N1", "H5N1"],
         0, "While equine H7N7 (Eq/Prague/56) has not been isolated since the late 1970s and is considered extinct, H3N8 (Eq/Miami/63, now diversified into Florida clade 1 and clade 2) remains the sole circulating subtype worldwide.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Swine are historically referred to as 'mixing vessels' for the generation of novel pandemic Influenza A strains because porcine respiratory epithelium uniquely expresses:",
         ["Both alpha-2,3-linked and alpha-2,6-linked sialic acid receptors, allowing co-infection by both avian and human influenza viruses", "Only alpha-2,3 receptors", "Only alpha-2,6 receptors", "No sialic acid receptors"],
         0, "Avian influenza viruses prefer galactose-alpha-2,3-sialic acid receptors, while human influenza viruses prefer galactose-alpha-2,6 receptors. Swine respiratory epithelium expresses both linkages, allowing dual infection and genetic reassortment.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Avian Reoviruses (genus Orthoreovirus, family Reoviridae) are characterized pathologically by producing which disease in broiler chickens?",
         ["Viral Arthritis / Tenosynovitis (swelling of the hock joint and rupture of the gastrocnemius tendon)", "Egg Drop Syndrome", "Visceral gout", "Hydropericardium syndrome"],
         0, "Avian orthoreoviruses have a predilection for synovial tissues and tendon sheaths of the distal legs, producing chronic fibrinous tenosynovitis, marked thickening of the digital flexor and gastrocnemius tendons, and tendon rupture.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        ("Duck Viral Enteritis (Duck Plague) virus is an alphaherpesvirus that can be definitively diagnosed in liver tissue by observing:",
         ["Eosinophilic intranuclear inclusion bodies within degenerating hepatocytes and bile duct epithelial cells", "Large Bollinger bodies in the cytoplasm", "Negri bodies in Kupffer cells", "Absence of any inclusions"],
         0, "Anatid alphaherpesvirus 1 induces multifocal necrotic hepatitis with pathognomonic Cowdry Type A eosinophilic intranuclear inclusion bodies in hepatocytes and cloacal epithelium.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Goose Hemorrhagic Polyomavirus (GHPv) is the etiological agent of 'Hemorrhagic Nephritis and Enteritis of Geese' (HNEG), which is characterized by:",
         ["Sudden high mortality in goslings aged 3 to 10 weeks, severe subcutaneous edema, hemorrhagic nephritis, and enteritis", "Chronic feather loss in adult ganders", "Pure corneal opacity", "Atrophy of the tongue"],
         0, "GHPv (family Polyomaviridae) targets renal tubular and capillary endothelial cells in young geese, causing vascular collapse, massive ascites, subcutaneous edema, acute hemorrhagic nephritis, and death.",
         False, "Systematic Virology"),

        ("Pigeon Paramyxovirus-1 (PPMV-1) is an antigenic and host-adapted variant of:",
         ["Newcastle Disease Virus (Avian Paramyxovirus-1)", "Infectious Bronchitis Virus", "Avian Influenza Virus", "Pigeon Poxvirus"],
         0, "PPMV-1 is an antigenic variant of APMV-1 adapted to columbiform birds (pigeons and doves), capable of causing severe neurotropic disease (torticollis, tremors) in pigeons and spreading to domestic poultry as virulent ND.",
         True, "Systematic Virology (ICAR PG PYQ)"),

        # 71-80: Viral diagnostics, cell culture, serology
        ("The embryonic route of inoculation in 10-to-12-day-old embryonated chicken eggs used specifically for the primary isolation of Poxviruses (producing visible 'pocks') is the:",
         ["Chorioallantoic membrane (CAM)", "Allantoic cavity", "Amniotic cavity", "Yolk sac"],
         0, "Poxviruses are epitheliotropic and proliferate upon the stratified chorioallantoic membrane (CAM); within 48-72 hours, focal, opaque, white-to-gray proliferative inflammatory nodules ('pocks') develop on the dropped CAM.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The allantoic cavity inoculation of 9-to-11-day-old embryonated eggs is the standard method used for propagating which group of animal viruses?",
         ["Newcastle Disease Virus and Influenza A Virus", "Poxviruses", "Avian Encephalomyelitis Virus", "Chlamydia psittaci"],
         0, "Both NDV and Influenza A virus replicate to extraordinarily high titers in the allantoic endodermal cells lining the allantoic sac, shedding billions of virions directly into the clear allantoic fluid, harvested for hemagglutination assays.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In diagnostic virology, continuous cell lines (such as Vero cells, BHK-21 cells, and MDCK cells) differ from primary cell cultures because continuous cell lines:",
         ["Are immortal, possess an abnormal heteroploid karyotype, and can be subcultured indefinitely through hundreds of passages", "Die after 5 to 10 passages", "Have a normal diploid chromosome number", "Can only be derived from chicken embryos"],
         0, "Primary cultures die after limited passages (Hayflick limit); continuous cell lines (e.g. Vero derived from African green monkey kidney, BHK-21 from baby hamster kidney) have undergone genetic transformation, allowing unlimited in vitro serial passage.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The 'Hemadsorption' (HAD) phenomenon is a specialized virological diagnostic technique where red blood cells adhere to the surface of virus-infected cell culture monolayers, pathognomonic for:",
         ["African Swine Fever Virus and Paramyxoviruses (Newcastle Disease / Parainfluenza)", "Parvoviruses", "Herpesviruses", "Adenoviruses"],
         0, "Infected cells express viral hemagglutinins on their plasma membranes prior to cell lysis; adding a suspension of RBCs (e.g. pig RBCs for ASFV, guinea pig RBCs for parainfluenza) results in specific adherence of RBCs around infected cells like rosettes (HAD positive).",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In the Hemagglutination Inhibition (HI) test, the official unit used to express the concentration of viral antigen required to perform the test is:",
         ["4 Hemagglutinating Units (4 HAU)", "1 HAU", "100 HAU", "10 HAU"],
         0, "Standard micro-titer HI assays (e.g. for NDV, Avian Influenza, or Canine Parvovirus) standardize the viral antigen to precisely 4 HA units (4 HAU) per test well to ensure reproducible, quantitative antibody titration.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The 'Plaque Assay' in diagnostic virology is a quantitative technique used to calculate the concentration of infectious viral particles in a sample, expressed as:",
         ["Plaque Forming Units per milliliter (PFU/mL)", "Tissue Culture Infectious Dose 50 (TCID50)", "Hemagglutination titer", "Optical density"],
         0, "Under a solid or semi-solid nutrient agar/carboxymethylcellulose overlay, each infectious virion infects a cell and spreads only to adjacent cells, producing a discrete macroscopic circular zone of cell clearing/lysis termed a 'plaque' (quantified as PFU/mL).",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The 50% Tissue Culture Infectious Dose (TCID50) is statistically calculated from end-point titration dilutions using which standard mathematical formula?",
         ["Reed and Muench method (or Kärber method)", "Lineweaver-Burk equation", "Michaelis-Menten formula", "Henderson-Hasselbalch equation"],
         0, "The Reed and Muench mathematical method (and the Spearman-Kärber method) interpolates the proportionate distance between dilution endpoints above and below 50% cytopathy to determine the precise 50% infective dose (TCID50 or LD50).",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In viral serology, the 'Virus Neutralization Test' (VNT / SNT) is universally regarded as the gold standard functional assay because it:",
         ["Directly measures the biological ability of serum antibodies to bind virions and block viral entry and infectivity in living host cells", "Detects non-neutralizing antibodies against internal nucleoproteins", "Requires only non-viable killed virus", "Is completed within 5 minutes"],
         0, "Unlike binding assays (ELISA, Western blot) that detect non-protective antibodies, the VNT directly measures biologically functional neutralizing antibodies that prevent viral infection of susceptible cell cultures or embryos.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Equine Coital Exanthema is a benign venereal disease of horses characterized by painful papules, vesicles, and ulcers on the external genitalia, caused by:",
         ["Equine alphaherpesvirus 3 (EHV-3)", "Equine alphaherpesvirus 1 (EHV-1)", "Equine arteritis virus", "Equine papillomavirus 2"],
         0, "EHV-3 is an epitheliotropic alphaherpesvirus transmitted venereally or by veterinary equipment, producing localized vesicles that rupture into ulcers on the penis, prepuce, and vulva, healing spontaneously without systemic illness.",
         False, "Systematic Virology"),

        ("Feline Calicivirus (FCV) belongs to the family Caliciviridae (positive-sense ssRNA) and is clinically distinguished from Feline Herpesvirus-1 (FHV-1) in cats with upper respiratory infection because FCV classically produces:",
         ["Prominent, painful, ulcerative stomatitis on the tongue, hard palate, and gingiva", "Severe corneal dendritic ulcers", "Persistent sneezing without mouth lesions", "Biliary cirrhosis"],
         0, "While FHV-1 produces severe rhinotracheitis with pathognomonic branching dendritic corneal ulcers, Feline Calicivirus characteristically targets oral epithelium, producing deep, painful vesicles that ulcerate on the dorsal surface of the tongue and palate.",
         True, "Systematic Virology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module2_questions()
    print(f"Microbiology Module 2 loaded: {len(qs)} questions")
