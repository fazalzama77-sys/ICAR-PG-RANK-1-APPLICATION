# scripts/anat_mod2_splanchnology.py
# Module 2: Splanchnology (Visceral Organs) (40 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit I

def get_module2_questions():
    qs = [
        # 1-10: Ruminant & Equine Stomachs, Tongue, Salivary glands
        ("In the ruminant stomach, the mucous membrane lining the interior of the Reticulum is arranged in a pathognomonic pattern resembling a:",
         ["Honeycomb (polygonal cells bounded by serrated mucosal ridges)", "Book with multiple leaf-like pages", "Carpet of shaggy conical papillae", "Smooth glistening velvet surface with no folds"],
         0, "The interior mucosa of the reticulum is thrown into permanent intersecting primary, secondary, and tertiary folds dividing the surface into 4- to 6-sided polygonal compartments resembling a honeycomb.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The 'Reticular Groove' (esophageal groove / sulcus reticuli) in suckling ruminants connects which two anatomical regions, allowing swallowed milk to bypass the rumen and reticulum?",
         ["Cardia to the Reticulo-omasal orifice", "Pylorus to the duodenum", "Dorsal ruminal sac to the ventral sac", "Omasum to the abomasum"],
         0, "In nursing calves and lambs, the reticular groove reflexively contracts into a closed muscular tube extending from the cardia across the medial wall of the reticulum directly into the reticulo-omasal orifice, shunting milk directly into the abomasum.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The 'Torus Pyloricus' is a prominent, rounded, fibro-muscular erectile mucosal cushion located at the pyloric sphincter, uniquely present in the stomach of the:",
         ["Ox (Bovine) and Pig (Porcine)", "Horse (Equine)", "Dog (Canine)", "Cat (Feline)"],
         0, "In ruminants and swine, the lesser curvature side of the pyloric canal features a hemispherical, bulbous projection called the torus pyloricus, which assists in closing the pyloric orifice and regulating digesta outflow.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The internal mucosal lining of the simple stomach of the Horse is sharply divided into a non-glandular stratified squamous region and a glandular region by a distinct, elevated, zigzag border known as the:",
         ["Margo Plicatus", "Sulcus intermedius", "Torus pyloricus", "Plica gastrica"],
         0, "The margo plicatus (folded border) is a prominent, raised, serrated cutoff line in the equine stomach separating the pale, cutaneous, non-glandular stratified squamous proventriculus from the dark, pink, glandular fundic mucosa.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The 'Diverticulum Ventriculi' is a cone-shaped, blind pouch extending cranially from the gastric fundus in the:",
         ["Pig (Porcine)", "Horse", "Dog", "Ox"],
         0, "The stomach of the domestic pig is distinguished by possessing a conical, blind-ending pouch projecting dorsomedially from the fundus, termed the diverticulum ventriculi.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The 'Torus Linguae' (lingual prominence / dorsal swelling of the tongue), bounded rostrally by the transverse 'fossa linguae', is an anatomical feature of the tongue of the:",
         ["Ox (Bovine)", "Horse (Equine)", "Dog (Canine)", "Pig (Porcine)"],
         0, "The bovine tongue is characterized by a prominent dorsal elevation in its caudal third (torus linguae), separated from the rostral body by a deep transverse groove (fossa linguae) where foreign plant awns frequently lodge.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The 'Lyssa' (a median, longitudinal, spindle-shaped, fibrous or fibro-cartilaginous cord embedded within the ventral muscular apex of the tongue) is present in the:",
         ["Dog (Canine) and Cat (Feline)", "Horse", "Ox", "Pig"],
         0, "The lyssa is an elastic, rod-like structure wrapped in a dense connective tissue sheath located along the median ventral raphe of the tongue apex in carnivores, containing fat, cartilage cells, and muscle fibers.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("In the domestic Horse, the Parotid Salivary Duct (Stensen's duct) opens into the buccal vestibule opposite the:",
         ["Upper 3rd cheek tooth (Premolar 4)", "Upper 1st molar", "Upper 4th premolar in the dog", "Lower canine tooth"],
         0, "In equines, the parotid duct travels in the vascular notch of the mandible alongside the facial artery and vein, piercing the cheek to open on a mucosal papilla opposite the upper third cheek tooth (P4), whereas in cattle it opens opposite the 2nd molar, and in dogs opposite the 4th upper premolar (carnassial).",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("Which domestic animal species completely lacks a Gall Bladder (vesica fellea)?",
         ["Horse (Equine), along with Pigeon, Ostrich, and Camel", "Ox (Bovine)", "Dog (Canine)", "Pig (Porcine)"],
         0, "The horse possesses no gall bladder; bile synthesized continuously by hepatic lobules flows directly through the common bile duct (ductus choledochus) and empties at the major duodenal papilla within the diverticulum duodeni.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The liver of the domestic Pig is readily recognized both grossly and microscopically by which distinctive histological feature?",
         ["Prominent interlobular connective tissue septa surrounding each hepatic lobule, giving the surface a 'morocco-leather' pattern", "Total absence of lobulation", "Presence of central veins with no sinusoidal lining", "Complete lack of portal triads"],
         0, "In swine, dense, thick bands of interlobular fibrous connective tissue encircle every individual hepatic lobule, imparting a distinct polygonal mosaic or 'morocco leather' appearance to the capsule and preventing easy parenchymal tearing.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        # 11-20: Intestines, cecum, spiral colon
        ("The 'Spiral Colon' (colon ascendens) of ruminants is anatomically arranged in flat concentric loops comprising:",
         ["Centripetal coils (running inwards towards the central flexure) and Centrifugal coils (running outwards from the central flexure)", "Haustrated sacculations with 4 taeniae", "A simple U-shaped loop", "A descending spiral without a central flexure"],
         0, "The ascending colon of ruminants forms a flattened planar spiral coiled within the mesentery; digesta travels inward along 1.5 to 2.5 centripetal gyri to the central flexure, and then reverses direction through centrifugal gyri.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("The massive, comma-shaped Cecum of the Horse has a capacity of 30 to 35 liters and is characterized by possessing how many longitudinal muscular bands (taeniae) and sacculations (haustra)?",
         ["4 longitudinal bands (taeniae: dorsal, ventral, medial, lateral) and 4 rows of haustra", "No bands or haustra", "2 bands only", "8 bands"],
         0, "The equine cecum is sacculated and banded, possessing exactly 4 longitudinal taeniae (dorsal, ventral, medial, lateral); the dorsal and medial bands receive the ileocecal and cecocolic folds, respectively.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("In the domestic Horse, the ascending Great Colon is divided into four consecutive anatomical segments that form two U-shaped loops connected by which narrow, non-sacculated flexure that is a frequent site of impaction colic?",
         ["Pelvic Flexure (between the Left Ventral Colon and Left Dorsal Colon)", "Diaphragmatic flexure", "Sternal flexure", "Duodenojejunal flexure"],
         0, "The equine large colon transitions from the wide, sacculated left ventral colon through a narrow, unbanded, unattached hairpin loop called the Pelvic Flexure before expanding into the left dorsal colon, making it the most common site of impaction.",
         True, "Digestive Splanchnology (ICAR PG PYQ)"),

        ("In birds (such as the domestic fowl), the anatomical junction between the small intestine and the large intestine is characterized by the presence of:",
         ["Paired (two) elongated Ceca", "A single large comma-shaped cecum", "No cecum of any kind", "Three ceca"],
         0, "Birds possess two long, blind ceca arising symmetrically at the ileocecal-colic junction, extending cranially along the sides of the ileum, functioning in water reabsorption and bacterial cellulose fermentation.",
         True, "Avian Splanchnology (ICAR PG PYQ)"),

        ("Meckel's Diverticulum (diverticulum vitellinum), situated along the antimesenteric border of the jejunum in domestic fowl, is an anatomical landmark representing the persistence of the embryonic:",
         ["Yolk sac stalk (vitelline duct)", "Allantoic stalk", "Urachus", "Mesonephric duct"],
         0, "Meckel's diverticulum is a small, constant, finger-like projection on the outer convex border of the jejunum in birds, demarcating the boundary between the jejunum and ileum, formed by the remnant of the yolk stalk.",
         True, "Avian Splanchnology (ICAR PG PYQ)"),

        ("In the canine carnassial (sectorial) tooth apparatus specialized for shearing flesh, the upper and lower carnassial teeth are which specific teeth?",
         ["Upper 4th Premolar (PM4) and Lower 1st Molar (M1)", "Upper 1st Molar and Lower 4th Premolar", "Upper Canine and Lower Canine", "Upper 3rd Premolar and Lower 3rd Molar"],
         0, "The shearing carnassial mechanism in dogs is formed by the occlusion of the upper 4th premolar (PM4) cutting against the lateral surface of the lower 1st molar (M1).",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The permanent dental formula of the adult domestic Ox (Bovine) is correctly written as:",
         ["2 x [ I 0/4, C 0/0, PM 3/3, M 3/3 ] = 32 teeth (with the 4th lower incisiform tooth being a modified canine)", "2 x [ I 3/3, C 1/1, PM 4/4, M 2/3 ] = 42", "2 x [ I 3/3, C 1/1, PM 3/3, M 3/3 ] = 40", "2 x [ I 1/1, C 0/0, PM 1/1, M 3/3 ] = 16"],
         0, "Ruminants completely lack upper incisors and upper canines (replaced by the tough fibrous dental pad / pulvinus dentalis); the 4 lower teeth on each side are 3 incisors + 1 canine that has adopted an incisiform shape (total 32).",
         True, "Comparative Anatomy (ICAR PG PYQ)"),

        ("The permanent dental formula of the adult domestic Pig (Sus scrofa) is complete and unreduced, containing a total of:",
         ["44 teeth: 2 x [ I 3/3, C 1/1, PM 4/4, M 3/3 ]", "32 teeth", "42 teeth", "40 teeth"],
         0, "The domestic pig retains the primitive, complete, unreduced eutherian mammalian dentition comprising 3 incisors, 1 canine, 4 premolars, and 3 molars in each quadrant, totaling 44 permanent teeth.",
         True, "Comparative Anatomy (ICAR PG PYQ)"),

        ("The permanent dental formula of the adult domestic Horse (Stallion) is:",
         ["2 x [ I 3/3, C 1/1, PM 3-4/3, M 3/3 ] = 40 or 42 teeth", "2 x [ I 0/4, C 0/0, PM 3/3, M 3/3 ] = 32", "2 x [ I 3/3, C 1/1, PM 4/4, M 2/3 ] = 42", "2 x [ I 3/3, C 0/0, PM 3/3, M 3/3 ] = 36"],
         0, "An adult stallion has 40-42 permanent teeth (3 incisors, 1 canine, 3 or 4 premolars - including the vestigial P1 'wolf tooth' - and 3 molars on each side); mares typically lack canine teeth (36 teeth).",
         True, "Comparative Anatomy (ICAR PG PYQ)"),

        ("In the domestic dog, the 'Wolf Tooth' seen in horses does not occur; instead, the permanent canine dental formula comprises a total of:",
         ["42 teeth: 2 x [ I 3/3, C 1/1, PM 4/4, M 2/3 ]", "44 teeth", "32 teeth", "30 teeth"],
         0, "The permanent dental formula of the dog is I 3/3, C 1/1, PM 4/4, M 2/3 (total 42 teeth), whereas the domestic cat has a reduced dentition of only 30 teeth (I 3/3, C 1/1, PM 3/2, M 1/1).",
         True, "Comparative Anatomy (ICAR PG PYQ)"),

        # 21-30: Respiratory tract, Larynx, Lungs
        ("The 'Tracheal Bronchus' (bronchus trachealis), which arises directly from the right side of the trachea cranial to the main tracheal bifurcation to supply the right cranial lung lobe, is present in:",
         ["Ruminants (Ox, Sheep, Goat) and Swine (Pig)", "Horse and Dog", "Cat and Rabbit", "Birds"],
         0, "In artiodactyls (ruminants and pigs), the right cranial lobe is ventilated independently by a dedicated tracheal bronchus arising 4-8 cm cranial to the carina, making the right cranial lobe particularly prone to aspiration.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The Tracheal Rings (cartilagines tracheales) of domestic mammals are incomplete dorsally, where the gap is bridged by the smooth Trachealis Muscle. In the Dog and Cat, the trachealis muscle is unique because it is positioned:",
         ["On the EXTERNAL (outer) surface of the tracheal cartilages", "On the INTERNAL (inner/luminal) surface of the tracheal cartilages as in Ox and Horse", "Completely absent", "Within the cartilage rings"],
         0, "In carnivores (dogs and cats), the transverse smooth fibers of the trachealis muscle attach to the external perichondrial surfaces of the cartilage rings, whereas in horses, cattle, and sheep, the muscle attaches to the internal luminal surface.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The Larynx consists of four major cartilages (Thyroid, Cricoid, Epiglottis, and paired Arytenoid). The vocal process and muscular process are anatomical landmarks located on the:",
         ["Arytenoid cartilages", "Thyroid cartilage", "Cricoid cartilage", "Epiglottic cartilage"],
         0, "The paired arytenoid cartilages are pyramidal; the cranial/dorsal apex bears the corniculate process, the ventral angle forms the vocal process (anchoring the vocal ligament), and the lateral angle forms the muscular process.",
         False, "Respiratory Splanchnology"),

        ("In the horse, the lateral laryngeal ventricle (sacculus laryngis of Morgagni) is a blind mucous pouch located between which two laryngeal folds?",
         ["Ventricular fold (vestibular fold / false vocal cord) and Vocal fold (true vocal cord)", "Epiglottis and arytenoid", "Cricoid and thyroid", "Tracheal ring and cricoid"],
         0, "The laryngeal ventricle is a mucosal pocket situated between the vestibular fold cranially and the vocal fold caudally; surgical ventriculectomy ('Hobday operation') obliterates this pocket to alleviate roaring (laryngeal hemiplegia).",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("In all domestic mammalian species (Ox, Horse, Dog, Pig, Sheep, and Cat), the Left Lung lacks which anatomical lobe?",
         ["Middle lobe (Cardiac lobe)", "Cranial lobe", "Caudal lobe", "Accessory lobe"],
         0, "The mammalian left lung is divided into a cranial lobe (often subdivided into cranial and caudal parts) and a caudal lobe, but never possesses a middle lobe; only the right lung has cranial, middle, caudal, and accessory lobes.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The 'Cardiac Notch' (incisura cardiaca) of the lung, where the heart contacts the thoracic wall directly without intervening lung tissue, is clinically used for auscultation and pericardiocentesis. In the horse, it is largest on the:",
         ["Left side (between ribs 3 and 6)", "Right side (between ribs 6 and 9)", "Dorsal aspect", "Caudal diaphragmatic border"],
         0, "Because the apex of the equine heart tilts to the left, the cardiac notch in the left lung is large and deep, occupying the 3rd to 6th intercostal spaces, allowing direct acoustic coupling and cardiac puncture.",
         False, "Respiratory Splanchnology"),

        ("The Right Lung of the domestic Horse is unique among ungulate lungs because it:",
         ["Lacks external interlobar fissures, so the cranial and middle lobes are completely fused into a single lobe", "Has 6 distinct lobes separated by deep fissures", "Possesses a tracheal bronchus", "Is smaller than the left lung"],
         0, "The equine lung is non-lobated externally; shallow fissures are absent, and the right lung possesses only an indistinct cranial lobe, a caudal lobe, and an accessory lobe (middle lobe is absent/fused), giving it a smooth external contour.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The 'Cupula Pleurae' (cervical dome of the pleura) extends cranially beyond the first pair of ribs into the neck region, and is clinically vulnerable to traumatic pneumothorax on the:",
         ["Right side in the Ox, and both sides in the Dog and Horse", "Left side only in all animals", "Neither side (it never extends beyond the 1st rib)", "Dorsal aspect of T3"],
         0, "In cattle, the right pleural sac extends cranially beyond the first rib into the thoracic inlet (cupula pleurae dextra); deep punctures in the lower neck can tear this cupula, producing immediate bilateral tension pneumothorax.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The Guttural Pouches (diverticula tubae auditivae) of the domestic Horse are large, bilateral, mucosal-lined diverticula of the:",
         ["Eustachian (auditory) tubes, each having a volume of approximately 300 to 500 mL", "Esophagus", "Trachea", "Sphenoid sinus"],
         0, "The equine guttural pouch is a massive ventral diverticulum of the auditory tube, bounded dorsally by the cranial base and atlas, and medially separated from its fellow by the rectus capitis muscles and thin septum.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        ("The stylohyoid bone divides each equine Guttural Pouch into two unequal compartments: a smaller Lateral Compartment and a larger Medial Compartment. Which vital cranial nerves and arteries lie in direct contact with the thin mucous lining of the Medial Compartment?",
         ["Internal Carotid Artery and Cranial Nerves IX (Glossopharyngeal), X (Vagus), XI (Accessory), XII (Hypoglossal), and sympathetic trunk", "External Carotid Artery and Facial nerve only", "Femoral nerve and Iliac artery", "Radial nerve and Brachial artery"],
         0, "The caudomedial wall of the medial compartment is in direct contact with the internal carotid artery and CN IX, X, XI, XII; mycotic infection (Aspergillus) can erode the artery (causing fatal epistaxis) or paralyze these cranial nerves.",
         True, "Respiratory Splanchnology (ICAR PG PYQ)"),

        # 31-40: Urogenital splanchnology
        ("The Kidney of the adult domestic Ox (Bovine) is anatomically unique among domestic mammals because it is:",
         ["Externally Lobated (multilobed) with 15 to 25 distinct superficial lobes, and lacks a renal pelvis", "Smooth and unipyramidal with a renal pelvis", "Heart-shaped", "Smooth multipyramidal"],
         0, "The bovine kidney is multilobar (multipyramidal) both internally and externally, exhibiting 15 to 25 polygonal lobes separated by interlobar fissures; calyces minores join to form two calyces majores that lead directly to the ureter without a renal pelvis.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The Right Kidney of the domestic Horse is pathognomonic on gross inspection for being:",
         ["Heart-shaped (resembling a playing card spade), while the left kidney is bean-shaped", "Multilobed with 20 lobes", "Puckered like a walnut", "Cylindrical"],
         0, "In the horse, the right kidney is flattened dorsoventrally and distinctly heart-shaped (or cloverleaf/trefoil), situated under the 16th to 18th ribs; the left kidney is elongated and bean-shaped.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("In the equine kidney, the renal pelvis and terminal collecting ducts are histologically unique because they contain:",
         ["Mucus-secreting tubuloalveolar glands (glandulae pelvis renalis), which make normal equine urine thick, cloudy, and viscous", "No mucus glands", "Abundant stratified squamous epithelium", "Heavy calcification in all nephrons"],
         0, "Normal horse urine is viscous and frothy due to high concentrations of mucus secreted by branched tubuloalveolar glands situated in the subepithelial connective tissue of the renal pelvis, combined with calcium carbonate crystals.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The 'Crista Renalis' (renal crest), a continuous longitudinal sagittal ridge formed by the complete fusion of all renal medullary pyramids, is present in the unipyramidal kidneys of the:",
         ["Dog, Cat, Sheep, Goat, and Horse", "Ox and Pig", "Only in humans", "Only in birds"],
         0, "In unipyramidal kidneys (carnivores, small ruminants, and horses), embryonic medullary pyramids fuse into a single continuous central longitudinal ridge (crista renalis) from which the papillary ducts discharge urine into the renal pelvis.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The fibroelastic Penis of the Bull, Ram, and Boar possesses an S-shaped curvature that straightens during erection to extend the penis, known as the:",
         ["Sigmoid Flexure (Flexura sigmoidea)", "Bulbus glandis", "Os penis", "Corpus spongiosum"],
         0, "Ruminants and swine possess a fibroelastic penis with high connective tissue content and minimal erectile cavernous tissue; in the flaccid state, the penis is folded into a post-scrotal (or pre-scrotal in boar) S-shaped curve (sigmoid flexure).",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The glans penis of the Ram (and Buck) is characterized by an exceptionally long, slender, worm-like process projecting 3 to 4 cm beyond the glans, known as the:",
         ["Processus urethrae (Vermiform appendage)", "Bulbus glandis", "Collum glandis", "Corona glandis"],
         0, "The ram and billy goat possess an elongated filiform urethral process (processus urethrae) that extends 3-4 cm free beyond the tip of the glans penis; it rotates rapidly during ejaculation to spray semen onto the external os of the cervix.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The glans penis of the adult Boar (Sus scrofa) is pathognomonic for having a:",
         ["Spiral, corkscrew-shaped terminal twist that locks into the interdigitating pulvini cervicales of the sow's cervix", "Bulbus glandis that causes a coital tie", "Long vermiform appendage", "Massive mushroom-shaped flare"],
         0, "The distal extremity of the boar penis is twisted spirally like a carpenter's corkscrew; during prolonged copulation, this spiral tip threads into and locks between the interdigitating mucosal pads (pulvini cervicales) of the sow cervix.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The 'Bulbus Glandis' is a massive expansile venous erectile ring located on the proximal glans penis responsible for the 'coital tie' (copulatory lock) in the:",
         ["Dog (Canine)", "Horse", "Bull", "Ram"],
         0, "In male canids, the bulbus glandis expands enormously upon intromission when venous drainage is compressed, locking the penis inside the canine vestibular sphincter and vagina for 15 to 45 minutes (the 'tie').",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("In the female bovine reproductive tract, the internal endometrium bears permanent, button-like, avascular-appearing aglandular elevations termed 'Caruncles', which are:",
         ["Convex in the Cow, but Concave (cup-shaped) in the Ewe", "Concave in the cow", "Flat in all ruminants", "Completely covered by uterine glands"],
         0, "The uterine mucosa of ruminants features 70 to 120 specialized aglandular caruncles; in cows, the caruncles are mushroom-shaped and convex, whereas in ewes and does, they have a central depression and are cup-shaped/concave.",
         True, "Urogenital Splanchnology (ICAR PG PYQ)"),

        ("The Cervix of the Sow (female pig) differs from that of the cow and mare because its cervical canal features:",
         ["Interdigitating rounded mucosal prominences (Pulvini cervicales) that occlude the lumen like a zipper, and lacks a distinct fornix vaginae", "3 to 4 circular rigid annular rings with a deep fornix", "Smooth longitudinal mucosal folds", "Total absence of muscularis"],
         0, "The porcine cervix is long (15-20 cm) and transitions gradually from the vagina without forming an external portio vaginalis or fornix; its lumen is packed with alternating, interdigitating round cartilaginous-firm mucosal pads (pulvini cervicales).",
         True, "Urogenital Splanchnology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module2_questions()
    print(f"Anatomy Module 2 loaded: {len(qs)} questions")
