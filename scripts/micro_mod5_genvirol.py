# scripts/micro_mod5_genvirol.py
# Module 5: General Virology & Viral Diagnostics (25 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module5_questions():
    qs = [
        # 1-10: Baltimore classification, viral structure, replication
        ("In the Baltimore classification of animal viruses, Group IV viruses are defined as possessing a genome of:",
         ["Positive-sense, single-stranded RNA (+ssRNA) that can function directly as mRNA in the host cell cytoplasm", "Negative-sense, single-stranded RNA (-ssRNA)", "Double-stranded segmented RNA", "Retroviral RNA with a DNA intermediate"],
         0, "David Baltimore categorized viruses into 7 groups based on mRNA synthesis pathways; Group IV comprises (+)ssRNA viruses (e.g. Picornaviridae, Flaviviridae, Coronaviridae) whose naked genomic RNA is infectious and immediately translated into viral polyproteins.",
         True, "General Virology (ICAR PG PYQ)"),

        ("Animal viruses with Helical symmetry in their nucleocapsids are unique in that all known animal helical viruses:",
         ["Possess a lipid envelope acquired by budding through host cellular membranes", "Are completely non-enveloped", "Contain double-stranded DNA genomes", "Are strictly non-pathogenic"],
         0, "Unlike plant helical viruses (e.g. Tobacco Mosaic Virus which is naked), all animal viruses with helical symmetry (e.g. Rhabdoviridae, Paramyxoviridae, Orthomyxoviridae, Coronaviridae) are enveloped.",
         True, "General Virology (ICAR PG PYQ)"),

        ("An Icosahedral (cubic) viral capsid possesses precise geometric symmetry characterized by:",
         ["20 equilateral triangular facets and 12 vertices (apices), exhibiting 5:3:2 rotational symmetry", "10 hexagonal facets", "6 square faces", "An irregular spherical geometry without symmetry"],
         0, "The icosahedron is the most efficient closed shell architecture for enclosing viral genomes with minimal repeating protein subunits; it has 20 triangular faces, 12 vertices, and rotational axes of twofold, threefold, and fivefold symmetry.",
         True, "General Virology (ICAR PG PYQ)"),

        ("Negative-sense single-stranded RNA (-ssRNA) viruses (such as Rhabdoviridae and Paramyxoviridae) must package which essential viral enzyme inside their virion?",
         ["RNA-dependent RNA Polymerase (RdRp / Transcriptase)", "Reverse transcriptase", "DNA ligase", "Topoisomerase II"],
         0, "Because host eukaryotic cells lack an RNA-dependent RNA polymerase to transcribe mRNA from a minus-strand RNA template, negative-sense RNA viruses must carry their own preformed RdRp enzyme molecules within the infectious virion.",
         True, "General Virology (ICAR PG PYQ)"),

        ("The phenomenon of 'Phenotypic Mixing' in virology occurs during co-infection of a single cell by two related viruses when:",
         ["Progeny virions contain the genome of one virus packaged within a capsid or envelope composed partly or entirely of proteins from the other virus", "A mutation occurs in the polymerase gene", "Two RNA segments cross over homologous sequences", "A virus loses its envelope permanently"],
         0, "Phenotypic mixing (or transcapsidation/pseudotype formation) involves dual infection where structural proteins intermix during assembly; the viral phenotype (antigenicity, host range) changes temporarily, but the underlying genotype is unchanged upon subsequent replication.",
         False, "General Virology"),

        ("The 'Multiplicity of Infection' (MOI) in experimental virology is defined as the:",
         ["Ratio of the number of infectious viral particles added to the number of target host cells in a culture vessel", "Total number of viral mutations per replication cycle", "Number of days required for plaques to appear", "Dilution factor required to neutralize 50% of virions"],
         0, "MOI is a quantitative laboratory parameter: MOI = (Volume of inoculum x Viral titer in PFU/mL) / Total number of viable cells plated; an MOI of 10 ensures that virtually 100% of cells are infected simultaneously.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("During the 'Eclipse Period' of the one-step viral growth curve, infectious intracellular virions cannot be detected inside host cells because:",
         ["The virus has uncoated its capsid, releasing its naked nucleic acid to initiate transcription and translation", "All virions have escaped into the extracellular medium", "Viruses are destroyed by host lysosomes", "The host cell has entered apoptosis"],
         0, "The eclipse phase begins immediately upon viral uncoating, when the physical structural virion disassembles so its genome can be replicated; it ends when the first newly assembled infectious progeny virions appear inside the cell.",
         True, "General Virology (ICAR PG PYQ)"),

        ("In virology, a 'Defective Interfering' (DI) particle is a subviral entity characterized as a:",
         ["Spontaneous deletion mutant lacking essential replication genes that can only replicate in the presence of a homologous helper virus, competing for replication machinery and reducing wild-type viral yields", "Virion containing foreign cellular DNA only", "Non-infectious empty capsid", "Virus that only infects bacteria"],
         0, "DI particles arise during high-titer serial passage; their deleted genomes replicate faster than full-length genomes, sequestering viral polymerases and structural proteins from the parent helper virus, thereby 'interfering' with wild-type replication.",
         True, "General Virology (ICAR PG PYQ)"),

        ("Which physical or chemical agent is routinely utilized in veterinary diagnostic laboratories to determine whether an unknown viral isolate possesses a lipid envelope?",
         ["Chloroform or Diethyl Ether treatment (enveloped viruses lose infectivity; non-enveloped viruses survive)", "Heat treatment at 37°C", "Exposure to pH 7.0", "Freezing at -20°C"],
         0, "Lipid solvents (chloroform, ether) and bile salts dissolve the host-derived lipid bilayer envelope of enveloped viruses, destroying their surface attachment spikes and abolishing infectivity, while non-enveloped naked capsids remain infectious.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Enzyme-mediated uncoating of Poxviruses inside host cell cytoplasm occurs in two distinct stages, with the second stage requiring:",
         ["De novo synthesis of a host- or viral-encoded uncoating protein catalyzed by mRNA transcribed by the viral core polymerase", "Acidification inside endosomes", "Direct cleavage by host trypsin", "Exposure to bile salts"],
         0, "Stage 1 uncoating involves host cell enzymes removing the outer envelope; the exposed intact viral core then transcribes early viral mRNAs that translate a specialized uncoating protein, which degrades the core wall to release viral DNA.",
         False, "General Virology"),

        # 11-20: Viral cytopathology, inclusion bodies, cell cultures
        ("A 'Syncytium' (multinucleated giant cell) is a distinctive cytopathic effect (CPE) produced by Paramyxoviruses and Lentiviruses, resulting directly from the action of:",
         ["Viral fusion glycoproteins expressed on the surface of an infected host cell fusing with adjacent uninfected cell membranes", "Viral endonucleases cleaving host chromatin", "Failure of nuclear division", "Phagocytosis of dying cells by hepatocytes"],
         0, "Viruses like Newcastle disease virus, BRSV, and retroviruses express fusion (F) proteins that traffic to the plasma membrane, causing neighboring host cell membranes to fuse together into a massive, multinucleate cytoplasmic mass (syncytium).",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Cowdry Type A inclusion bodies, the classical intranuclear diagnostic hallmark of Herpesvirus infections, are microscopically described as:",
         ["Single, large, round, eosinophilic, amorphous intranuclear masses surrounded by a clear halo, with chromatin margination along the nuclear membrane", "Multiple tiny basophilic granules scattered in the cytoplasm", "Dense crystalline arrays of virions filling the nucleolus", "Intracytoplasmic lipid droplets"],
         0, "Cowdry Type A inclusions (seen in BHV-1, EHV-1, ILT) represent site of viral assembly; as the inclusion expands, chromatin is pushed to the nuclear rim, leaving an eosinophilic central body separated from the nuclear membrane by a clear artifactual halo.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Cowdry Type B inclusion bodies differ from Cowdry Type A inclusions because Type B inclusions:",
         ["Are smaller, more variable in number, do not cause marked chromatin margination, and are seen in Adenovirus or Poliovirus infections", "Are exclusively cytoplasmic", "Stain bright blue with Gram stain", "Are always calcified"],
         0, "Cowdry Type B inclusions (e.g. in Adenovirus and Poliovirus infections) are discrete, smaller, round eosinophilic or amphophilic nuclear bodies that leave normal nuclear chromatin intact without margination.",
         False, "Diagnostic Virology"),

        ("In cell culture techniques, the enzymatic agent universally used to detach adherent monolayer cells from plastic culture flasks for subculturing is:",
         ["Trypsin (frequently combined with EDTA)", "Pepsin", "Collagenase exclusively", "Lysozyme"],
         0, "Trypsin is a serine protease that cleaves cell adhesion proteins (integrins, cadherins) anchoring cells to the plastic substrate; EDTA chelates Ca2+ and Mg2+ ions required for cadherin-mediated intercellular adhesion, accelerating gentle detachment.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Fetal Bovine Serum (FBS) is added to cell culture media (such as DMEM or RPMI-1640) at a concentration of 5% to 10% primarily to provide:",
         ["Essential physiological growth factors, hormones, attachment factors (fibronectin), and trace minerals", "An energy source in place of glucose", "Protection against bacterial contamination", "Buffering capacity alone"],
         0, "FBS is rich in polypeptide growth factors (EGF, FGF, IGF), attachment factors, transport proteins (transferrin, albumin), and selenium, which are essential for cell proliferation and survival in in vitro cell culture.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The pH indicator universally incorporated into mammalian cell culture media (e.g. MEM, DMEM) that turns yellow upon medium acidification is:",
         ["Phenol Red (red at physiological pH 7.2-7.4, yellow when acidic < 6.8, purple when alkaline > 7.8)", "Methyl Red", "Bromothymol Blue", "Neutral Red"],
         0, "Phenol red monitors media pH: cellular metabolism produces lactic acid and CO2, dropping the pH and turning the medium orange-yellow; nutrient exhaustion or contamination triggers rapid yellowing, alerting the virologist.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The primary diagnostic application of the yolk sac route of inoculation in 5-to-7-day-old embryonated chicken eggs is for the cultivation of:",
         ["Chlamydia psittaci and Avian Encephalomyelitis Virus", "Foot and Mouth Disease Virus", "Rabies virus", "Newcastle Disease Virus exclusively"],
         0, "The yolk sac of 5-7 day old embryos provides an abundant, lipid-rich nutrient environment specifically favored for the primary propagation and titration of fastidious Chlamydia species and Avian Encephalomyelitis picornavirus.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In diagnostic virology, 'Interference' is a diagnostic phenomenon where:",
         ["Infection of a cell culture by a non-cytopathic virus inhibits or blocks subsequent replication and cytopathic effect of a superinfecting challenge virus", "Two viruses kill the host cell in half the time", "A virus loses its genome", "Antiserum fails to neutralize a virus"],
         0, "Viral interference occurs when the primary virus stimulates cellular interferon production or downregulates entry receptors; it is utilized diagnostically to detect non-cytopathic viruses (e.g. rubella or Hog Cholera) by challenging with an indicator cytopathic virus.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Differential centrifugation and Sucrose Density Gradient Centrifugation are biophysical methods used in virology for:",
         ["Purification and concentration of intact viral particles based on buoyant density and sedimentation coefficient", "Measuring viral genome mutation rate", "Counting bacterial colonies", "Inactivating viral envelopes"],
         0, "Isopycnic (equilibrium density) centrifugation in cesium chloride (CsCl) or sucrose gradients separates and purifies intact virions, defective particles, and empty capsids into discrete visible buoyant density bands (expressed in g/cm3).",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Polyethylene Glycol (PEG 6000 or 8000) is commonly used in viral laboratories for:",
         ["Precipitation and concentration of viruses from large volumes of cell culture supernatants", "Inactivating viral infectivity for vaccines", "Staining viral capsids for brightfield microscopy", "Buffering pH"],
         0, "PEG acts as a non-ionic volume-excluding hydrophilic polymer; by sequestering free water, it forces viral particles to aggregate and precipitate out of solution at neutral pH, allowing gentle harvest by low-speed centrifugation.",
         False, "Diagnostic Virology"),

        # 21-25: PCR, diagnostics, biosafety
        ("Reverse Transcription Polymerase Chain Reaction (RT-PCR) is the essential molecular diagnostic tool for detecting RNA viruses because it utilizes:",
         ["Reverse Transcriptase to synthesize complementary DNA (cDNA) from the viral RNA template prior to exponential PCR amplification", "Taq polymerase alone to copy RNA directly", "DNA ligase exclusively", "Restriction endonucleases to cut RNA"],
         0, "Standard thermostable DNA polymerases (like Taq) can only use DNA templates; RT-PCR first utilizes viral reverse transcriptase (e.g. M-MLV RT) with specific primers to generate cDNA, which is then amplified by conventional or real-time PCR.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("In Real-Time quantitative PCR (qPCR) utilizing TaqMan chemistry, the fluorescent reporter signal is generated through:",
         ["The 5' to 3' exonuclease activity of Taq DNA polymerase cleaving the dual-labeled fluorogenic probe hybridized to the target sequence", "Direct intercalation of ethidium bromide into double-stranded DNA", "Binding of antibodies to the amplicon", "Chemical degradation of primers"],
         0, "A TaqMan probe has a 5' reporter dye (e.g. FAM) and a 3' quencher dye (e.g. TAMRA); during primer extension, the 5'->3' exonuclease activity of Taq polymerase hydrolyzes the hybridized probe, releasing the reporter from quencher proximity to fluoresce.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The primary diagnostic utility of the 'Hemagglutination' (HA) test in veterinary virology is that it:",
         ["Provides a rapid, simple, in vitro quantification of viral particles without requiring living host cells, based on surface hemagglutinins bridging erythrocytes", "Measures the precise number of viable neutralizing antibodies", "Identifies bacterial spores", "Measures host cell apoptosis"],
         0, "Viruses like Influenza, Newcastle Disease, and Parvoviruses possess surface spikes that bind sialic acid or glycoprotein receptors on red blood cells, cross-linking them into a continuous macroscopic lattice in microtiter plates.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("Under the World Health Organization (WHO) and WOAH laboratory biosafety classification, Foot and Mouth Disease Virus and African Swine Fever Virus are classified under which Biosafety Level (BSL)?",
         ["Biosafety Level 3 Agriculture (BSL-3 Ag / High Containment)", "Biosafety Level 1", "Biosafety Level 2", "Biosafety Level 4 only"],
         0, "FMDV and ASFV are highly contagious transboundary animal pathogens capable of catastrophic economic devastation; they require Biosafety Level 3 Agriculture (BSL-3 Ag) high-containment facilities equipped with negative air pressure and HEPA filtration.",
         True, "Diagnostic Virology (ICAR PG PYQ)"),

        ("The preservative solution universally recommended for submitting field tissue samples for viral isolation when samples cannot be frozen immediately in liquid nitrogen is:",
         ["50% Buffered Glycerol Saline (equal parts glycerol and 0.01M phosphate-buffered saline, pH 7.4)", "10% Neutral Buffered Formalin", "70% Ethanol", "Distilled water with penicillin"],
         0, "Glycerol stabilizes viral proteins and acts as a cryoprotectant; 50% neutral glycerol saline prevents osmotic lysis and preserves viral viability during ambient temperature transport to diagnostic laboratories (unlike formalin, which kills viruses).",
         True, "Diagnostic Virology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module5_questions()
    print(f"Microbiology Module 5 loaded: {len(qs)} questions")
