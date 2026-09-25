# scripts/micro_mod4_immunology.py
# Module 4: Veterinary Immunology, Serology & Vaccinology (45 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module4_questions():
    qs = [
        # 1-10: Immunoglobulins & maternal immunity
        ("In ruminants (cattle, sheep, goats), the predominant immunoglobulin class present in colostrum is:",
         ["IgG1 (selectively transported across the mammary alveolar epithelium via FcRn receptors)", "IgA", "IgM", "IgE"],
         0, "Unlike monogastric species (where secretory IgA predominates in milk), ruminant colostrum is dominated by IgG1 (comprising >80-85% of total colostral immunoglobulins), actively transcytosed from maternal serum into colostrum during late gestation via the neonatal Fc receptor (FcRn).",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The phenomenon of 'Gut Closure' (cessation of macromolecular absorption of intact colostral immunoglobulins) in newborn calves and foals is completed by approximately:",
         ["24 to 36 hours after birth (with highest absorption efficiency in the first 4-6 hours)", "6 hours", "3 to 5 days", "2 weeks"],
         0, "Newborn enterocytes absorb intact colostral immunoglobulins by non-specific pinocytosis; intestinal permeability drops dramatically after 12 hours and is completely closed by 24-36 hours as specialized fetal enterocytes are replaced by mature cells.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The definitive diagnosis of Failure of Passive Transfer (FPT) in a 24-hour-old dairy calf is confirmed when serum IgG concentration drops below:",
         ["10 mg/mL (1000 mg/dL)", "2 mg/mL", "25 mg/mL", "50 mg/mL"],
         0, "Adequate passive transfer in calves is defined as a serum IgG concentration >10 mg/mL (or total serum protein >= 5.5 g/dL on refractometry); levels below 10 mg/mL represent FPT, predisposing to fatal colisepticemia and diarrhea.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Secretory IgA (sIgA) present in tears, saliva, and intestinal secretions is protected from proteolytic cleavage in the gastrointestinal lumen by the presence of the:",
         ["Secretory Component (SC, derived from cleaved polymeric immunoglobulin receptor / pIgR)", "J (joining) chain", "Hypervariable loop", "Disulfide bridge"],
         0, "Polymeric IgA dimers containing a J-chain bind the polymeric immunoglobulin receptor (pIgR) on the basolateral surface of epithelial cells; upon transcytosis, pIgR is cleaved, leaving the Secretory Component wrapped around the IgA hinge region, shielding it from proteases.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The primary immunoglobulin class responsible for activating the Classical Pathway of the Complement cascade with the highest molecular efficiency is:",
         ["IgM (a pentamer requiring only a single molecule to bind C1q)", "IgG4", "IgA", "IgD"],
         0, "Complement component C1q requires binding to at least two adjacent Fc regions to become activated. A single pentameric IgM molecule in 'staple' conformation on an antigen provides all required Fc sites, making it ~1000x more efficient than IgG.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The antigen-binding site (paratope) of an antibody molecule is formed by the spatial combination of the:",
         ["Hypervariable regions (Complementarity-Determining Regions / CDRs) of both the Heavy and Light variable domains", "Constant regions of the Heavy chain only", "Fc domain", "CH2 and CH3 domains"],
         0, "Each variable domain (VH and VL) contains three hypervariable loops termed Complementarity-Determining Regions (CDR1, CDR2, CDR3); together, these six loops fold to create the unique three-dimensional antigen-binding surface (paratope).",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Monoclonal antibodies were originally produced by Georges Köhler and César Milstein (1975) utilizing 'Hybridoma Technology', which involves fusing:",
         ["Antigen-primed splenic B-lymphocytes with immortal non-secreting myeloma cells using Polyethylene Glycol (PEG)", "T-lymphocytes with macrophages", "Plasma cells with fibroblasts", "Erythrocytes with stem cells"],
         0, "Köhler and Milstein fused normal antibody-producing spleen B-cells (which have a finite lifespan) with mutant hypoxanthine-guanine phosphoribosyltransferase-deficient (HGPRT-) myeloma cells, creating immortal hybridomas secreting a single monoclonal antibody.",
         True, "Immunological Techniques (ICAR PG PYQ)"),

        ("The selective medium utilized to culture hybridoma cells while killing unfused myeloma cells is HAT medium, which contains:",
         ["Hypoxanthine, Aminopterin, and Thymidine", "Histamine, Ampicillin, and Tryptophan", "Heparin, Actinomycin, and Threonine", "Hyaluronic acid and Tetracycline"],
         0, "Aminopterin blocks de novo purine and pyrimidine synthesis; unfused HGPRT-deficient myeloma cells cannot utilize the salvage pathway and die, while hybridomas inherit functional HGPRT from spleen cells, surviving on hypoxanthine and thymidine.",
         True, "Immunological Techniques (ICAR PG PYQ)"),

        ("Neonatal Isoerythrolysis (NI / 'Jaundiced Foal Syndrome') in thoroughbred foals is an alloimmune hemolytic disorder resulting from ingestion of maternal colostrum containing antibodies against which foal erythrocyte antigens?",
         ["Aa and Qa blood group antigens", "Ca and Da", "Ua and Ka", "X and Y antigens"],
         0, "In equines, Aa-negative or Qa-negative mares bred to Aa-positive or Qa-positive stallions produce antibodies against fetal RBCs; when the newborn foal suckles colostrum, anti-Aa or anti-Qa alloantibodies cause acute, massive extravascular and intravascular hemolysis.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Which domestic animal species exhibits an 'epitheliochorial' placenta that completely prevents any transplacental transfer of maternal immunoglobulins to the fetus during gestation?",
         ["Horses and Pigs (and synepitheliochorial in Ruminants)", "Dogs and Cats (endotheliochorial)", "Primates (hemochorial)", "Rodents"],
         0, "In mares, sows (epitheliochorial, 6 tissue layers separating maternal and fetal blood), and ruminants (synepitheliochorial), no maternal immunoglobulins cross the intact placenta, making newborn survival 100% dependent on colostral intake.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        # 11-20: Complement, MHC, cytokines
        ("The classical C3 convertase enzyme complex formed during the Classical Complement pathway is composed of:",
         ["C4b2a", "C3bBb", "C4b2a3b", "C5b67"],
         0, "Activated C1s cleaves C4 into C4a and C4b, and C2 into C2a and C2b; C4b and C2a associate on the cell membrane to form C4b2a, which functions as the active C3 convertase of the classical and lectin pathways.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The Alternative Complement pathway is initiated independently of antigen-antibody complexes by the spontaneous hydrolysis of C3 and activation by microbial surfaces, using which C3 convertase?",
         ["C3bBb (stabilized by Properdin)", "C4b2a", "C1qrs", "C5a"],
         0, "Spontaneous tick-over of C3 generates C3(H2O), which binds Factor B; cleavage by Factor D forms C3bBb, the alternative pathway C3 convertase, which is stabilized against rapid decay by binding Properdin (Factor P).",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The Membrane Attack Complex (MAC), which inserts into lipid membranes to form transmembrane hydrophilic pores causing osmotic lysis of target pathogens, is composed of:",
         ["C5b, C6, C7, C8, and multiple C9 molecules (C5b-9 complex)", "C1q, C1r, C1s", "C3a and C5a", "C4b and C2a"],
         0, "C5 convertase cleaves C5 into C5a and C5b; C5b sequentially recruits C6, C7, and C8, and induces polymerisation of 10 to 18 C9 molecules to assemble a tubular channel (MAC / C5b-9) that causes osmotic cell lysis.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The two potent cleavage fragments of complement that function as 'Anaphylatoxins' (inducing mast cell degranulation, smooth muscle contraction, and increased vascular permeability) are:",
         ["C3a and C5a", "C3b and C4b", "C2b and C4a", "C1q and C1s"],
         0, "C3a and C5a are anaphylatoxins that bind specific G-protein-coupled receptors on mast cells and basophils, triggering immediate degranulation and histamine release; C5a is additionally a potent neutrophil chemoattractant.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The complement fragment that acts as the primary 'Opsonin' by binding covalently to microbial cell surfaces and being recognized by CR1 receptors on phagocytes is:",
         ["C3b (and iC3b)", "C3a", "C5a", "C9"],
         0, "C3 convertase cleaves millions of C3 molecules into C3b; reactive thioester bonds in C3b covalently attach to hydroxyl/amino groups on bacterial surfaces, binding CR1 receptors on macrophages and stimulating avid phagocytosis.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Major Histocompatibility Complex (MHC) Class I molecules are expressed on:",
         ["All nucleated cells of the body, and present endogenous (viral/intracellular) peptide antigens to CD8+ Cytotoxic T-lymphocytes (CTLs)", "Antigen-presenting cells exclusively", "Erythrocytes only", "B-lymphocytes only"],
         0, "MHC Class I (composed of a polymorphic alpha chain non-covalently associated with invariant beta-2 microglobulin) is expressed on virtually all nucleated cells, presenting endogenous peptides degraded by the proteasome to CD8+ T cells.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("MHC Class II molecules present exogenous peptide antigens to CD4+ T-helper lymphocytes and are constitutively expressed on:",
         ["Professional Antigen-Presenting Cells (Dendritic cells, Macrophages, and B-lymphocytes)", "All nucleated cells", "Mature erythrocytes and platelets", "Skeletal myocytes only"],
         0, "MHC Class II heterodimers (alpha and beta chains) are restricted to professional APCs; exogenous antigens are endocytosed, degraded in lysosomes, loaded onto MHC Class II (following CLIP displacement), and presented to CD4+ Th cells.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The major cytokine secreted by activated CD4+ Th1 lymphocytes that serves as the master activator of macrophages and driver of cell-mediated immunity is:",
         ["Interferon-gamma (IFN-gamma)", "Interleukin-4 (IL-4)", "Interleukin-10 (IL-10)", "Interleukin-13 (IL-13)"],
         0, "IFN-gamma is the signature Th1 cytokine; it activates classical M1 macrophages, upregulates MHC Class II, stimulates inducible nitric oxide synthase (iNOS), and drives IgG2a class-switching in mice/cattle against intracellular pathogens.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Interleukin-2 (IL-2), synthesized primarily by activated T-helper cells, functions biologically as the essential autocrine and paracrine growth factor for:",
         ["T-lymphocyte clonal proliferation and survival", "Neutrophil maturation in bone marrow", "Mast cell degranulation", "Platelet aggregation"],
         0, "Upon T-cell receptor engagement, activated T-cells synthesize IL-2 and express the high-affinity trimeric IL-2 receptor (CD25 / alpha chain), stimulating autocrine proliferation and expansion of antigen-specific T-cell clones.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Interleukin-4 (IL-4) secreted by CD4+ Th2 lymphocytes drives antibody class-switching in B-lymphocytes towards which immunoglobulin class?",
         ["IgE (and IgG1 in mice / IgG4 in humans)", "IgM", "IgD", "IgA only"],
         0, "IL-4 is the master cytokine directing Th2 responses; it instructs activated B-cells to undergo heavy-chain class-switch recombination to IgE, mediating defense against helminth parasites and driving allergic Type I reactions.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        # 21-30: Hypersensitivity reactions (Gell and Coombs)
        ("In the Gell and Coombs classification of hypersensitivity reactions, Type I Hypersensitivity is mediated by:",
         ["IgE antibodies cross-linking on the surface of tissue mast cells and blood basophils, triggering immediate degranulation", "IgG and IgM antibodies activating complement on cell surfaces", "Deposition of circulating soluble immune complexes in blood vessel walls", "Sensitized CD4+ and CD8+ T-lymphocytes (cell-mediated)"],
         0, "Type I (immediate/anaphylactic) hypersensitivity occurs within minutes of re-exposure to an allergen; multivalent allergen cross-links high-affinity Fc-epsilon-RI-bound IgE on mast cells, releasing preformed histamine, heparin, and leukotrienes.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Systemic Anaphylaxis in domestic animals exhibits species-specific 'shock organs' (the primary organ that fails during acute anaphylactic collapse). In the dog, the primary shock organ is the:",
         ["Hepatic veins (hepatic venous sphincter contraction causing massive portal venous pooling and splanchnic shock)", "Lungs (bronchospasm)", "Heart (coronary occlusion)", "Kidney"],
         0, "In dogs, the smooth muscle of the hepatic sublobular and central veins is exceptionally sensitive to histamine; contraction creates a hepatic 'sluice-valve' obstruction, pooling 60% of circulating blood volume in the splanchnic bed.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("In cattle, sheep, and horses, the primary shock organ during acute systemic anaphylaxis is the:",
         ["Lungs (pulmonary edema, bronchospasm, and pulmonary hypertension)", "Liver", "Spleen", "Urinary bladder"],
         0, "In ruminants and equines, pulmonary smooth muscle and pulmonary venules are the primary target organs; anaphylaxis manifests as intense bronchospasm, alveolar emphysema, pulmonary edema, and acute respiratory dyspnea.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Which of the following clinical conditions in domestic animals is a classic manifestation of Type II (Cytotoxic / Antibody-mediated) Hypersensitivity?",
         ["Immune-Mediated Hemolytic Anemia (IMHA) and Neonatal Isoerythrolysis", "Flea allergy dermatitis", "Glomerulonephritis", "Tuberculin skin reaction"],
         0, "Type II hypersensitivity involves IgG or IgM antibodies directed against surface antigens on target cells (e.g. anti-erythrocyte antibodies in IMHA), leading to complement-mediated lysis or Fc-mediated opsonophagocytosis by splenic macrophages.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Type III Hypersensitivity (Immune-Complex mediated) produces tissue injury fundamentally through the deposition of:",
         ["Soluble antigen-antibody complexes formed in slight antigen excess, which activate complement and attract neutrophils in vessel walls", "Mast cell granules directly", "Sensitized cytotoxic T-lymphocytes", "Precipitated calcium crystals"],
         0, "When soluble immune complexes form in moderate antigen excess, they evade clearing by phagocytes and lodge in vessel walls (glomeruli, synovium, skin), activating complement; C5a recruits neutrophils whose released proteases digest vessel walls (fibrinoid necrosis).",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The local Arthus reaction, producing acute hemorrhagic necrotizing vasculitis in the skin within 4 to 8 hours after booster vaccination, is an experimental prototype of:",
         ["Type III hypersensitivity", "Type I hypersensitivity", "Type II hypersensitivity", "Type IV hypersensitivity"],
         0, "The Arthus reaction occurs when an animal with high circulating IgG antibody titers receives an intradermal injection of antigen; localized immune complexes deposit in dermal microvessels, activating complement and neutrophils.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("'Corneal Opacity' ('Blue Eye') observed in dogs recovering from Canine Adenovirus Type 1 (CAV-1 / Infectious Canine Hepatitis) is a classic example of:",
         ["Type III hypersensitivity (immune-complex deposition in the anterior chamber and corneal endothelial cells)", "Type I immediate allergic reaction", "Direct viral cytolysis of the retina", "Bacterial endophthalmitis"],
         0, "In CAV-1 infection, circulating viral antigen-antibody complexes deposit in the anterior uveal tract and corneal endothelium; complement activation causes severe anterior uveitis and fluid influx into the corneal stroma ('blue eye').",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("The Tuberculin Test (Mantoux / Intradermal test) used for detecting bovine tuberculosis is a classic diagnostic application of:",
         ["Type IV Hypersensitivity (Delayed-Type Hypersensitivity / DTH)", "Type I immediate hypersensitivity", "Type II cytotoxic hypersensitivity", "Type III immune complex hypersensitivity"],
         0, "Type IV hypersensitivity is cell-mediated and antibody-independent; sensitized memory CD4+ Th1 cells recognize tuberculin PPD presented on dendritic cells, releasing cytokines (IFN-gamma) that recruit and activate macrophages, peaking at 48-72 hours.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Allergic Contact Dermatitis in dogs (e.g. from flea collars, carpet dyes, or topical medications) is mediated by low-molecular-weight chemical substances termed:",
         ["Haptens (which are non-immunogenic alone, but become immunogenic upon covalently binding host epidermal proteins)", "Complete antigens", "Superantigens", "Adjuvants"],
         0, "Haptens are low-molecular-weight reactive chemicals that cannot induce an immune response alone; upon skin contact, they penetrate the stratum corneum and conjugate to host self-proteins, forming neo-antigens that activate Langerhans cells (Type IV reaction).",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Bovine Atopic Rhinitis ('Enzootic Nasal Granuloma' / 'Summer Snuffles') in Jersey and Guernsey cattle is pathologically classified as an allergy mediated by:",
         ["Type I hypersensitivity to inhaled fungal spores or plant pollens, characterized by eosinophilic mast-cell-rich nasal polyps", "Type IV granulomatous infection by Mycobacterium", "Direct viral lysis by BRSV", "Bacterial osteomyelitis"],
         0, "Summer snuffles is an allergic rhinitis characterized by localized mucosal edema, multiple nodular polyps in the anterior nasal cavity, and intense infiltration of eosinophils and mast cells driven by IgE against inhaled environmental allergens.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        # 31-40: Serological assays, Vaccinology & Adjuvants
        ("The 'Prozone Phenomenon' observed during antibody titration in agglutination and precipitation assays is characterized by:",
         ["Absence of visible agglutination or precipitation at high serum antibody concentrations (low dilutions) due to extreme antibody excess", "Absence of precipitation at extreme antigen excess", "Spontaneous lysis of all red blood cells", "Complete denaturation of antibodies"],
         0, "In the prozone (antibody excess), every antigenic determinant is bound by a separate bivalent antibody molecule without cross-linking; only when serum is diluted to the 'zone of equivalence' can extensive multivalent lattice networks precipitate or agglutinate.",
         True, "Diagnostic Immunology (ICAR PG PYQ)"),

        ("In competitive Enzyme-Linked Immunosorbent Assay (cELISA), an increase in the concentration of target antibody in the patient's test serum results in:",
         ["A decrease in the final color intensity (optical density / OD) developed by the enzyme-substrate reaction", "An increase in final optical density", "Precipitation of a visible agar ring", "Lysis of indicator erythrocytes"],
         0, "In competitive ELISA, antibodies in the test serum compete with an enzyme-labeled monoclonal antibody for binding to a fixed antigen; higher patient antibody levels block the conjugated antibody, resulting in lower final absorbance.",
         True, "Diagnostic Immunology (ICAR PG PYQ)"),

        ("In Western Blotting (Immunoblotting), after proteins are resolved by SDS-PAGE, they are electrotransferred onto which solid support membrane for antibody probing?",
         ["Nitrocellulose or Polyvinylidene Fluoride (PVDF) membrane", "Agarose gel plate", "Cellulose acetate paper", "Filter paper disc"],
         0, "Western blotting transfers denatured, separated proteins from polyacrylamide gels onto microporous nitrocellulose or PVDF membranes, which have high non-specific protein-binding capacity, allowing subsequent probing with primary and enzyme-conjugated secondary antibodies.",
         True, "Immunological Techniques (ICAR PG PYQ)"),

        ("The Coombs Test (Direct Antiglobulin Test / DAT) is the definitive serological test used to diagnose Immune-Mediated Hemolytic Anemia (IMHA) in dogs by detecting:",
         ["Sub-agglutinating host antibodies (IgG/IgM) and/or complement component C3b already bound to the patient's erythrocyte surface", "Free unconjugated bilirubin in serum", "Antinuclear antibodies in plasma", "Fibrin degradation products"],
         0, "Coombs reagent consists of species-specific anti-canine IgG, IgM, and C3 antibodies; when added to washed patient erythrocytes that are coated with non-agglutinating autoantibodies, Coombs reagent bridges adjacent RBCs, producing visible agglutination.",
         True, "Diagnostic Immunology (ICAR PG PYQ)"),

        ("A 'Toxoid' vaccine (such as Tetanus Toxoid or Clostridium perfringens Toxoid) is prepared by treating bacterial exotoxins with:",
         ["Formalin (0.2% to 0.4% formaldehyde) at 37°C to destroy toxicity while preserving immunogenicity", "Glutaraldehyde at 100°C", "Ether and chloroform", "Gamma radiation"],
         0, "Formalin treatment cross-links amino groups in protein toxins, irreversibly inactivating the lethal enzymatic activity while preserving the natural three-dimensional tertiary conformation of antigenic epitopes, creating a safe, highly immunogenic toxoid.",
         True, "Vaccinology (ICAR PG PYQ)"),

        ("Freund's Complete Adjuvant (FCA) is one of the most potent experimental adjuvants known, composed of mineral oil, an emulsifying agent (mannide monooleate), and:",
         ["Heat-killed, dried Mycobacterium tuberculosis (or M. butyricum) cells", "Live attenuated Brucella cells", "Purified endotoxin (LPS)", "Aluminum hydroxide crystals"],
         0, "Freund's Incomplete Adjuvant (FIA) contains only water-in-oil emulsion; Freund's Complete Adjuvant (FCA) adds killed Mycobacteria, whose cell wall muramyl dipeptide binds NOD2, stimulating intense Th1-driven cell-mediated immunity and granuloma formation.",
         True, "Vaccinology (ICAR PG PYQ)"),

        ("Aluminum hydroxide and Aluminum phosphate (Alum adjuvants), the most widely used adjuvants in commercial veterinary vaccines, enhance immunity primarily by:",
         ["Creating a slow-release antigen depot at the injection site and promoting a Th2-biased humoral antibody response", "Directly stimulating cytotoxic CD8+ T-cells to lyse virus-infected cells", "Acting as viral DNA polymerases", "Destroying regulatory T-cells"],
         0, "Alum adjuvants adsorb protein antigens onto particulate mineral gels, providing a physical depot for sustained antigen release, activating the NLRP3 inflammasome in dendritic cells, and selectively driving strong IgG1 and Th2 antibody responses.",
         True, "Vaccinology (ICAR PG PYQ)"),

        ("In veterinary vaccinology, the 'Marker Vaccine' (DIVA vaccine: Differentiating Infected from Vaccinated Animals) concept requires which critical combination?",
         ["A vaccine with a deleted non-essential gene (e.g. gE-deleted Pseudorabies vaccine) used alongside a companion diagnostic ELISA that detects antibodies against the deleted protein", "A vaccine with green fluorescent protein added", "A vaccine that uses live human pathogens", "A vaccine given only by oral route"],
         0, "DIVA vaccines lack a specific non-essential viral protein (e.g. glycoprotein E deleted from Aujeszky's disease virus or BoHV-1); vaccinated animals produce antibodies to all antigens except gE, while field-infected animals produce anti-gE antibodies, detectable by companion gE-ELISA.",
         True, "Vaccinology (ICAR PG PYQ)"),

        ("DNA vaccines (plasmid DNA immunization) elicit both humoral and strong cell-mediated immunity because the encoded antigen is:",
         ["Synthesized endogenously inside host myocytes and antigen-presenting cells, allowing processing and presentation on both MHC Class I and Class II pathways", "Coated on red blood cells", "Excreted directly in urine", "Derived entirely from plant leaves"],
         0, "DNA vaccines introduce a plasmid encoding the pathogen's protective protein driven by a strong eukaryotic promoter (CMV); host cells synthesize the antigen intracellularly, allowing endogenous proteasomal processing onto MHC Class I (activating CD8+ CTLs) as well as secretion onto MHC Class II.",
         True, "Vaccinology (ICAR PG PYQ)"),

        ("The primary reason that maternal derived antibodies (MDA) interfere with active immunization in young puppies and calves during early life is that maternal IgG:",
         ["Binds and neutralizes the vaccine antigen and cross-links the inhibitory Fc-gamma-RIIB receptor on naive B-cells, blocking activation", "Directly destroys the host thymus", "Cleaves host T-cell receptors", "Inactivates complement"],
         0, "High titers of maternal IgG bind the epitopes on live vaccine viruses, neutralizing them before they can replicate, and cross-link B-cell antigen receptors to inhibitory Fc-gamma-RIIB receptors, transmitting an inhibitory signal that prevents B-cell proliferation.",
         True, "Vaccinology (ICAR PG PYQ)"),

        # 41-45: Autoimmunity, immunodeficiencies
        ("In systemic lupus erythematosus (SLE) in dogs, the classic serological diagnostic hallmark is the presence of high circulating titers of:",
         ["Antinuclear Antibodies (ANA) directed against native double-stranded DNA and histone nucleoproteins", "Anti-thyroglobulin antibodies only", "Rheumatoid factor exclusively", "Anti-insulin antibodies"],
         0, "Canine SLE is a prototype multisystemic autoimmune disorder characterized by loss of self-tolerance to nuclear antigens; indirect immunofluorescence on HEp-2 cells demonstrating positive ANA titers (>= 1:256) is a core diagnostic criterion.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Severe Combined Immunodeficiency (SCID) in Arabian foals is a fatal autosomal recessive genetic disease caused by a defect in:",
         ["DNA-dependent protein kinase catalytic subunit (DNA-PKcs), preventing V(D)J recombination of T-cell receptors and immunoglobulins", "CD18 integrin subunit", "Myeloperoxidase", "Complement C3"],
         0, "Arabian SCID is caused by a 5-base-pair deletion in the DNA-PKcs gene, which is essential for double-strand break repair during V(D)J recombination in developing lymphocytes; foals lack all mature, functional B- and T-lymphocytes, dying of opportunistic adenovirus or Pneumocystis infections.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Myasthenia Gravis in dogs (congenital or acquired) is characterized by muscle weakness that worsens with exercise, caused by autoantibodies directed against:",
         ["Nicotinic Acetylcholine Receptors (nAChR) on the post-synaptic neuromuscular junction", "Ryanodine receptors in the sarcoplasmic reticulum", "Type 2M myosin fibers", "Dystrophin protein"],
         0, "Acquired myasthenia gravis is a Type II autoimmune disorder in which autoantibodies bind to post-synaptic nicotinic acetylcholine receptors at neuromuscular junctions, accelerating receptor internalization and complement-mediated destruction.",
         True, "Veterinary Immunology (ICAR PG PYQ)"),

        ("Autoimmune (Lymphocytic) Thyroiditis in dogs is the primary cause of primary adult hypothyroidism, characterized histopathologically by:",
         ["Diffuse infiltration of the thyroid gland by lymphocytes, plasma cells, and macrophages with progressive destruction of follicular architecture", "Massive follicular hyperplasia with goiter", "C-cell adenoma", "Pure calcification of follicles"],
         0, "Lymphocytic thyroiditis is an organ-specific autoimmune endocrinopathy characterized by autoantibodies against thyroglobulin (TgAA) and thyroid peroxidase (TPO), causing chronic lymphoplasmacytic infiltration, follicular atrophy, and replacement fibrosis.",
         False, "Veterinary Immunology"),

        ("The 'Passive Hemagglutination Test' (Indirect Hemagglutination / IHA) differs from direct hemagglutination because IHA:",
         ["Utilizes carrier erythrocytes artificially coated with soluble soluble antigens to detect serum antibodies by visible agglutination", "Uses unadsorbed normal red blood cells", "Requires live influenza virus", "Can only be performed at 56°C"],
         0, "In indirect (passive) hemagglutination, erythrocytes (often treated with tannic acid or formalin) act as inert, visual carrier particles to which soluble bacterial or viral antigens are chemically adsorbed, clumping when exposed to specific antibody.",
         True, "Diagnostic Immunology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module4_questions()
    print(f"Microbiology Module 4 loaded: {len(qs)} questions")
