# scripts/micro2_mod4.py
# Module 4: General & Systematic Virology (DNA & RNA Animal/Poultry Viruses & Prions) (75 questions)

TOPIC = "General & Systematic Virology (DNA & RNA Animal/Poultry Viruses & Prions)"

def get_module4_questions():
    return [
        (
            "In David Baltimore's classification of viruses based on mRNA synthesis pathways, Class VII viruses (such as Duck Hepatitis B Virus in the family Hepadnaviridae) possess which unique genome and replication strategy?",
            [
                "Partially double-stranded (gapped) circular DNA that replicates via a pregenomic RNA intermediate using viral reverse transcriptase",
                "Linear single-stranded positive-sense RNA that replicates directly in the cytoplasm without any DNA intermediate",
                "Segmented double-stranded RNA that transcribes monocistronic mRNAs inside an intact icosahedral subviral core",
                "Circular single-stranded negative-sense DNA that replicates via rolling-circle amplification in the host nucleolus"
            ],
            0,
            "Baltimore Class VII viruses (Hepadnaviridae and Caulimoviridae, termed pararetroviruses) package a partially double-stranded, gapped circular DNA genome that is repaired to cccDNA in the nucleus, transcribed into pregenomic RNA, and reverse-transcribed back into DNA inside nascent viral cores.",
            True,
            TOPIC
        ),
        (
            "Autonomous Parvoviruses (Baltimore Class II, single-stranded linear DNA) lack a viral DNA polymerase and initiate replication of their genome in the nucleus of S-phase host cells by using:",
            [
                "Short host-derived capped mRNA primers cleaved from cellular pre-mRNAs ('cap-snatching')",
                "Self-complementary terminal palindromic sequences that fold into 3' hairpin loops ('rolling-hairpin' self-priming)",
                "A covalently linked terminal protein (TP) carrying a deoxycytidine monophosphate residue",
                "Host transfer RNA (tRNALys or tRNATrp) annealed to a primer-binding site near the 5' end"
            ],
            1,
            "Parvovirus linear ssDNA genomes possess palindromic inverted terminal repeats (ITRs) at both ends that fold back on themselves to form base-paired 3'-OH hairpin duplexes, serving as built-in self-primers for host DNA Polymerase delta.",
            True,
            TOPIC
        ),
        (
            "Why do double-stranded RNA viruses (Baltimore Class III, such as Bluetongue virus, Rotavirus, and Infectious Bursal Disease virus) NEVER uncoat completely to release naked dsRNA into the host cell cytoplasm?",
            [
                "Naked dsRNA is immediately imported into the host nucleus and integrated by host transposases",
                "The host ribosome directly translates intact dsRNA duplexes without needing mRNA transcription",
                "Exposed cytoplasmic dsRNA is a potent PAMP (activating PKR, OAS/RNase L, and RIG-I/MDA5) and host cells lack dsRNA-dependent RNA polymerases",
                "Double-stranded RNA spontaneously hydrolyzes at physiological pH 7.4 unless chelated by calcium ions"
            ],
            2,
            "Eukaryotic cells lack enzymes to transcribe dsRNA into mRNA and possess powerful innate sensors (PKR, RIG-I, MDA5, TLR3, OAS) that trigger interferon and translational shutoff upon detecting naked dsRNA. Therefore, dsRNA viruses keep their genome hidden inside an inner core capsid and extrude only +ssRNA transcripts synthesized by internal viral RdRp.",
            True,
            TOPIC
        ),
        (
            "Unlike cellular mRNAs (which possess a 5' 7-methylguanosine cap), the positive-sense single-stranded RNA genome of Picornaviruses (such as Foot and Mouth Disease Virus) has which structure at its 5' end and initiates translation via which mechanism?",
            [
                "A covalently linked tRNA primer and leaky scanning of polycistronic subgenomic mRNAs",
                "A triphosphorylated 5'-pppA terminus and ribosomal shunting across a hairpin leader",
                "A host-snatched 5' methylated cap and 40S ribosomal scanning from the extreme 5' terminus",
                "A covalently linked viral protein (VPg / 3B) and cap-independent translation via an Internal Ribosome Entry Site (IRES)"
            ],
            3,
            "Picornavirus genomic +ssRNA has the small peptide VPg (viral protein genome-linked, encoded by 3B) covalently attached via a tyrosine phosphodiester bond to its 5' uridine, and recruits the 40S ribosome directly to an Internal Ribosome Entry Site (IRES) in the 5' UTR.",
            True,
            TOPIC
        ),
        (
            "During Foot and Mouth Disease Virus (FMDV) replication, how does the viral Leader Protease (Lpro) rapidly shut off host cell protein synthesis while allowing viral protein synthesis to proceed unimpeded?",
            [
                "Lpro cleaves host eukaryotic translation initiation factor eIF4G, abolishing cap-dependent host mRNA translation",
                "Lpro depurinates the 28S rRNA of the 60S ribosomal subunit in a manner identical to ricin toxin",
                "Lpro ADP-ribosylates host elongation factor-2 (eEF-2) to freeze polypeptide translocation",
                "Lpro degrades all cellular transfer RNAs (tRNAs) except initiator methionyl-tRNA"
            ],
            0,
            "FMDV Leader protease (Lpro, a papain-like cysteine protease) cleaves the host scaffold protein eIF4G (which bridges the 5'-cap-binding protein eIF4E to the 40S ribosome). This shuts down host cap-dependent translation (including Type I interferon synthesis), while FMDV IRES-mediated translation requires only the C-terminal fragment of eIF4G.",
            True,
            TOPIC
        ),
        (
            "The icosahedral capsid of Foot and Mouth Disease Virus is assembled from 60 copies of each of four structural proteins (VP1, VP2, VP3, and VP4). Which protein is entirely internal (lining the inner capsid surface), and which protein carries the surface-exposed RGD loop that induces neutralizing antibodies?",
            [
                "VP1 is entirely internal; VP4 carries the surface RGD neutralizing loop",
                "VP4 is entirely internal and myristoylated; VP1 carries the surface G-H loop (residues 140–160) with the RGD motif",
                "VP2 is entirely internal; VP3 carries the surface RGD neutralizing loop",
                "VP3 is entirely internal; VP2 carries the surface RGD neutralizing loop"
            ],
            1,
            "In FMDV (146S intact virion), VP1, VP2, and VP3 form the external icosahedral shell, with the flexible G-H loop of VP1 displaying the conserved Arg-Gly-Asp (RGD) tripeptide that binds host alpha-v integrins. VP4 is small, myristoylated, and located entirely on the interior face of the capsid in contact with viral RNA.",
            True,
            TOPIC
        ),
        (
            "In the epidemiology of Foot and Mouth Disease, an animal is defined as a 'Persistent Carrier' if infectious FMDV can be recovered for more than 28 days post-infection. Which domestic species NEVER becomes an FMDV carrier, and what is the primary anatomical site of persistence in cattle (sampled via a Probang cup)?",
            [
                "Cattle never become carriers; virus persists in the renal cortex of pigs",
                "Sheep and goats never become carriers; virus persists in the spleen of horses",
                "Swine (pigs) do NOT become carriers; in cattle and buffaloes, virus persists in the dorsal soft palate and nasopharynx",
                "Water buffaloes never become carriers; virus persists in the mammary gland of pigs"
            ],
            2,
            "Pigs shed massive aerosol quantities of FMDV ('amplifier hosts') during acute infection but clear the virus completely within 3–4 weeks and NEVER become long-term carriers. Ruminants (cattle up to 3.5 years, sheep ~9 months, African Cape buffalo up to 5 years) harbor persistent virus in the epithelial crypts of the dorsal soft palate and pharynx, sampled via a Probang cup.",
            True,
            TOPIC
        ),
        (
            "In modern commercial FMD vaccine manufacturing, why is Binary Ethylenimine (BEI) universally preferred over Formaldehyde for viral inactivation?",
            [
                "BEI cross-links the outer VP1 capsid proteins into rigid heat-stable 12S pentamers",
                "BEI saponifies the viral lipid envelope without requiring aluminum hydroxide or oil adjuvants",
                "BEI selectively cleaves the non-structural 3ABC polyprotein from the crude culture supernatant",
                "BEI alkylates the internal viral RNA with linear first-order kinetics while leaving the immunogenic 146S capsid epitopes intact"
            ],
            3,
            "Formaldehyde cross-links surface capsid proteins and exhibits non-linear ('tailing') inactivation kinetics that can leave residual live virus inside aggregates. Binary Ethylenimine (BEI, an aziridine formed by cyclization of 2-bromoethylamine in alkali) penetrates the capsid and alkylates viral RNA with first-order kinetics without altering the 146S antigenic conformation.",
            True,
            TOPIC
        ),
        (
            "Which emerging picornavirus (genus Senecavirus) causes vesicular lesions on the snout, oral mucosa, and coronary bands of pigs that are clinically indistinguishable from Foot and Mouth Disease, requiring differential RT-PCR in swine vesicular disease investigations?",
            [
                "Senecavirus A (Seneca Valley Virus)",
                "Porcine Teschovirus-1 (Teschen/Talfan disease virus)",
                "Sapelovirus A (Porcine enterovirus 8)",
                "Torque Teno Sus Virus (TTSuV)"
            ],
            0,
            "Senecavirus A (Seneca Valley Virus, family Picornaviridae) causes acute vesicular lesions on the snout and coronary bands of market pigs and sows as well as neonatal piglet mortality (epidemics since 2015), clinically mimicking FMD, Vesicular Stomatitis, Swine Vesicular Disease, and Vesicular Exanthema of Swine.",
            True,
            TOPIC
        ),
        (
            "Swine Vesicular Disease Virus (SVDV)—which produces vesicular lesions in pigs identical to FMD—differs fundamentally from FMDV in its taxonomy, physicochemical stability, and host range because SVDV is:",
            [
                "An enveloped Rhabdovirus that is rapidly destroyed at pH 6.5 and infects horses and cattle",
                "An Enterovirus (Picornaviridae) that is stable from pH 2.5 to 12.0, persists in cured pork salami, and infects ONLY pigs",
                "A Calicivirus derived from marine pinnipeds that is inactivated at 37°C within 1 hour",
                "A double-stranded RNA Orbivirus transmitted biologically by Culicoides biting midges"
            ],
            1,
            "Swine Vesicular Disease Virus (SVDV) belongs to the genus Enterovirus (species Enterovirus B, closely related to human Coxsackievirus B5). Unlike acid-labile FMDV (inactivated below pH 6.0), SVDV is acid-resistant (stable at pH 2.5–12.0), survives fermentation and smoking in dry sausages for >1 year, and naturally infects only swine.",
            True,
            TOPIC
        ),
        (
            "Encephalomyocarditis Virus (EMCV, genus Cardiovirus, family Picornaviridae) is maintained in nature by commensal rats and mice (Rattus and Mus species) and causes which characteristic fatal syndrome in young swine and captive zoo elephants?",
            [
                "Progressive demyelinating leukoencephalomalacia and blindness",
                "Chronic proliferative ileitis and mesenteric lymphadenopathy",
                "Sudden death from acute non-suppurative myocarditis with chalky white necrotic streaks in the right ventricle and reproductive failure in sows",
                "Vesicular eruptions on the tongue, snout, and interdigital skin"
            ],
            2,
            "Rodents are the natural reservoir of EMCV, shedding virus in feces and urine that contaminate swine and elephant feed/water. In piglets and elephants, EMCV has an intense tropism for the myocardium, causing peracute sudden death with pale yellow-to-chalky white calcified necrotic foci in the ventricular myocardium.",
            True,
            TOPIC
        ),
        (
            "'Epidemic Tremor' (Avian Encephalomyelitis), characterized by ataxia, sitting on the hocks, rapid fine tremors of the head and neck, and subsequent bilateral lens cataracts in 1-to-3-week-old chicks, is caused by a vertically and horizontally transmitted virus belonging to which family?",
            [
                "Coronaviridae (genus Gammacoronavirus)",
                "Flaviviridae (genus Orthoflavivirus)",
                "Birnaviridae (genus Avibirnavirus)",
                "Picornaviridae (genus Tremovirus, species Tremovirus A)"
            ],
            3,
            "Avian Encephalomyelitis Virus (AEV) is a hepatovirus-like picornavirus (genus Tremovirus). When naive laying hens are infected during egg production, they experience a temporary drop in egg production and transmit the virus vertically into eggs, causing 'Epidemic Tremor' in hatched chicks; breeder pullets are vaccinated at 10–15 weeks (prior to lay).",
            True,
            TOPIC
        ),
        (
            "Rabbit Hemorrhagic Disease Virus (RHDV / RHDV2)—which causes peracute necrotizing hepatitis, disseminated intravascular coagulation (DIC), blood-stained nasal discharge, and >80% mortality in European rabbits (Oryctolagus cuniculi)—belongs to which viral family and genus?",
            [
                "Family Caliciviridae, genus Lagovirus",
                "Family Poxviridae, genus Leporipoxvirus",
                "Family Filoviridae, genus Orthoebolavirus",
                "Family Togaviridae, genus Alphavirus"
            ],
            0,
            "Rabbit Hemorrhagic Disease Virus (RHDV / Lagovirus europaeus) is a non-enveloped positive-sense ssRNA virus in the family Caliciviridae (genus Lagovirus) that targets hepatocytes and endothelial cells and characteristically agglutinates human group O erythrocytes.",
            True,
            TOPIC
        ),
        (
            "Among the mosquito-borne equine encephalomyelitis viruses (Eastern [EEE], Western [WEE], and Venezuelan [VEE] Equine Encephalomyelitis viruses, genus Alphavirus, family Togaviridae), which virus uses HORSES as the primary viremic amplifying host rather than a dead-end host?",
            [
                "Eastern Equine Encephalomyelitis Virus (EEEV, maintained in Culiseta melanura and passerine birds)",
                "Venezuelan Equine Encephalomyelitis Virus (VEEV, epidemic strains IA/IB/IC)",
                "Western Equine Encephalomyelitis Virus (WEEV, maintained in Culex tarsalis and wild birds)",
                "West Nile Virus (WNV, genus Orthoflavivirus)"
            ],
            1,
            "In EEE, WEE, and West Nile virus infections, wild birds are the amplifying reservoir hosts, while horses develop low-level viremia insufficient to infect mosquitoes ('dead-end hosts'). In contrast, epizootic Venezuelan Equine Encephalomyelitis Virus (VEEV) replicates to extremely high viremic titers in horses, making equids the primary amplifying hosts for mosquito transmission.",
            True,
            TOPIC
        ),
        (
            "In the natural transmission cycle of Japanese Encephalitis Virus (JEV, genus Orthoflavivirus, family Flaviviridae), transmitted by paddy-breeding Culex tritaeniorhynchus mosquitoes, which domestic animal serves as the primary mammalian 'amplifying host' (suffering stillbirths, mummified fetuses, and boar orchitis), while horses and humans act as dead-end hosts?",
            [
                "Domestic cattle and water buffaloes",
                "Sheep and goats",
                "Swine (domestic and wild pigs, alongside ardeid wading birds as natural reservoirs)",
                "Domestic dogs and cats"
            ],
            2,
            "Ardeid wading birds (pond herons and cattle egrets) are the natural maintenance reservoirs of JEV, while domestic pigs develop prolonged, high-titer viremia that infects Culex tritaeniorhynchus mosquitoes (acting as the key peri-domestic amplifying host). Pregnant sows suffer stillbirths/mummification, whereas horses and humans are dead-end hosts developing fatal encephalitis.",
            True,
            TOPIC
        ),
        (
            "How does fatal 'Mucosal Disease' (characterized by severe panleukopenia and linear erosions/ulcerations over Peyer's patches and the gastrointestinal tract) develop in cattle infected with Bovine Viral Diarrhea Virus (BVDV)?",
            [
                "Primary post-natal aerosol infection of an immunocompetent adult dairy cow with a non-cytopathic BVDV Type 1 strain",
                "Co-infection of a neonatal calf under 5 days of age with Bovine Coronavirus and Cryptosporidium parvum",
                "Transplacental infection of a fetus during the third trimester (days 200–270) with a cytopathic BVDV strain",
                "Superinfection of an immunotolerant Persistently Infected (PI) animal (harboring non-cytopathic BVDV from days 40–120 of gestation) with an antigenically homologous Cytopathic (CP) BVDV biotype"
            ],
            3,
            "When a fetus is infected between days 40 and 120 of gestation with a Non-Cytopathic (NCP) BVDV strain, it becomes immunotolerant to that specific strain and is born Persistently Infected (PI). If that PI calf later encounters an antigenically homologous Cytopathic (CP) BVDV strain (typically via mutation/RNA recombination that cleaves NS2-3 into NS3), the unchecked CP virus destroys gut lymphoid tissue, causing fatal Mucosal Disease.",
            True,
            TOPIC
        ),
        (
            "In Classical Swine Fever Virus (CSFV / Hog Cholera), which envelope glycoprotein is the major immunodominant target of virus-neutralizing antibodies and is incorporated into chimeric or baculovirus-expressed subunit DIVA vaccines?",
            [
                "Envelope glycoprotein E2 (gp55)",
                "Envelope glycoprotein Erns (gp44/48, possessing intrinsic ribonuclease activity)",
                "Non-structural helicase/protease protein NS3 (p80)",
                "Internal nucleocapsid core protein C (p14)"
            ],
            0,
            "The pestivirus envelope contains three glycoproteins: Erns (secreted ribonuclease used as the companion diagnostic antigen in DIVA ELISAs), E1, and E2. Glycoprotein E2 (gp55) is the major immunogenic surface spike that induces potent neutralizing antibodies and confers complete protection in subunit and chimeric (CP7_E2alf) marker vaccines.",
            True,
            TOPIC
        ),
        (
            "Porcine Reproductive and Respiratory Syndrome Virus (PRRSV, family Arteriviridae) exhibits an extremely restricted cellular tropism for porcine alveolar macrophages. Which macrophage surface receptor is the essential mediator of PRRSV uncoating and genome release (whose gene deletion renders gene-edited pigs completely resistant to PRRSV)?",
            [
                "Angiotensin-Converting Enzyme 2 (ACE2)",
                "Scavenger receptor CD163 (specifically its SRCR5 domain)",
                "Signaling Lymphocyte Activation Molecule (SLAM / CD150)",
                "Coxsackievirus and Adenovirus Receptor (CAR)"
            ],
            1,
            "While sialoadhesin (CD169 / Siglec-1) mediates initial attachment and internalization on porcine alveolar macrophages, the scavenger receptor CD163 (specifically domain 5, SRCR5) is indispensable for PRRSV uncoating and infection; CRISPR/Cas9 pigs lacking CD163 SRCR5 are completely resistant to both PRRSV-1 and PRRSV-2.",
            True,
            TOPIC
        ),
        (
            "Unlike Avian Paramyxoviruses and Orthomyxoviruses, freshly harvested allantoic fluid containing Infectious Bronchitis Virus (IBV, Gammacoronavirus) does NOT spontaneously agglutinate chicken red blood cells until the viral suspension is pre-treated with which enzyme to cleave surface alpha-2,3-linked sialic acid inhibitors?",
            [
                "Trypsin or Chymotrypsin",
                "Lysozyme or Lysostaphin",
                "Neuraminidase or Phospholipase C (Type 1 from Clostridium perfringens)",
                "Proteinase K or Papain"
            ],
            2,
            "Native Infectious Bronchitis Virus (IBV) virions do not hemagglutinate chicken erythrocytes directly; treatment of concentrated IBV with bacterial Neuraminidase or Clostridium perfringens Type 1 Phospholipase C removes interfering sialic acid/lipid moieties and exposes the hemagglutinating site on the S1 spike glycoprotein for HI testing.",
            True,
            TOPIC
        ),
        (
            "According to World Health Organization (WHO) and WOAH standards for human and animal Rabies vaccination, what is the minimum acceptable protective serum virus-neutralizing antibody titer (as measured by RFFIT or FAVN assay) confirming adequate immunity?",
            [
                "Greater than or equal to 0.01 IU/mL",
                "Greater than or equal to 10.0 IU/mL",
                "Greater than or equal to 5.0 IU/mL",
                "Greater than or equal to 0.5 IU/mL"
            ],
            3,
            "A serum neutralizing antibody level of >= 0.5 International Units per milliliter (0.5 IU/mL), measured by the Rapid Fluorescent Focus Inhibition Test (RFFIT) or Fluorescent Antibody Virus Neutralization (FAVN) test, is the universal benchmark for protective immunity against Rabies.",
            True,
            TOPIC
        ),
        (
            "In clinical differential diagnosis of vesicular diseases, how does Vesicular Stomatitis Virus (VSV, genus Vesiculovirus, family Rhabdoviridae) differ critically in its domestic host range from Foot and Mouth Disease Virus (FMDV)?",
            [
                "Vesicular Stomatitis Virus causes natural clinical vesicular disease in HORSES (as well as cattle and pigs), whereas horses are completely refractory to FMDV",
                "Vesicular Stomatitis Virus infects only sheep and goats, whereas FMDV infects only horses and dogs",
                "Vesicular Stomatitis Virus infects only marine pinnipeds and swine, sparing cattle and horses",
                "Vesicular Stomatitis Virus causes vesicular lesions exclusively in poultry and waterfowl"
            ],
            0,
            "Equids (horses, donkeys, mules) are completely resistant to Foot and Mouth Disease Virus, Swine Vesicular Disease Virus, and Senecavirus A, but are highly susceptible to Vesicular Stomatitis Virus (serotypes New Jersey and Indiana). Therefore, vesicular lesions in horses immediately rule out FMD and point to Vesicular Stomatitis.",
            True,
            TOPIC
        ),
        (
            "Bovine Ephemeral Fever ('Three-Day Sickness')—an arthropod-borne rhabdoviral disease (genus Ephemerovirus) of cattle and water buffaloes characterized by acute biphasic fever, shivering, shifting lameness, and sternal recumbency with rapid recovery—induces recumbency primarily by causing:",
            [
                "Irreversible demyelination of the sciatic nerve and lumbar spinal cord",
                "Severe acute hypocalcemia and neutrophilic polyserositis/synovitis mimicking parturient paresis (milk fever)",
                "Massive intravascular hemolysis and methemoglobinemia",
                "Spastic tetanic contraction of axial muscles via Renshaw cell blockade"
            ],
            1,
            "Bovine Ephemeral Fever Virus triggers an acute pro-inflammatory cytokine storm (IFN-alpha, TNF-alpha, IL-1) accompanied by a sharp drop in ionized blood calcium (hypocalcemia), causing rumen stasis, muscle tremors, paresis, and recumbency that often responds dramatically to intravenous calcium borogluconate.",
            True,
            TOPIC
        ),
        (
            "In the biological pathotyping of Newcastle Disease Virus (NDV) isolates using 9-to-10-day-old embryonated chicken eggs, how are Velogenic, Mesogenic, and Lentogenic strains classified based on the 'Mean Death Time' (MDT, in hours) of the minimum lethal dose?",
            [
                "Velogenic: >90 hours; Mesogenic: 60–90 hours; Lentogenic: <60 hours",
                "Velogenic: <12 hours; Mesogenic: 12–24 hours; Lentogenic: 24–48 hours",
                "Velogenic: <60 hours; Mesogenic: 60–90 hours; Lentogenic: >90 hours",
                "Velogenic: 100–120 hours; Mesogenic: 120–150 hours; Lentogenic: >150 hours"
            ],
            2,
            "Mean Death Time (MDT) in embryonated chicken eggs classifies NDV pathotypes into three groups: Velogenic strains kill embryos in <60 hours (ICPI 1.5–2.0); Mesogenic strains (such as R2B Mukteswar and Komarov) kill embryos in 60–90 hours (ICPI 1.0–1.5); and Lentogenic strains (such as LaSota, F, and B1) take >90 hours (ICPI <0.7).",
            True,
            TOPIC
        ),
        (
            "In Indian poultry vaccination programs against Newcastle Disease (Ranikhet Disease), which live attenuated 'Mesogenic' strain—administered parenterally (subcutaneously/intramuscularly) as a booster only to birds older than 6 to 8 weeks already primed with a lentogenic vaccine—provides long-lasting immunity?",
            [
                "LaSota strain",
                "Hitchner B1 strain",
                "Ulster 2C strain",
                "R2B (Mukteswar) strain (or Komarov strain)"
            ],
            3,
            "The R2B (Mukteswar) strain was developed at IVRI, Mukteswar by serial passage in embryonated eggs. Because it is a mesogenic strain, it is neuropathic/lethal if given to unprimed chicks under 6 weeks of age, and is reserved as an injectable booster at 6–8 weeks after primary lentogenic (F or LaSota) vaccination.",
            True,
            TOPIC
        ),
        (
            "Hendra Virus (causing acute fatal respiratory and neurological disease in horses and humans in Australia) and Nipah Virus (causing 'barking pig syndrome' and fatal human encephalitis in Asia) are BSL-4 zoonotic paramyxoviruses (genus Henipavirus) whose natural wildlife reservoir is:",
            [
                "Frugivorous flying foxes (fruit bats of the genus Pteropus)",
                "Wild aquatic mallard ducks (Anas platyrhynchos)",
                "Peridomestic brown rats (Rattus norvegicus)",
                "Ixodid hard ticks (Ixodes holocyclus)"
            ],
            0,
            "Pteropid fruit bats (flying foxes of the genus Pteropus) are the asymptomatic natural reservoir hosts of both Hendra virus and Nipah virus, shedding virus in urine, saliva, and birthing fluids onto pastures or date palm sap/fruit consumed by horses and pigs.",
            True,
            TOPIC
        ),
        (
            "During necropsy of a goat or sheep that died of acute Peste des Petits Ruminants (PPR), the pathognomonic gross lesion observed along the crests of the longitudinal mucosal folds of the ceco-colic junction and rectum is:",
            [
                "Button-like concentric necrotic ulcers ('button ulcers')",
                "Linear dark-red zones of congestion and hemorrhage termed 'Zebra Markings' (or 'Zebra Stripes')",
                "Thickened, corrugated, cobblestone-like granulomatous rugae resembling Johne's disease",
                "Annular diphtheritic hemorrhagic rings encircling the gut lumen"
            ],
            1,
            "In acute PPR (and historically Rinderpest), linear streaks of severe congestion and hemorrhage develop along the crests of the longitudinal mucosal folds of the posterior colon, ceco-colic junction, and rectum, creating the classic diagnostic appearance known as 'Zebra stripes' or 'Zebra markings'.",
            True,
            TOPIC
        ),
        (
            "In Influenza A viruses (family Orthomyxoviridae), what is the specific biological function of the viral Neuraminidase (NA) surface glycoprotein during the replication cycle?",
            [
                "It binds alpha-2,3-sialic acid receptors on host enterocytes to initiate receptor-mediated endocytosis",
                "It forms a proton-selective ion channel that acidifies the viral core inside the endosome",
                "It cleaves terminal sialic acid (N-acetylneuraminic acid) residues from host glycoproteins and glycolipids to release budding progeny virions and prevent viral self-aggregation",
                "It snatches 5'-methylated cap structures from host nuclear pre-mRNAs to prime viral transcription"
            ],
            2,
            "While Hemagglutinin (HA) binds sialic acid receptors and mediates membrane fusion, Neuraminidase (NA, a tetrameric mushroom-shaped sialidase) cleaves terminal sialic acid from respiratory mucus and from the infected cell surface, allowing newly budded virions to detach rather than clumping together.",
            True,
            TOPIC
        ),
        (
            "Rift Valley Fever Virus (RVFV, genus Phlebovirus, family Phenuiviridae) is a high-consequence mosquito-borne zoonotic arbovirus in Africa and the Arabian Peninsula whose two classic epidemiological hallmarks in sheep and cattle herds are:",
            [
                "Chronic progressive carpal arthritis and demyelinating leukoencephalomalacia in adult rams",
                "Vesicular lesions on the coronary band and persistent pharyngeal shedding for 3 years",
                "Congenital cerebellar hypoplasia and persistent immunotolerant viremia in surviving calves",
                "Nearly 100% 'abortion storms' in pregnant ewes and >90% mortality with diffuse hepatic necrosis ('yellow liver') in neonatal lambs"
            ],
            3,
            "Outbreaks of Rift Valley Fever following heavy rainfall and flooding of dambos (Aedes mosquito emergence) are immediately recognized by simultaneous near-100% abortion storms in pregnant ewes/cows, >90% mortality with bright yellow pan-necrotic livers in newborn lambs, and influenza-like/hemorrhagic illness in veterinary personnel.",
            True,
            TOPIC
        ),
        (
            "Akabane Virus and Schmallenberg Virus (genus Orthobunyavirus, family Peribunyaviridae) are Culicoides-transmitted arboviruses that cause mild or subclinical infection in adult cattle and sheep, but when transmitted transplacentally during early-to-mid gestation, they cause which classic congenital malformation syndrome?",
            [
                "Arthrogryposis-Hydranencephaly Syndrome (AHS: ankylosed joints, torticollis, scoliosis, and fluid-filled cerebral hemispheres)",
                "Bilateral microphthalmia, persistent right aortic arch, and ventricular septal defects",
                "Hypomyelinogenesis ('hairy shaker lambs') and persistent postnatal viremia",
                "Osteopetrosis ('marble bone disease') and thymic aplasia"
            ],
            0,
            "Akabane virus, Schmallenberg virus, and Cache Valley virus are teratogenic orthobunyaviruses transmitted by Culicoides midges (or mosquitoes for Cache Valley). Depending on the gestational age of the fetus, destruction of developing cerebral neuroblasts and spinal ventral horn motor neurons produces Hydranencephaly and neurogenic Arthrogryposis (AHS).",
            True,
            TOPIC
        ),
        (
            "Nairobi Sheep Disease Virus (genus Orthonairovirus, family Nairoviridae)—which causes peracute hemorrhagic gastroenteritis and >70% mortality in naive sheep and goats in East Africa—is antigenically and genetically synonymous with which tick-borne virus found in India?",
            [
                "Kyasanur Forest Disease Virus (transmitted by Haemaphysalis spinigera)",
                "Ganjam Virus (transmitted in India by Haemaphysalis intermedia)",
                "Bhanja Virus (transmitted by Rhipicephalus decoloratus)",
                "Chandipura Virus (transmitted by Phlebotomus sandflies)"
            ],
            1,
            "Nairobi Sheep Disease Virus (transmitted in East Africa by the brown ear tick Rhipicephalus appendiculatus) and Ganjam Virus (isolated from sheep and goats in Odisha/India and transmitted by Haemaphysalis intermedia) are now classified as variants of the same Orthonairovirus species (Nairobi sheep disease orthonairovirus).",
            True,
            TOPIC
        ),
        (
            "In the double-layered icosahedral capsid of Bluetongue Virus (BTV, genus Orbivirus), which structural protein forms the conserved middle core layer (detecting all 29+ BTV serotypes in group-specific cELISA), and which outer capsid protein determines the specific Serotype (1–29+) in Virus Neutralization?",
            [
                "VP2 is the group-specific core antigen; VP7 is the serotype-specific outer neutralization antigen",
                "VP6 is the group-specific core antigen; VP4 is the serotype-specific outer neutralization antigen",
                "VP7 is the conserved group-specific middle core antigen; VP2 is the outer capsid protein determining serotype specificity",
                "NS1 is the group-specific core antigen; NS3 is the serotype-specific outer neutralization antigen"
            ],
            2,
            "In Bluetongue Virus, VP7 (encoded by segment 7) forms the 260 trimers of the middle core layer and is highly conserved across all BTV serotypes (serving as the target antigen in competitive ELISA). VP2 (encoded by segment 2) forms the outermost triskelion spikes, mediates hemagglutination and cell attachment, and determines serotype specificity.",
            True,
            TOPIC
        ),
        (
            "African Horse Sickness Virus (AHSV, genus Orbivirus) manifests in four classical clinical forms in equids. What are the pathognomonic signs of the peracute 'Dunkop' form versus the subacute 'Dikkop' form?",
            [
                "Dunkop is the mild fever form in zebras; Dikkop is the ascending spinal paralysis form",
                "Dunkop is characterized by hepatic cirrhosis; Dikkop is characterized by ulcerative lymphangitis",
                "Dunkop is the cutaneous papular form; Dikkop is the hemorrhagic enterocolitis form",
                "Dunkop (pulmonary form) causes fulminant pulmonary edema and frothy nasal discharge; Dikkop (cardiac form) causes subcutaneous edema of the head/supraorbital fossae and hydropericardium"
            ],
            3,
            "In Afrikaans, 'Dunkop' ('thin head', the peracute pulmonary form) is characterized by severe dyspnea, paroxysmal coughing, and copious frothy yellow fluid pouring from the nostrils (>95% mortality). 'Dikkop' ('thick head', the subacute cardiac form) is characterized by hydropericardium and dramatic gelatinous subcutaneous edema bulging out the supraorbital fossae, eyelids, and neck (~50% mortality).",
            True,
            TOPIC
        ),
        (
            "Group A Rotaviruses (family Sedoreoviridae)—a premier cause of neonatal diarrhea in calves, piglets, and foals—possess 11 segments of dsRNA and encode which non-structural glycoprotein that acts as the first discovered 'Viral Enterotoxin' by mobilizing intracellular Ca2+?",
            [
                "NSP4 (Non-structural protein 4, encoded by segment 10)",
                "VP6 (Middle capsid group-specific protein, encoded by segment 6)",
                "VP4 (Protease-cleaved spike protein P-type antigen)",
                "VP7 (Outer capsid glycoprotein G-type antigen)"
            ],
            0,
            "Rotavirus Non-Structural Protein 4 (NSP4) is an endoplasmic reticulum transmembrane glycoprotein and secreted enterotoxin peptide that binds integrin receptors on uninfected crypt cells, activates phospholipase C / IP3, elevates cytosolic Ca2+, and stimulates chloride secretion via calcium-activated chloride channels.",
            True,
            TOPIC
        ),
        (
            "In Infectious Bursal Disease (Gumboro Disease) of chickens, why does infection of chicks BEFORE 2 weeks of age produce catastrophic lifelong humoral immunosuppression (vaccine failures against NDV/IBV) with minimal clinical mortality, whereas infection at 3 to 6 weeks of age produces acute clinical disease, bursal hemorrhage, and high mortality?",
            [
                "Chicks under 2 weeks express no viral receptors in the bursa and replicate virus only in the brain",
                "IBDV selectively destroys actively dividing immature IgM+ B-lymphocyte precursors in the Bursa of Fabricius, permanently ablating the B-cell repertoire in neonates while triggering a massive cytokine storm in 3-to-6-week-old chicks",
                "Chicks under 2 weeks possess mature CD8+ cytotoxic T cells that lyse the thymus instead of the bursa",
                "IBDV replicates exclusively in bone marrow erythroblasts during the first 14 days post-hatch"
            ],
            1,
            "The target cell of IBDV is the actively dividing surface-IgM-bearing (sIgM+) immature B-lymphocyte in the cloacal Bursa of Fabricius. In chicks <2 weeks old, destruction of bursal stem cells prevents seeding of peripheral lymphoid organs (permanent B-cell immunodepletion without severe clinical inflammation). At 3–6 weeks, when the bursa is maximally populated with sIgM+ B cells, massive synchronous cytolysis triggers acute cytokine storm, coagulopathy, and mortality.",
            True,
            TOPIC
        ),
        (
            "How is Equine Infectious Anemia Virus (EIAV, genus Lentivirus) transmitted between horses in the field, and which viral core protein is used as the antigen in the official Coggins Agar Gel Immunodiffusion (AGID) test?",
            [
                "Transmitted biologically by Culicoides midges; Coggins test detects envelope glycoprotein gp90",
                "Transmitted venereally by carrier stallions; Coggins test detects reverse transcriptase p66",
                "Transmitted mechanically on the mouthparts of large biting flies (Tabanus horseflies and Stomoxys stable flies); Coggins test detects antibodies against the group-specific p26 core capsid protein",
                "Transmitted transovarially by Rhipicephalus ticks; Coggins test detects matrix protein p15"
            ],
            2,
            "EIAV is transmitted mechanically via interrupted blood feeding by painful large biting flies (horseflies [Tabanus], deerflies [Chrysops], and stable flies [Stomoxys]) or contaminated needles. Because envelope gp90/gp45 undergo rapid antigenic drift causing recurrent febrile waves, the Coggins AGID test uses the highly conserved major capsid core protein p26.",
            True,
            TOPIC
        ),
        (
            "Small Ruminant Lentiviruses (Maedi-Visna Virus in sheep and Caprine Arthritis Encephalitis Virus in goats) evade host neutralizing antibodies and disseminate into the lungs, mammary gland, joints, and CNS via which classic cellular mechanism coined by Ashley Haase?",
            [
                "Retrograde axonal transport inside peripheral sensory nerve fibers",
                "Erythrocyte surface adsorption via viral hemagglutinin spikes",
                "Free cell-free viremia Complexed with host alpha-2-macroglobulin",
                "The 'Trojan Horse' mechanism (latent proviral DNA inside circulating blood monocytes that activates only when monocytes differentiate into tissue macrophages)"
            ],
            3,
            "Maedi-Visna Virus (MVV) and CAEV infect bone marrow myeloid precursors and circulating blood monocytes, where viral transcription is restricted ('silent' provirus, evading immune detection)—the classic 'Trojan Horse' mechanism. Only when monocytes migrate into target tissues (lung, udder, synovium, choroid plexus) and mature into macrophages does full viral gene expression occur.",
            True,
            TOPIC
        ),
        (
            "In poultry oncology, how is Lymphoid Leukosis (caused by Avian Leukosis Virus, an Alpharetrovirus) pathologically and epidemiologically differentiated from Marek's Disease (caused by Gallid alphaherpesvirus 2)?",
            [
                "Lymphoid Leukosis is a B-cell lymphoma originating in the Bursa of Fabricius in birds >16 weeks old with NO peripheral nerve lesions; Marek's Disease is a T-cell lymphoma occurring from 3–4 weeks of age with peripheral nerve enlargement and bursal atrophy",
                "Lymphoid Leukosis is a T-cell lymphoma causing sciatic nerve paralysis in 4-week-old chicks; Marek's Disease is a B-cell lymphoma restricted to hens >24 weeks old",
                "Lymphoid Leukosis is caused by a DNA herpesvirus shed in feather dander; Marek's Disease is caused by an RNA retrovirus transmitted vertically in egg albumen",
                "Lymphoid Leukosis produces intranuclear Cowdry Type A inclusions in tracheal epithelium; Marek's Disease produces Bollinger bodies in skin"
            ],
            0,
            "Key differential table: Marek's Disease (Alphaherpesvirus) transforms CD4+ T-cells (via Meq), affects young birds (>=3–4 weeks), causes enlargement/yellowing and loss of cross-striations of peripheral nerves (sciatic/brachial plexus) and diffuse bursal atrophy. Lymphoid Leukosis (Alpharetrovirus) transforms IgM+ B-cells via insertional activation of c-myc inside the Bursa of Fabricius (producing nodular bursal tumors), occurs only in sexually mature birds (>16 weeks), and NEVER involves peripheral nerves.",
            True,
            TOPIC
        ),
        (
            "Which subgroup of exogenous Avian Leukosis Virus (ALV)—which emerged in the late 1980s through recombination with endogenous retroviral env sequences—exhibits a unique tropism for myeloid cells and causes 'Myelocytomatosis' (chalky-white tumors on the sternum, ribs, pelvis, and liver) in meat-type broiler breeders?",
            [
                "Avian Leukosis Virus Subgroup A (ALV-A)",
                "Avian Leukosis Virus Subgroup J (ALV-J)",
                "Avian Leukosis Virus Subgroup E (ALV-E, endogenous locus ev)",
                "Reticuloendotheliosis Virus (REV)"
            ],
            1,
            "While classical exogenous ALV subgroups A and B induce B-cell lymphoid leukosis in egg-type layers, ALV Subgroup J (ALV-J) possesses a divergent gp85 envelope glycoprotein (binding the chicken Na+/H+ exchanger 1, chNHE1) and predominantly induces myeloid leukosis (myelocytomatosis) in meat-type broiler breeders.",
            True,
            TOPIC
        ),
        (
            "In point-of-care veterinary diagnostics for feline retroviruses, what specific viral target is detected by the in-clinic ELISA/immunochromatography test for Feline Leukemia Virus (FeLV) versus Feline Immunodeficiency Virus (FIV)?",
            [
                "FeLV test detects anti-gp70 antibodies; FIV test detects free reverse transcriptase antigen",
                "Both FeLV and FIV point-of-care tests detect only host IgM antibodies in saliva",
                "FeLV test detects free soluble p27 core capsid ANTIGEN in blood; FIV test detects host ANTIBODIES against viral p24/gp40",
                "FeLV test detects proviral DNA by agglutination; FIV test detects p27 antigen in tears"
            ],
            2,
            "Viremic FeLV-infected cats shed large excesses of unencapsidated major core protein p27 into plasma, so FeLV rapid tests are sandwich assays detecting p27 ANTIGEN. Conversely, FIV-infected cats have very low plasma viral antigen loads after the acute phase, so FIV rapid tests are indirect/competitive assays detecting anti-FIV ANTIBODIES (against p24 capsid or gp40 transmembrane protein).",
            True,
            TOPIC
        ),
        (
            "Why can a live attenuated Goatpox vaccine (such as the Uttarkashi strain used in India) or Sheeppox vaccine be used for heterologous immunization of cattle against Lumpy Skin Disease (LSD)?",
            [
                "Lumpy Skin Disease virus is actually a Parapoxvirus that shares its envelope with Orf virus",
                "Goatpox virus integrates into the bovine chromosome via reverse transcriptase",
                "Lumpy Skin Disease is caused by Bovine Herpesvirus-2, which cross-reacts with Goatpox",
                "Sheeppox virus, Goatpox virus, and Lumpy Skin Disease virus all belong to the genus Capripoxvirus, share >96% genome identity, and constitute a single cross-protective serological group"
            ],
            3,
            "All three members of the genus Capripoxvirus—Sheeppox virus (SPPV), Goatpox virus (GTPV), and Lumpy Skin Disease virus (LSDV)—cannot be distinguished serologically by virus neutralization and share >96% nucleotide sequence identity, providing strong cross-protection (alongside homologous attenuated LSDV Neethling vaccines).",
            True,
            TOPIC
        ),
        (
            "Contagious Ecthyma ('Orf', 'Scabby Mouth', or 'Contagious Pustular Dermatitis') of sheep and goats is caused by a Parapoxvirus whose virions are immediately distinguished from Orthopoxviruses and Capripoxviruses under negative-stain electron microscopy by their:",
            [
                "Narrow ovoid ('cocoon') shape with surface protein tubules wound in a regular criss-cross ('ball of yarn' / basket-weave) spiral pattern",
                "Icosahedral capsid surrounded by a spiked double lipid envelope resembling a wheel",
                "Bullet-shaped helical nucleocapsid with a flat base and rounded apex",
                "Long filamentous pleomorphic rods measuring over 1,000 nm in length"
            ],
            0,
            "Whereas Orthopoxviruses and Capripoxviruses are large brick-shaped virions (250 x 300 nm) with randomly arranged short surface tubules ('mulberry' form), Parapoxviruses (Orf virus, Pseudocowpox virus, Bovine Papular Stomatitis virus) are smaller, oval/cocoon-shaped (160 x 260 nm) with a single continuous surface tubule wrapped spirally creates a diagnostic criss-cross ('ball of wool') pattern.",
            True,
            TOPIC
        ),
        (
            "In histopathological sections of avian skin infected with Fowlpox Virus (genus Avipoxvirus), hyperplastic and ballooning epidermal prickle cells contain large, eosinophilic intracytoplasmic inclusion bodies termed:",
            [
                "Negri bodies (containing Lyssavirus ribonucleoprotein)",
                "Bollinger bodies (which enclose numerous elementary viral particles called Borrel bodies)",
                "Guarnieri bodies (characteristic of Vaccinia and Cowpox viruses)",
                "Cowdry Type A bodies (characteristic of Infectious Laryngotracheitis virus)"
            ],
            1,
            "Avipoxviruses (Fowlpox, Pigeonpox, Canarypox, Turkeypox) induce massive epidermal hyperplasia containing pathognomonic large, eosinophilic, lipid-rich intracytoplasmic inclusion bodies called Bollinger bodies; when crushed and stained (e.g., Gimenez or Wright stain), Bollinger bodies release individual viral elementary bodies known as Borrel bodies.",
            True,
            TOPIC
        ),
        (
            "Control and eradication programs for Infectious Bovine Rhinotracheitis (BHV-1) and Pseudorabies / Aujeszky's Disease (SuHV-1) in Europe and North America utilize 'Marker Vaccines' (DIVA vaccines) engineered by deleting which non-essential viral envelope glycoprotein gene?",
            [
                "Glycoprotein B (gB, which is essential for viral cell-to-cell fusion and entry)",
                "Glycoprotein D (gD, which is essential for high-affinity receptor binding)",
                "Glycoprotein E (gE, formerly designated gI in Pseudorabies virus)",
                "Major capsid protein VP5 (UL19, which forms the icosahedral hexons and pentons)"
            ],
            2,
            "In both Bovine Alphaherpesvirus 1 (BHV-1) and Suid Alphaherpesvirus 1 (Pseudorabies virus), Glycoprotein E (gE, which complexes with gI to facilitate anterograde axonal spread and cell-to-cell spread) is non-essential for replication in vitro, but is expressed by 100% of wild-type field strains. Deleting the gE gene yields a safe attenuated vaccine whose recipients remain negative on an anti-gE blocking ELISA.",
            True,
            TOPIC
        ),
        (
            "In Marek's Disease of chickens (caused by Gallid alphaherpesvirus 2), although CD4+ T-lymphocytes in visceral tumors and peripheral nerves are latently infected and transformed by the viral 'Meq' oncogene, where is the ONLY anatomical site in the chicken where productive replication of fully enveloped, cell-free infectious virions occurs for horizontal shedding?",
            [
                "The cortical lymphocytes of the Bursa of Fabricius",
                "The Schwann cells of the sciatic and brachial nerve plexuses",
                "The goblet cells of the cecal tonsils and duodenum",
                "The keratinizing Feather Follicle Epithelium (FFE), shed into poultry house dust and dander"
            ],
            3,
            "In lymphoid cells and tumors, Marek's Disease Virus is strictly cell-associated and non-infectious if cells are lysed. Productive lytic replication producing fully enveloped, cell-free, environmentally stable infectious virions occurs EXCLUSIVELY in the stratified squamous Feather Follicle Epithelium (FFE), which sloughs off as infectious feather dander/poultry house dust.",
            True,
            TOPIC
        ),
        (
            "Vaccination against Marek's Disease is routinely performed at the hatchery (either in ovo at day 18 of embryonation or subcutaneously at day 1 of age). How are the three serotypes of Marek's Disease-related avian herpesviruses defined?",
            [
                "Serotype 1: Oncogenic MDV & attenuated CVI988/Rispens; Serotype 2: Naturally apathogenic chicken strain SB-1; Serotype 3: Herpesvirus of Turkeys (HVT, strain FC126)",
                "Serotype 1: Herpesvirus of Turkeys (HVT); Serotype 2: Infectious Laryngotracheitis virus; Serotype 3: Duck Plague virus",
                "Serotype 1: Avian Leukosis virus; Serotype 2: Reticuloendotheliosis virus; Serotype 3: Chicken Anemia virus",
                "Serotype 1: Lentogenic NDV; Serotype 2: Mesogenic NDV; Serotype 3: Velogenic NDV"
            ],
            0,
            "Marek's disease viral group comprises three serotypes: Serotype 1 (Gallid alphaherpesvirus 2) includes all pathogenic/oncogenic field strains and their attenuated derivatives (most notably the gold-standard CVI988 / Rispens vaccine strain); Serotype 2 (Gallid alphaherpesvirus 3) includes naturally non-oncogenic chicken strains (SB-1, 301B/1); and Serotype 3 (Meleagrid alphaherpesvirus 1) is the apathogenic Herpesvirus of Turkeys (HVT, FC126).",
            True,
            TOPIC
        ),
        (
            "'Egg Drop Syndrome 1976' (EDS-76)—characterized by a sudden drop in egg production and laying of pale, thin-shelled, soft-shelled, or shell-less eggs by apparently healthy hens—is caused by Duck Atadenovirus A (family Adenoviridae), which is diagnostically unique among avian adenoviruses because it:",
            [
                "Replicates exclusively in the cytoplasm and produces Bollinger bodies",
                "Directly agglutinates chicken, duck, and turkey erythrocytes, allowing rapid HA and HI testing",
                "Contains a segmented double-stranded RNA genome and requires Culicoides vectors",
                "Causes 100% mortality with hydropericardium ('Leechi disease') in 3-week-old broilers"
            ],
            1,
            "Unlike classical Fowl Aviadenoviruses (FAdV-1 to 12, most of which do not hemagglutinate chicken RBCs), EDS-76 virus (Duck Atadenovirus A) strongly agglutinates avian (chicken, duck, turkey, goose) erythrocytes via its fiber knob protein, making the Hemagglutination Inhibition (HI) test the standard serological assay.",
            True,
            TOPIC
        ),
        (
            "'Hydropericardium Syndrome' ('Angara Disease' or 'Leechi Disease') in 3-to-6-week-old broiler chickens—characterized by sudden mortality (up to 60%), accumulation of clear straw-colored jelly-like fluid in the pericardial sac (giving the heart the appearance of a peeled leechi fruit), and multifocal hepatic necrosis with basophilic intranuclear inclusions—is caused by:",
            [
                "Duck Atadenovirus A (Egg Drop Syndrome-76 virus)",
                "Chicken Anemia Virus (Gyrovirus)",
                "Fowl Aviadenovirus Serotype 4 (FAdV-4, species Fowl aviadenovirus C)",
                "Avian Reovirus (Orthoreovirus)"
            ],
            2,
            "First reported at Angara Goth near Karachi (1987) and termed 'Leechi disease' in India, Hydropericardium-Hepatitis Syndrome is caused specifically by virulent strains of Fowl Adenovirus Serotype 4 (FAdV-4, species Fowl aviadenovirus C), whereas other serotypes (FAdV-2, -8a, -8b, -11) cause classic Inclusion Body Hepatitis (IBH) without severe hydropericardium.",
            True,
            TOPIC
        ),
        (
            "In cattle chronically grazing pastures infested with Bracken Fern (Pteridium aquilinum), which Bovine Papillomavirus (BPV) type acts synergistically with bracken fern carcinogens (ptaquiloside) and quercetin to induce urinary bladder tumors (hemangiomas and transitional cell carcinomas) causing 'Enzootic Bovine Hematuria'?",
            [
                "Bovine Papillomavirus Type 3 (cutaneotropic Xipapillomavirus)",
                "Bovine Papillomavirus Type 6 (teat frond papillomavirus)",
                "Bovine Papillomavirus Type 8",
                "Bovine Papillomavirus Type 2 (BPV-2, whereas BPV-4 induces upper alimentary tract squamous cell carcinoma)"
            ],
            3,
            "Bracken fern contains the immunosuppressant and DNA-alkylating norsesquiterpene glucoside Ptaquiloside. In cattle grazing bracken fern, latent Bovine Papillomavirus Type 2 (BPV-2, a Deltapapillomavirus that also causes equine sarcoids along with BPV-1) is activated in the urothelium and vascular endothelium to cause Enzootic Bovine Hematuria, while BPV-4 causes esophageal/ruminal squamous cell carcinoma.",
            True,
            TOPIC
        ),
        (
            "In gilts and sows exposed oronasally during the first half of pregnancy (before fetal immunocompetence at day 70 of gestation), Porcine Parvovirus (PPV) crosses the placenta and spreads sequentially from fetus to fetus along the uterine horn, causing which classic reproductive syndrome in the absence of maternal illness?",
            [
                "SMEDI Syndrome (Stillbirth, Mummification, Embryonic Death, and Infertility)",
                "Blue Ear Disease with late-term abortion at day 110 and maternal anorexia/cyanosis",
                "Congenital Myoclonia Congenita ('dancing pig disease') and cerebellar hypoplasia",
                "Maternal agalactia, vulvovaginitis, and rectal prolapse"
            ],
            0,
            "Porcine Parvovirus (Ungulate protoparvovirus 1) causes no clinical signs in the pregnant dam, but transplacental infection before day 30 causes embryonic death and resorption (return to service/infertility), infection between days 30 and 70 causes sequential fetal death and mummification of fetuses of progressively different sizes (SMEDI), and fetuses infected after day 70 mount an antibody response and survive.",
            True,
            TOPIC
        ),
        (
            "Aleutian Mink Disease Virus (AMDV, genus Amdoparvovirus, family Parvoviridae) causes a fatal chronic wasting disease in mink and ferrets whose immunopathogenesis is a textbook model of:",
            [
                "IgE-mediated systemic anaphylaxis and mast cell degranulation",
                "Non-neutralizing hypergammaglobulinemia, extreme plasmacytosis, Antibody-Dependent Enhancement (ADE) of macrophage infection, and Type III immune-complex glomerulonephritis/arteritis",
                "Complete aplasia of the thymus and Bursa of Fabricius with agammaglobulinemia",
                "Prion-like amyloid conversion of host neuronal membrane proteins"
            ],
            1,
            "In adult mink (especially homozygous recessive Aleutian 'aa' mink), AMDV replicates in macrophages and stimulates massive polyclonal B-cell activation and hypergammaglobulinemia (>50% of serum protein is anti-viral IgG). Instead of neutralizing the virus, these antibodies mediate Fc-receptor uptake into macrophages (ADE) and deposit in renal glomeruli and arteries as fatal Type III immune complexes.",
            True,
            TOPIC
        ),
        (
            "Chicken Anemia Virus (CAV, genus Gyrovirus, family Anelloviridae) is vertically transmitted from breeder flocks that become infected during egg production and causes 'Blue Wing Disease' in 2-to-3-week-old progeny chicks by selectively destroying which two precursor cell populations?",
            [
                "Bursal B-lymphocytes and intestinal crypt enterocytes",
                "Tracheal ciliated epithelial cells and renal tubular epithelium",
                "Bone marrow hemocytoblasts (causing severe aplastic anemia, pale yellow bone marrow, and hematocrit <20%) and cortical thymocytes (causing thymic atrophy and T-cell immunosuppression)",
                "Cerebellar Purkinje neurons and pancreatic acinar cells"
            ],
            2,
            "Chicken Anemia Virus possesses a circular negative-sense ssDNA genome encoding the apoptin protein (VP3), which selectively induces apoptosis in dividing bone marrow erythroblast/granulocyte/thrombocyte progenitors (hemocytoblasts, causing profound anemia, watery blood, fatty yellow femoral marrow, and subcutaneous hemorrhages) and T-lymphocyte precursors in the thymic cortex.",
            True,
            TOPIC
        ),
        (
            "In Transmissible Spongiform Encephalopathies (Prion diseases such as Scrapie and BSE), the conformational conversion of normal host cellular prion protein (PrPC) into the infectious pathogenic isoform (PrPSc) involves which fundamental change in secondary protein structure without any change in amino acid sequence?",
            [
                "Enzymatic glycosylation and phosphorylation of tyrosine residues by viral kinases",
                "Cleavage of the C-terminal GPI anchor and refolding from beta-sheets into 100% alpha-helices",
                "Covalent cross-linking of cysteine residues to bacterial lipopolysaccharide",
                "Post-translational refolding of alpha-helical domains (~42% alpha-helix in PrPC) into protease-resistant beta-sheet aggregates (~43% beta-sheet in PrPSc)"
            ],
            3,
            "Normal PrPC and infectious PrPSc have the exact same primary amino acid sequence encoded by the host PRNP gene. However, PrPC is monomeric, rich in alpha-helices (~42% alpha-helix, 3% beta-sheet), and completely degraded by Proteinase K, whereas PrPSc acts as a conformational template that refolds PrPC into insoluble fibrils rich in beta-sheets (~43% beta-sheet) whose PrP27-30 core resists Proteinase K.",
            True,
            TOPIC
        ),
        (
            "Genetic susceptibility and resistance of domestic sheep to classical Scrapie is controlled by polymorphisms at three specific codons (136, 154, and 171) of the ovine prion protein gene (PRNP). Which haplotype/genotype confers the highest genetic resistance (targeted by national Scrapie eradication breeding programs), and which confers the highest susceptibility?",
            [
                "ARR/ARR confers maximal resistance; VRQ/VRQ confers maximal susceptibility",
                "VRQ/VRQ confers maximal resistance; ARR/ARR confers maximal susceptibility",
                "ARQ/ARH confers maximal resistance; AHQ/AHQ confers maximal susceptibility",
                "All sheep genotypes are equally susceptible regardless of codons 136, 154, and 171"
            ],
            0,
            "In the ovine 3-codon PRNP classification (codons 136 [A/V], 154 [R/H], and 171 [R/Q/H]): the ARR allele (Alanine-136, Arginine-154, Arginine-171) confers dominant resistance to classical scrapie (homozygous ARR/ARR rams are Type 1 resistant), whereas the VRQ allele (Valine-136, Arginine-154, Glutamine-171) confers extreme susceptibility.",
            True,
            TOPIC
        ),
        (
            "For statutory post-mortem surveillance and confirmatory diagnosis of Bovine Spongiform Encephalopathy (BSE) in cattle and Scrapie in sheep, which specific anatomical region of the brainstem must be harvested (often via the foramen magnum using a specialized spoon) because it is the earliest and most consistent site of vacuolar change and PrPSc accumulation?",
            [
                "The Ammon's horn of the hippocampus and cerebellar vermis",
                "The Obex region of the medulla oblongata (containing the dorsal motor nucleus of the vagus nerve and solitary tract nucleus)",
                "The olfactory bulbs and prefrontal cerebral cortex",
                "The lumbar spinal cord intumescence and dorsal root ganglia"
            ],
            1,
            "Following oral ingestion of prions, PrPSc ascends from the gut-associated lymphoid tissue (ileal Peyer's patches) via parasympathetic fibers of the vagus nerve and sympathetic splanchnic nerves directly to the Dorsal Motor Nucleus of the Vagus (DMNV) located at the level of the Obex in the medulla oblongata, making the obex the mandatory regulatory diagnostic sample.",
            True,
            TOPIC
        ),
        (
            "How does Chronic Wasting Disease (CWD) of deer, elk, and moose differ epidemiologically from Classical Bovine Spongiform Encephalopathy (BSE) in cattle?",
            [
                "CWD is transmitted exclusively via contaminated meat-and-bone meal and never spreads horizontally",
                "CWD prions are restricted strictly to the brain and never enter lymphoid tissues",
                "CWD is efficiently transmitted horizontally from animal to animal and via environmental contamination because PrPCWD accumulates extensively in peripheral lymphoid tissues and is shed in saliva, urine, and feces",
                "CWD is caused by a slow lentivirus rather than a Proteinase K-resistant prion protein"
            ],
            2,
            "In Classical BSE of cattle, PrPSc is largely restricted to the CNS, retina, and distal ileum (Specified Risk Materials), so BSE is not contagious horizontally between cattle and spreads only via contaminated feed. In contrast, CWD in cervids (and classical Scrapie in sheep) exhibits widespread lymphoid replication (tonsils, retropharyngeal lymph nodes, Peyer's patches) and is shed in saliva, urine, feces, and placenta, maintaining horizontal transmission.",
            True,
            TOPIC
        ),
        (
            "Which non-retroviral animal negative-sense single-stranded RNA virus (Order Mononegavirales, family Bornaviridae)—the causative agent of fatal non-suppurative meningoencephalomyelitis ('Sad Horse Disease') with intranuclear Joest-Degen inclusion bodies in horses and sheep—is unique because it replicates and transcribes its genome inside the HOST CELL NUCLEUS?",
            [
                "Rabies Virus (genus Lyssavirus)",
                "Vesicular Stomatitis Virus (genus Vesiculovirus)",
                "Newcastle Disease Virus (genus Orthoavulavirus)",
                "Borna Disease Virus 1 (BoDV-1, genus Orthobornavirus)"
            ],
            3,
            "Unlike Rhabdoviridae, Paramyxoviridae, and Filoviridae (which replicate exclusively in the cytoplasm), Borna Disease Virus (BoDV-1, reservoired in the bicolored white-toothed shrew Crocidura leucodon) replicates and transcribes its -ssRNA genome inside the host cell nucleus, utilizes host nuclear RNA splicing machinery, and forms eosinophilic intranuclear Joest-Degen inclusion bodies in hippocampal neurons.",
            True,
            TOPIC
        ),
        (
            "In Duck Virus Enteritis ('Duck Plague', caused by Anatid alphaherpesvirus 1), necropsy of affected ducks reveals which pathognomonic gross lesions in the gastrointestinal tract?",
            [
                "Annular hemorrhagic bands and raised diphtheritic necrotic rings encircling the mucosal lymphoid zones of the intestine, along with longitudinal necrotic plaques in the esophagus and cloaca",
                "Zebra-striped linear hemorrhages restricted strictly to the rectum and spiral colon",
                "Multiple nodular B-cell tumors in the Bursa of Fabricius and osteopetrosis of the tibiotarsus",
                "Massive dilation of the proventriculus filled with undigested seeds without intestinal hemorrhage"
            ],
            0,
            "Duck Virus Enteritis (Duck Plague, an alphaherpesvirus) has a strong tropism for vascular endothelium and gut-associated lymphoid tissue, producing pathognomonic dark-red annular bands ('hemorrhagic rings') around the four annular lymphoid rings of the duck small intestine (or raised diphtheritic discs in Pekin ducks) and diphtheritic membranes along the longitudinal folds of the esophagus.",
            True,
            TOPIC
        ),
        (
            "Avian Orthoreoviruses (family Reoviridae), the causative agents of 'Viral Arthritis / Tenosynovitis' (rupture of the gastrocnemius tendon above the hock joint) in broiler chickens, are non-enveloped dsRNA viruses that nevertheless induce massive syncytia (cell-cell fusion) in cell culture by expressing which unique viral protein?",
            [
                "A furin-cleaved enveloped F0 fusion glycoprotein spike",
                "A small non-structural Fusion-Associated Small Transmembrane (FAST) protein designated p10",
                "A hemagglutinin-esterase (HE) dimer that degrades plasma membrane cholesterol",
                "An internal myristoylated VP4 capsid protein that lyses host nuclei"
            ],
            1,
            "Fusogenic orthoreoviruses (such as Avian Reovirus and Nelson Bay Reovirus) lack a lipid envelope and have no structural fusion spikes; instead, they encode a tiny (~10 kDa) non-structural membrane-spanning protein called p10 (a FAST protein: Fusion-Associated Small Transmembrane protein) that traffics to the infected cell plasma membrane and drives cell-to-cell syncytium formation.",
            True,
            TOPIC
        ),
        (
            "Crimean-Congo Hemorrhagic Fever Virus (CCHFV, genus Orthonairovirus, family Nairoviridae) is a high-fatality BSL-4 zoonotic pathogen transmitted primarily by Hyalomma ticks. What is the clinical manifestation of CCHFV infection in domestic ruminants (cattle, sheep, and goats)?",
            [
                "Nearly 100% mortality with bloody diarrhea, necrotic stomatitis, and corneal opacity",
                "Severe vesicular lesions on the tongue, dental pad, and interdigital cleft",
                "Subclinical infection with a 1-week viremia (serving as silent amplifying hosts for ticks and a blood-splash hazard)",
                "Progressive hindlimb paralysis and hydropericardium ('heartwater')"
            ],
            2,
            "In cattle, sheep, goats, and ostriches, Crimean-Congo Hemorrhagic Fever Virus causes an inapparent (subclinical) infection with transient viremia lasting ~7 days. Domestic ruminants thus serve as silent amplifying hosts that infect feeding Hyalomma ticks and expose veterinarians and abattoir workers via viremic blood.",
            True,
            TOPIC
        ),
        (
            "Duck Viral Hepatitis Type 1 (DHV-1, genus Avihepatovirus, family Picornaviridae) causes peracute, high-mortality (>90%) infection in young ducklings under 3 weeks of age, characterized clinically and pathologically by:",
            [
                "Chronic bumblefoot, amyloidosis of the spleen, and diphtheritic esophagitis",
                "Slow progressive paralysis of the legs with enlargement of the sciatic nerves",
                "Cystic dilatation of the right oviduct and laying of rough-shelled depigmented eggs",
                "Sudden death in characteristic 'opisthotonos' (head arched backward) with an enlarged, pale liver covered in punctate/ecchymotic hemorrhages"
            ],
            3,
            "Duck Viral Hepatitis Type 1 (Duck Hepatitis A Virus-1, family Picornaviridae) strikes ducklings <3 weeks old with peracute spasmodic paddling and death within an hour in classic opisthotonos (head drawn back over the dorsum), accompanied by an enlarged reddish-yellow liver studded with petechial and ecchymotic hemorrhages.",
            True,
            TOPIC
        ),
        (
            "Vesicular Exanthema of Swine Virus (VESV, genus Vesivirus, family Caliciviridae)—which caused FMD-like vesicular outbreaks in pigs fed raw garbage in California—originated from a marine reservoir virus endemic in Pacific pinnipeds known as:",
            [
                "San Miguel Sea Lion Virus (SMSV)",
                "Phocine Distemper Virus (PDV)",
                "Cetacean Morbillivirus (CeMV)",
                "Elephant Endotheliotropic Herpesvirus (EEHV)"
            ],
            0,
            "Vesicular Exanthema of Swine Virus (VESV, family Caliciviridae) is phylogenetically and antigenically a strain of San Miguel Sea Lion Virus (SMSV) that jumped from marine pinnipeds (sea lions, fur seals) and opaleye fish into swine herds fed uncooked marine offal in swill.",
            True,
            TOPIC
        ),
        (
            "'Louping Ill'—an acute tick-borne viral encephalomyelitis of sheep and red grouse in the British Isles characterized by a biphasic fever and a peculiar bounding, leaping cerebellar ataxia ('louping' gait)—is caused by an Orthoflavivirus transmitted by:",
            [
                "Rhipicephalus appendiculatus (brown ear tick)",
                "Ixodes ricinus (castor bean / sheep tick)",
                "Ornithodoros moubata (soft tampan tick)",
                "Dermacentor reticulatus (ornate cow tick)"
            ],
            1,
            "Louping Ill Virus belongs to the Tick-Borne Encephalitis (TBE) complex in the genus Orthoflavivirus (family Flaviviridae) and is biologically transmitted on heather moorlands by the three-host hard tick Ixodes ricinus, causing fatal polioencephalomyelitis in sheep and willow ptarmigan/red grouse.",
            True,
            TOPIC
        ),
        (
            "In Classical Swine Fever (Hog Cholera), which live attenuated vaccine strain (adapted by hundreds of serial passages in rabbits) is the global gold-standard vaccine, and what is the most pathognomonic gross lesion seen in the spleen of pigs dying of acute CSF?",
            [
                "Mukteswar strain; diffuse splenomegaly with miliary caseous granulomas",
                "Sungri-96 strain; complete atrophy and fibrosis of the splenic white pulp",
                "Lapinized Chinese (C) strain; raised, dark-red wedge-shaped marginal infarcts along the edges of the spleen",
                "Neethling strain; rupture of the splenic capsule with hemoperitoneum"
            ],
            2,
            "The lapinized Chinese ('C') strain of CSFV induces rapid, lifelong immunity within 3–5 days of vaccination. At necropsy of acute Classical Swine Fever, raised dark-red pyramidal infarcts along the margin of the spleen (caused by fibrinoid necrosis of splenic arterioles), 'turkey-egg' petechiated kidneys, and colonic 'button ulcers' are pathognomonic.",
            True,
            TOPIC
        ),
        (
            "'Vomiting and Wasting Disease' (VWD) in suckling piglets under 3 weeks of age—characterized by repeated retching, emaciation, constipation, and encephalomyelitis—is caused by Porcine Hemagglutinating Encephalomyelitis Virus (PHEV), which belongs to:",
            [
                "Family Picornaviridae, genus Enterovirus",
                "Family Arteriviridae, genus Betaarterivirus",
                "Family Circoviridae, genus Circovirus",
                "Family Coronaviridae, genus Betacoronavirus (subgenus Embecovirus)"
            ],
            3,
            "Porcine Hemagglutinating Encephalomyelitis Virus (PHEV) is a Betacoronavirus (expressing a Hemagglutinin-Esterase [HE] glycoprotein that agglutinates chicken/mouse RBCs) that replicates in nasal/tonsillar mucosa and spreads retrogradely via the trigeminal and vagus nerves to the medullary vomiting center and Auerbach's myenteric plexus of the stomach.",
            True,
            TOPIC
        ),
        (
            "While the surface Glycoprotein (G) of Rabies virus is the sole antigen that induces virus-neutralizing antibodies, which internal structural protein is the most abundant, highly conserved group-specific antigen targeted by FITC-conjugated antibodies in the gold-standard Direct Fluorescent Antibody Test (dFAT) on brain impression smears?",
            [
                "Nucleoprotein (N protein, which encapsidates the genomic RNA to form Negri bodies)",
                "Matrix protein (M protein, which lines the inner surface of the viral envelope)",
                "Large protein (L protein, the RNA-dependent RNA polymerase)",
                "Phosphoprotein (P protein, the non-catalytic polymerase cofactor)"
            ],
            0,
            "Rabies virus Nucleoprotein (N) tightly encapsidates the viral RNA and forms the bulk of the cytoplasmic ribonucleoprotein aggregates (Negri bodies). Because the N protein is produced in vast excess and is antigenically conserved across Lyssavirus genotypes, anti-N monoclonal antibodies conjugated to FITC are used in the direct FAT.",
            True,
            TOPIC
        ),
        (
            "Peste des Petits Ruminants Virus (PPRV) and Canine Distemper Virus (CDV) (genus Morbillivirus) infect host lymphocytes (causing profound acute leukopenia and lymphoid depletion) and subsequently infect mucosal epithelial cells (for horizontal shedding) by binding sequentially to which two host cell-surface receptors?",
            [
                "CD4 on T-helper cells, followed by CCR5 on mucosal macrophages",
                "SLAM (Signaling Lymphocyte Activation Molecule / CD150) on immune cells, followed by Nectin-4 on epithelial cells",
                "Sialoadhesin (CD169) on macrophages, followed by CD163 in endosomes",
                "Alpha-v-beta-6 integrin on tongue epithelium, followed by heparan sulfate"
            ],
            1,
            "All Morbilliviruses (Measles, Rinderpest, PPRV, CDV) use SLAM (CD150) expressed on activated T- and B-lymphocytes, macrophages, and dendritic cells as their primary immune receptor (explaining severe morbillivirus-induced immunosuppression), and subsequently use the adherens junction protein Nectin-4 (PVRL4) on the basolateral surface of respiratory/intestinal epithelium for viral exit.",
            True,
            TOPIC
        ),
        (
            "In dogs with acute Canine Distemper, microscopic examination of Giemsa- or Wright-stained peripheral blood smears, conjunctival scrapings, or urinary bladder transitional epithelium frequently reveals eosinophilic intracytoplasmic inclusion bodies known specifically as:",
            [
                "Joest-Degen bodies",
                "Guarnieri bodies",
                "Lentz bodies",
                "Councilman bodies"
            ],
            2,
            "In Canine Distemper Virus (CDV) infection, aggregates of viral nucleocapsid tubules form characteristic round-to-ovoid acidophilic (eosinophilic) intracytoplasmic inclusion bodies called 'Lentz bodies' inside circulating neutrophils, lymphocytes, erythrocytes, and transitional epithelial cells of the urinary bladder and renal pelvis.",
            True,
            TOPIC
        ),
        (
            "During Influenza A virus entry into a host cell following receptor-mediated endocytosis, what is the critical function of the viral Matrix-2 (M2) envelope protein (the target of the antiviral drug Amantadine)?",
            [
                "It cleaves alpha-2,6-sialic acid receptors to release the virion from respiratory mucus",
                "It exports newly synthesized viral mRNAs out of the host cell nucleus via CRM1",
                "It polymerizes complementary positive-sense cRNA templates inside the nucleolus",
                "It forms a proton-selective ion channel (viroporin) that acidifies the virion interior, dissociating M1 matrix protein from the 8 vRNP segments for nuclear import"
            ],
            3,
            "The Influenza A M2 protein is a tetrameric transmembrane proton (H+) channel (viroporin). Inside the acidified late endosome (pH 5.0–6.0), M2 conducts protons into the virion core, disrupting the interaction between Matrix protein M1 and the 8 viral ribonucleoprotein (vRNP) segments so that the vRNPs are released into the cytosol after HA-mediated membrane fusion.",
            True,
            TOPIC
        ),
        (
            "Reticuloendotheliosis Virus (REV, genus Gammaretrovirus) causes runting-stunting syndrome, feathering defects ('Nakanuke'), and lymphomas in poultry, and is uniquely notorious in veterinary vaccine quality control because its proviral DNA can naturally integrate into the genome of which two large avian DNA viruses?",
            [
                "Fowlpox Virus (Avipoxvirus) and Marek's Disease Virus (Gallid alphaherpesvirus 2)",
                "Infectious Bursal Disease Virus (Birnavirus) and Avian Reovirus",
                "Newcastle Disease Virus (Paramyxovirus) and Infectious Bronchitis Virus (Coronavirus)",
                "Chicken Anemia Virus (Gyrovirus) and Goose Parvovirus"
            ],
            0,
            "Reticuloendotheliosis Virus (REV) is an avian gammaretrovirus whose reverse-transcribed LTRs or full-length provirus can spontaneously insert into the large double-stranded DNA genomes of Fowlpox virus and Marek's Disease virus during co-infection of birds or embryo fibroblast cultures, historically causing widespread REV contamination of commercial Fowlpox and HVT vaccines.",
            True,
            TOPIC
        ),
        (
            "Myxoma Virus (genus Leporipoxvirus, family Poxviridae) is a classic textbook example of host-parasite co-evolution. It causes only a benign, localized cutaneous fibroma in its natural reservoir (South American tapeti / Sylvilagus brush rabbits), whereas in European rabbits (Oryctolagus cuniculi) it causes:",
            [
                "Subclinical lifelong enteric shedding without any skin lesions",
                "Fulminant generalized 'Myxomatosis' (mucoid subcutaneous pseudotumors, 'big head' blepharoconjunctivitis, and >99% mortality)",
                "Peracute necrotizing hepatitis and epistaxis within 24 hours without skin nodules",
                "Chronic demyelinating encephalitis and cataracts after a 2-year incubation period"
            ],
            1,
            "Introduced into Australia in 1950 to control feral European rabbits (Oryctolagus cuniculi) and transmitted mechanically by mosquitoes and the rabbit flea (Spilopsyllus cuniculi), Myxoma virus caused >99.8% case fatality in naive Oryctolagus rabbits, before co-evolving toward intermediate virulence Rank III/IV strains alongside rising rabbit genetic resistance.",
            True,
            TOPIC
        ),
        (
            "Bovine Alphaherpesvirus 1 (BHV-1) is divided into restriction-endonuclease subtypes (BHV-1.1, BHV-1.2a, and BHV-1.2b). While BHV-1.1 causes classical respiratory Infectious Bovine Rhinotracheitis (IBR / 'Red Nose'), which clinical venereal syndromes are caused by BHV-1.2b?",
            [
                "Contagious Bovine Pleuropneumonia and ulcerative mammillitis",
                "Malignant Catarrhal Fever and corneoscleral panvasculitis",
                "Infectious Pustular Vulvovaginitis (IPV) in cows and Infectious Pustular Balanoposthitis (IPB) in bulls",
                "Epivaginitis and fibropapillomatosis of the glans penis"
            ],
            2,
            "The exact same virus species—Bovine alphaherpesvirus 1 (BHV-1)—causes both respiratory disease (IBR, primarily subtype 1.1) and venereal genital disease: Infectious Pustular Vulvovaginitis (IPV) in cows and Infectious Pustular Balanoposthitis (IPB) in bulls (primarily subtype 1.2b, which does not cause abortion).",
            True,
            TOPIC
        ),
        (
            "In laying and breeder chickens, acute Infectious Laryngotracheitis (caused by Gallid alphaherpesvirus 1) is clinically and pathologically characterized by gasping ('pump-handle breathing'), expectoration of blood-stained mucus casts, and which pathognomonic histopathological lesion in the tracheal mucosa during the first 1–5 days?",
            [
                "Intracytoplasmic eosinophilic Bollinger bodies inside hyperplastic squamous cells",
                "Crypt epithelial necrosis with large basophilic amphophilic inclusions in Peyer's patches",
                "Granulomatous giant-cell pneumonia with dichotomously branching hyphae",
                "Sloughing multinucleated epithelial syncytia containing eosinophilic intranuclear Cowdry Type A inclusion bodies"
            ],
            3,
            "Infectious Laryngotracheitis Virus (ILTV, Gallid alphaherpesvirus 1) replicates strictly in the respiratory epithelium and conjunctiva (establishing latency in the trigeminal ganglion), inducing fusion of respiratory epithelial cells into multinucleated syncytia that contain prominent eosinophilic intranuclear Cowdry Type A inclusion bodies.",
            True,
            TOPIC
        ),
        (
            "Malignant Catarrhal Fever (MCF) is a fatal, sporadic lymphoproliferative and necrotizing panvasculitis of cattle, water buffaloes, bison, and deer. Which two reservoir species asymptomatically harbor and shed the causative gammaherpesviruses—Alcelaphine gammaherpesvirus 1 (AlHV-1) and Ovine gammaherpesvirus 2 (OvHV-2), respectively?",
            [
                "Blue wildebeest (Connochaetes taurinus) for AlHV-1, and domestic sheep (Ovis aries) for OvHV-2",
                "African Cape buffalo (Syncerus caffer) for AlHV-1, and domestic goats (Capra hircus) for OvHV-2",
                "Dromedary camels for AlHV-1, and wild boars for OvHV-2",
                "Plains zebras for AlHV-1, and red deer for OvHV-2"
            ],
            0,
            "Wildebeest-associated MCF (WA-MCF) in Africa is caused by Alcelaphine gammaherpesvirus 1 (AlHV-1), shed in nasal/ocular secretions of young wildebeest calves up to 3–4 months of age. Sheep-associated MCF (SA-MCF) worldwide is caused by Ovine gammaherpesvirus 2 (OvHV-2), carried asymptomatically by domestic sheep (especially lambs aged 6–9 months); affected cattle are dead-end hosts.",
            True,
            TOPIC
        ),
        (
            "Which bovine herpesvirus causes 'Bovine Herpes Mammillitis' (severe painful vesicles, plaques, and ulcers on the teats and udder skin of first-calf dairy heifers) as well as generalized benign 'Pseudo-Lumpy Skin Disease'?",
            [
                "Bovine Alphaherpesvirus 1 (BHV-1)",
                "Bovine Alphaherpesvirus 2 (BHV-2 / Allerton virus)",
                "Bovine Gammaherpesvirus 4 (BHV-4 / Movar virus)",
                "Bovine Alphaherpesvirus 5 (BHV-5, agent of bovine necrotizing meningoencephalitis)"
            ],
            1,
            "Bovine Alphaherpesvirus 2 (BHV-2, antigenically related to human Herpes Simplex Virus) replicates best at lower skin temperatures (30–35°C) and causes two distinct syndromes: localized ulcerative Bovine Herpes Mammillitis on the teats/udder of periparturient dairy heifers, and generalized superficial skin nodules termed Pseudo-Lumpy Skin Disease (Allerton virus).",
            True,
            TOPIC
        ),
        (
            "Bovine Papillomavirus Types 1 and 2 (BPV-1 and BPV-2, genus Deltapapillomavirus) are unique among all known mammalian papillomaviruses because they can cross the species barrier to infect dermal fibroblasts of horses, donkeys, and mules, causing the most common equine skin tumor known as:",
            [
                "Equine Cutaneous Melanomatosis",
                "Equine Squamous Cell Carcinoma of the third eyelid",
                "Equine Sarcoid (locally invasive, non-metastasizing fibroblastic skin tumor)",
                "Equine Molluscum Contagiosum"
            ],
            2,
            "Unlike strict epitheliotropic papillomaviruses, Deltapapillomaviruses (BPV-1 and BPV-2) infect both epithelium and subepithelial fibroblasts (fibropapillomas in cattle). When transmitted to equids via flies or fomites, BPV-1/BPV-2 non-productively transform equine dermal fibroblasts via the E5 and E6/E7 oncoproteins, producing locally aggressive Equine Sarcoids.",
            True,
            TOPIC
        ),
        (
            "'Derzsy's Disease'—a highly contagious, fatal viral disease of young goslings and Muscovy ducklings (aged 1 to 4 weeks) characterized by fibrinous perihepatitis, ascitic fluid accumulation ('water belly'), hydropericardium, and degenerative myocarditis—is caused by:",
            [
                "Duck Atadenovirus A",
                "Goose Hemorrhagic Polyomavirus",
                "Anatid Alphaherpesvirus 1",
                "Goose Parvovirus (Anseriform dependoparvovirus 1)"
            ],
            3,
            "Derzsy's disease (Goose Plague / Goose Hepatitis) is caused by Goose Parvovirus (and Muscovy Duck Parvovirus). Although classified taxonomically in the genus Dependoparvovirus, it replicates autonomously without any helper virus in rapidly dividing myocardial, hepatic, and intestinal cells of goslings and Muscovy ducklings.",
            True,
            TOPIC
        ),
        (
            "Feline Spongiform Encephalopathy (FSE) in domestic cats and captive cheetahs, as well as Variant Creutzfeldt-Jakob Disease (vCJD) in humans, emerged in the United Kingdom during the 1990s as a direct consequence of dietary exposure to which prion strain?",
            [
                "Classical Bovine Spongiform Encephalopathy (BSE) prions in contaminated beef byproducts and meat-and-bone meal",
                "Classical Ovine Scrapie (VRQ) prions in raw mutton offal",
                "Cervid Chronic Wasting Disease (CWD) prions in venison pet food",
                "Transmissible Mink Encephalopathy (TME) prions in fish meal"
            ],
            0,
            "Glycosylation profiling and strain typing in inbred mice proved that Feline Spongiform Encephalopathy (FSE), Exotic Ungulate Encephalopathy (in zoo nyala/kudu), and human Variant Creutzfeldt-Jakob Disease (vCJD) were all caused by the exact same prion strain—Classical Bovine Spongiform Encephalopathy (BSE)—transmitted orally via contaminated feed/food.",
            True,
            TOPIC
        ),
        (
            "In respiratory infections of turkeys and broiler chickens, Avian Metapneumovirus (aMPV, family Pneumoviridae)—the primary etiological agent of 'Turkey Rhinotracheitis' (TRT) and chicken 'Swollen Head Syndrome' (SHS)—differs from Newcastle Disease Virus (Paramyxoviridae) because aMPV envelope glycoproteins:",
            [
                "Possess strong neuraminidase activity but lack fusion (F) protein",
                "Lack both hemagglutinating (HA) and neuraminidase (NA) activities (so it does NOT agglutinate chicken RBCs)",
                "Directly agglutinate horse and pig erythrocytes at 37°C",
                "Contain a segmented 8-piece negative-sense RNA genome"
            ],
            1,
            "Members of the family Pneumoviridae (Avian Metapneumovirus [aMPV] and Bovine Respiratory Syncytial Virus [BRSV]) possess attachment (G) and fusion (F) surface glycoproteins that lack both hemagglutinin and neuraminidase activity; therefore, unlike NDV and Avian Influenza, aMPV cannot be detected by the Hemagglutination (HA) test.",
            True,
            TOPIC
        ),
        (
            "In cats presenting with acute upper respiratory tract infection ('Cat Flu'), how is Feline Herpesvirus-1 (FHV-1 / Feline Viral Rhinotracheitis) clinically distinguished from Feline Calicivirus (FCV)?",
            [
                "FHV-1 causes exclusively chronic stomatitis and acute febrile 'limping syndrome' (polyarthritis)",
                "FHV-1 is a non-enveloped RNA virus that persists on dry surfaces for over 30 days",
                "FHV-1 causes severe keratitis with pathognomonic branching 'dendritic corneal ulcers' and turbinate bone osteolysis",
                "FHV-1 causes systemic virulent hemorrhagic fever with subcutaneous edema of the face and paws"
            ],
            2,
            "Feline Herpesvirus-1 (Felid alphaherpesvirus 1) replicates in conjunctival, corneal, and nasal respiratory epithelium, causing severe rhinotracheitis, turbinate erosion, and pathognomonic branching 'dendritic corneal ulcers' (stained with fluorescein), whereas Feline Calicivirus (FCV) characteristically causes oral/lingual vesicles and ulcers, chronic gingivostomatitis, and acute febrile lameness ('limping kitten syndrome').",
            True,
            TOPIC
        ),
        (
            "Why do modern commercial parenteral dog vaccines utilize live attenuated Canine Adenovirus Type 2 (CAV-2, the respiratory kennel-cough virus) rather than attenuated Canine Adenovirus Type 1 (CAV-1) to protect dogs against Infectious Canine Hepatitis (Rubarth's Disease)?",
            [
                "CAV-1 cannot be propagated in any mammalian cell culture line in vitro",
                "CAV-1 provides immunity lasting less than 14 days and requires weekly boosters",
                "CAV-2 also protects dogs against Canine Parvovirus-2 and Canine Distemper Virus",
                "Attenuated CAV-1 vaccines replicate in corneal endothelium and kidneys, causing post-vaccinal 'Blue Eye' (Type III hypersensitivity anterior uveitis/corneal edema) and urinary viral shedding, whereas CAV-2 cross-protects against CAV-1 without causing 'Blue Eye'"
            ],
            3,
            "Live attenuated CAV-1 vaccines occasionally localized in the anterior uvea and corneal endothelium, triggering an Arthus-like Type III immune-complex reaction ('Blue Eye' corneal opacity) and interstitial nephritis with urine shedding. Because CAV-2 (which is restricted to respiratory epithelium) shares cross-protective hexon/fiber neutralizing epitopes with CAV-1, CAV-2 vaccines protect against both ICH and kennel cough without ocular or renal side effects.",
            True,
            TOPIC
        ),
        (
            "The circular single-stranded DNA genome (~1.76 kb) of Porcine Circovirus Type 2 (PCV2) has an 'ambisense' organization containing two major open reading frames (ORF1 and ORF2). Which gene encodes the immunodominant viral Capsid protein expressed in recombinant baculovirus systems to produce commercial Virus-Like Particle (VLP) subunit vaccines?",
            [
                "ORF2 (the cap gene on the complementary strand, encoding the 27.8-kDa Capsid protein)",
                "ORF1 (the rep gene on the viral strand, encoding the replication-associated proteins Rep and Rep')",
                "ORF3 (encoding a non-structural apoptotic protein)",
                "The VP2 hypervariable region located on segment A"
            ],
            0,
            "PCV2 is the smallest autonomously replicating animal virus (~1,767–1,768 nt circular ambisense ssDNA). ORF1 on the viral sense strand encodes Rep/Rep' replicase proteins, while ORF2 on the complementary anti-sense strand encodes the sole structural Capsid (Cap) protein, which self-assembles into highly immunogenic 60-subunit icosahedral Virus-Like Particles (VLPs) in insect cells.",
            True,
            TOPIC
        ),
        (
            "Why did the natural emergence and widespread circulation of Porcine Respiratory Coronavirus (PRCV) in European and North American pig herds in the 1980s lead to the dramatic spontaneous disappearance of clinical Transmissible Gastroenteritis (TGE), while failing to protect herds against Porcine Epidemic Diarrhea Virus (PEDV)?",
            [
                "PRCV is a bacteriophage that selectively lyses enteric coronaviruses in the porcine stomach",
                "PRCV is a natural Spike (S) deletion mutant of TGEV that induces lactogenic anti-TGEV antibodies",
                "PRCV permanently downregulates porcine aminopeptidase N (pAPN) receptors on villous enterocytes",
                "PRCV integrates into the porcine germ line and confers CRISPR-like immunity against all coronaviruses"
            ],
            1,
            "Porcine Respiratory Coronavirus (PRCV) arose naturally via a 621–681 nucleotide deletion near the 5' end of the TGEV Spike (S) gene, shifting tissue tropism from small intestinal villous enterocytes to respiratory epithelium. Subclinical respiratory PRCV infection acts as a natural vaccine that primes gilts to secrete anti-TGEV lactogenic antibodies, but offers zero cross-protection against PEDV.",
            True,
            TOPIC
        ),
        (
            "In equine respiratory and reproductive virology, why does Equine Herpesvirus 1 (EHV-1) frequently cause late-term 'abortion storms' (at 8–11 months of gestation) and myeloencephalopathy, whereas closely related Equine Herpesvirus 4 (EHV-4) remains primarily restricted to upper respiratory rhinopneumonitis in foals?",
            [
                "EHV-4 lacks a double-stranded DNA genome and cannot replicate at 38°C",
                "EHV-4 infects only B-lymphocytes in the spleen without entering the nasal cavity",
                "EHV-1 establishes a high-grade cell-associated viremia in CD8+ T-cells/monocytes that infects uterine endometrial and CNS vascular endothelium",
                "EHV-4 is transmitted exclusively by Culicoides biting midges during winter months"
            ],
            2,
            "While EHV-4 replication is generally confined to the respiratory tract mucosa and regional lymph nodes, EHV-1 invades circulating leukocytes (T-lymphocytes and monocytes) to produce a cell-associated viremia that seeds vascular endothelial cells of the pregnant uterus (causing placental thrombosis and late-term abortion of fresh fetuses with hepatic necrotic foci) and spinal cord.",
            True,
            TOPIC
        )
    ]


