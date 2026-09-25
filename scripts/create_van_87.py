# scripts/create_van_87.py
import json

VAN_OVERRIDES = {
    "van_q_020": [
        "Caudal translation of tibia relative to the femoral condyles",
        "Medial luxation of patella relative to femoral trochlea",
        "Severe hyperextension and valgus deviation of the stifle joint"
    ],
    "van_q_030": [
        "Third permanent lower molar (M3 in mandible)",
        "Erupted canine tooth in the adult stallion (C1)",
        "Deciduous first lower incisor (Di1 in foal)"
    ],
    "van_q_031": [
        "Biceps femoris, semitendinosus, and gracilis muscles",
        "Pectineus, adductor, and deep digital flexor muscles",
        "Tibialis cranialis and peroneus tertius tendons"
    ],
    "van_q_042": [
        "Renal vein and Internal iliac venous trunk",
        "External jugular vein and Cephalic vein",
        "Right azygos vein and Caudal vena cava"
    ],
    "van_q_050": [
        "Facial nerve (CN VII) and Mandibular nerve (CN V3)",
        "Phrenic nerve and Spinal accessory nerve (CN XI)",
        "Vagus nerve (CN X) and Glossopharyngeal nerve (CN IX)"
    ],
    "van_q_051": [
        "Internal jugular vein and Subclavian vein",
        "Superficial cephalic vein and Brachial vein",
        "Caudal auricular vein and Occipital vein"
    ],
    "van_q_058": [
        "The primary and exclusive arterial supply to the brain",
        "A direct continuous branch of the vertebral artery",
        "Markedly hypertrophied and twice the caliber of maxillary artery"
    ],
    "van_q_067": [
        "Smooth external surface with single renal crest (unipapillary)",
        "Heart-shaped right kidney with smooth cortex (multipyramidal)",
        "Elongated flattened kidney with internal calyces (multipapillary)"
    ],
    "van_q_078": [
        "Rostral entrance of the cranial larynx at the glottis",
        "Base of the tongue anterior to the hyoid apparatus",
        "Intrapulmonary mesobronchus within the lung parenchyma"
    ],
    "van_q_084": [
        "Smooth longitudinal folds without transverse rings (in the mare)",
        "Interdigitating corkscrew mucosal pads (pulvini cervicales in sow)",
        "Single transverse spiral fold with smooth canal (in the bitch)"
    ],
    "van_exp_002": [
        "C13 T6 L5 S5 Cy18-20 (Avian vertebral formula)",
        "C7 T13 L7 S3 Cy20-23 (Canine vertebral formula)",
        "C7 T14-15 L6-7 S4 Cy20-23 (Porcine vertebral formula)"
    ],
    "van_exp_003": [
        "Facial crest extending horizontally onto the nasal bone",
        "Supraorbital process forming a complete bony orbital rim",
        "Cornual process projecting caudolaterally from the parietal"
    ],
    "van_exp_004": [
        "Medial aspect of the proximal extremity of the tibia",
        "Lateral epicondyle of the humerus distal to the crest",
        "Cranial border of the neck of the scapula near tuber"
    ],
    "van_exp_005": [
        "Large single central canal for the transmission of spinal cord",
        "Nutrient foramen dedicated strictly to medullary blood supply",
        "Muscular fossa providing extensive attachment for masseter"
    ],
    "van_exp_006": [
        "Ox and Sheep (Ruminantia)",
        "Dog and Cat (Carnivora)",
        "Pig and Camel (Suina / Tylopoda)"
    ],
    "van_exp_011": [
        "Distal extremity of the femur (condyles and trochlea)",
        "Medial malleolus of the distal tibia and fibula",
        "Radial tuberosity of the proximal radius and ulna"
    ],
    "van_exp_012": [
        "Spina scapulae is low and terminates without an acromion",
        "Possesses a distinct hamate and suprahamate acromial process",
        "Tuber spinae is absent and the spine divides scapula equally"
    ],
    "van_exp_014": [
        "Shaft is fused completely to radius along its entire length",
        "Proximal end is completely absent while distal end forms styloid",
        "Distal end articulates with the intermediate carpal bone only"
    ],
    "van_exp_015": [
        "Four digits (Digits II, III, IV, and V with small dewclaws)",
        "Two fully developed weight-bearing functional digits (Digits III and IV)",
        "Three digits (Digit III primary, with rudimentary Digits II and IV)"
    ],
    "van_exp_016": [
        "Metacarpal III and IV (bearing distinct medial and lateral splints)",
        "Metacarpal I and V (forming prominent accessory weight-bearing bones)",
        "Metacarpal II and V (present as thin proximal rudimentary splints)"
    ],
    "van_exp_017": [
        "Extensor process on the dorsal articular border of the proximal phalanx",
        "Flexor tuberosity on the palmar surface of the middle phalanx",
        "Crest of the ungual process surrounded by the ungual hood"
    ],
    "van_exp_021": [
        "Two functional weight-bearing digits (Digits III and IV)",
        "Four functional digits (Digits II, III, IV, and V bearing weight)",
        "Single solitary functional digit (Digit III supporting limb)"
    ],
    "van_exp_022": [
        "Lateral malleolus of the distal fibular shaft",
        "Olecranon tuberosity of the proximal ulna",
        "Greater trochanter of the proximal femur"
    ],
    "van_exp_023": [
        "Trochanter tertius (third trochanter) on lateral shaft",
        "Fovea capitis femoris located on articular head",
        "Supracondyloid fossa on the caudal distal shaft"
    ],
    "van_exp_024": [
        "Tuber calcanei of the fibular tarsal bone",
        "Tuber coxae of the iliac cranial wing",
        "Patella (kneecap) gliding on trochlea"
    ],
    "van_exp_025": [
        "Single large bone formed by total fusion of all seven tarsals",
        "Eight bones arranged in three distinct transverse rows",
        "Five bones (Tibial, Fibular, Central, fused I+II, and IV)"
    ],
    "van_exp_026": [
        "Ox and Sheep (Ruminants)",
        "Horse (Equine)",
        "Pig (Porcine)"
    ],
    "van_exp_028": [
        "Ox (Bovine, situated along the medial pubic crest)",
        "Horse (Equine, located at the caudal border of pubis)",
        "Pig (Porcine, forming an ossified ventral symphysis)"
    ],
    "van_exp_029": [
        "Synarthrosis (immovable cranial suture or synchondrosis)",
        "Amphiarthrosis (slightly movable intervertebral cartilaginous joint)",
        "Gomphosis (specialized fibrous dentoalveolar peg-and-socket joint)"
    ],
    "van_exp_030": [
        "Synovial hinge joint (Ginglymus permitting flexion/extension)",
        "Suture joint (Gomphosis binding cranial bones immovably)",
        "Fibrous syndesmosis (connected solely by interosseous ligaments)"
    ],
    "van_exp_031": [
        "Ox (Bovine, possessing only the round ligament / ligamentum teres)",
        "Dog (Canine, possessing an extensive transverse acetabular ligament)",
        "Pig (Porcine, possessing a wide capsular ligament without accessory bands)"
    ],
    "van_exp_032": [
        "Sacrotuberous ligament running from the sacrum to the ischiatic tuber",
        "Dorsal sacroiliac ligament reinforcing the dorsal pelvic margin",
        "Inguinal ligament spanning the caudal abdominal internal margin"
    ],
    "van_exp_033": [
        "Collateral ligaments of the femorotibial joint",
        "Meniscofemoral ligament of the lateral meniscus",
        "Transverse ligament connecting cranial meniscal horns"
    ],
    "van_exp_034": [
        "Three distinct patellar ligaments (Medial, Middle, and Lateral)",
        "Two patellar ligaments (Cranial and Caudal patellar bands)",
        "Four patellar ligaments forming a cruciate fibrous meshwork"
    ],
    "van_exp_035": [
        "Femorotibial and femoropatellar joint compartments",
        "Tibiotarsal (tarsocrural) joint compartment",
        "Proximal and distal intertarsal joint compartments"
    ],
    "van_exp_036": [
        "Masseter muscle (closing the jaw with powerful lateral chewing)",
        "Temporalis muscle (raising the mandible vertically against maxilla)",
        "Medial pterygoid muscle (elevating and adducting the mandible)"
    ],
    "van_exp_037": [
        "Supraspinatus muscle (acting across the shoulder joint)",
        "Biceps brachii muscle (acting across shoulder and elbow)",
        "Latissimus dorsi muscle (retracting the forelimb caudally)"
    ],
    "van_exp_038": [
        "Horse (Equus caballus) and Ox (Bos taurus)",
        "Dog (Canis familiaris) and Sheep (Ovis aries)",
        "Camel (Camelus dromedarius) and Goat (Capra hircus)"
    ],
    "van_exp_041": [
        "Iliopsoas muscle inserting onto the lesser trochanter",
        "Quadriceps femoris muscle inserting onto the patella",
        "Biceps femoris muscle inserting onto the calcaneus"
    ],
    "van_exp_042": [
        "Cranial tibial muscle and Peroneus longus muscle",
        "Gastrocnemius muscle and Soleus muscle tendons",
        "Gracilis muscle and Pectineus muscle aponeuroses"
    ],
    "van_exp_044": [
        "Inability to extend the elbow joint with dropped shoulder posture",
        "Loss of cutaneous sensation over the caudolateral thigh skin",
        "Severe hyperflexion of the hock with inability to extend digits"
    ],
    "van_exp_045": [
        "Inability to bear weight due to collapse of stifle flexion",
        "Hyperflexion of the hock joint with knuckling of distal fetlock",
        "Lateral abduction of the thigh with inability to adduct limb"
    ],
    "van_exp_046": [
        "Loss of the patellar tendon reflex (quadriceps femoris paralysis)",
        "Inability to flex the hip joint and retract the abdominal wall",
        "Severe overextension of the hock with hyperflexion of digits"
    ],
    "van_exp_048": [
        "Parotid salivary gland (situated ventral to the ear canal)",
        "Submandibular lymph node (located at the angle of mandible)",
        "External jugular vein (running within the jugular furrow)"
    ],
    "van_exp_049": [
        "Deep circumflex iliac artery and internal abdominal oblique",
        "Caudal epigastric artery and external abdominal oblique",
        "External pudendal artery and superficial inguinal ring"
    ],
    "van_exp_050": [
        "Superficial and deep digital flexor muscle tendons",
        "Suspensory ligament (interosseous medius muscle)",
        "Biceps brachii and lacertus fibrosus tendinous cord"
    ],
    "van_exp_051": [
        "Peroneus tertius and superficial digital flexor tendons",
        "Gastrocnemius and deep digital flexor muscle tendons",
        "Cranial tibial muscle and lateral digital extensor tendons"
    ],
    "van_exp_052": [
        "Ventral border of the sternum along the costal cartilages",
        "Dorsal midline of the thoracic and lumbar vertebral spines",
        "Lateral border of the ribs forming the costal arch line"
    ],
    "van_exp_053": [
        "Linea alba (median fibrous raphe of the ventral abdomen)",
        "Prepubic tendon (anchoring the rectus abdominis to pelvis)",
        "Thoracolumbar fascia (investing the epaxial musculature)"
    ],
    "van_exp_054": [
        "Femoral hernia (protrusion through the vascular lacuna)",
        "Umbilical hernia (protrusion through the ventral umbilical ring)",
        "Perineal hernia (weakness between levator ani and coccygeus)"
    ],
    "van_exp_055": [
        "Filiform papillae (mechanical, slender, cornified papillae)",
        "Conical papillae (large, sharp mechanical buccal papillae)",
        "Lenticular papillae (flattened, lens-shaped mechanical papillae)"
    ],
    "van_exp_056": [
        "Ox and Sheep (Ruminants possessing a distinct torus linguae)",
        "Dog and Cat (Carnivores possessing a dorsal median lingual groove)",
        "Pig and Camel (Omnivores possessing paired foliate papillae)"
    ],
    "van_exp_057": [
        "Lyssa (fibrocartilaginous cord embedded in ventral carnivore tongue)",
        "Cartilago dorsi linguae (median dorsal fibrous lingual bar in horse)",
        "Torus linguae (dorsal muscular lingual prominence in ruminants)"
    ],
    "van_exp_058": [
        "Mandibular salivary gland (mixed seromucous gland in jaw angle)",
        "Sublingual salivary gland (polystomatic and monostomatic parts)",
        "Zygomatic salivary gland (dorsal buccal gland in carnivores)"
    ],
    "van_exp_060": [
        "Infundibulum (deep enamel invagination on occlusal table)",
        "Pulp cavity (central vascular chamber containing odontoblasts)",
        "Secondary dentin (protective reparative dentin covering pulp)"
    ],
    "van_exp_062": [
        "Simple monogastric stomach with extensive non-glandular pars esophagea",
        "Composite stomach with three distinct glandular mucosal compartments",
        "Ruminant stomach lacking an omasal compartment (pseudoruminant)"
    ],
    "van_exp_063": [
        "Left paralumbar fossa and abdominal wall (Rumen atrium and dorsal sac)",
        "Ventral abdominal floor caudal to the xiphoid cartilage (Abomasum)",
        "Right hypochondriac region medial to the 7th-9th ribs (Omasum)"
    ],
    "van_exp_064": [
        "Esophageal groove (Sulcus reticuli) directly into the omasal canal",
        "Ventral ruminal sac via the large ruminoreticular orifice",
        "Pyloric sphincter directly into the cranial duodenal ampulla"
    ],
    "van_exp_065": [
        "Glandular stomach producing gastric acid, pepsin, and lysozyme",
        "Fermentation vat lined by stratified squamous keratinized epithelium",
        "Mechanical grinding organ containing ingested gravel and stones"
    ],
    "van_exp_066": [
        "Equine ascending colon (divided into four large parallel segments)",
        "Canine ascending colon (simple, short, straight segment)",
        "Feline ascending colon (reduced, non-sacculated tube)"
    ],
    "van_exp_067": [
        "Lacks external interlobar fissures, so cranial and middle lobes are fused into a single lobe",
        "Divided into four separate cranial lobes and three large caudal lobes by deep fissures",
        "Consists of a single undivided continuous lung mass without any accessory lobules"
    ],
    "van_exp_068": [
        "Right side in the Ox, and both sides in the Dog and Horse",
        "Left side exclusively in the Horse, and absent in the Dog",
        "Bilateral and symmetrical in the Pig, and absent in the Ox"
    ],
    "van_exp_069": [
        "Eustachian auditory tubes, each having a volume of approximately 300 to 500 mL",
        "Maxillary sinuses, each holding approximately 50 to 75 mL of serous fluid",
        "Frontal sinus diverticula, holding over 1,000 mL of mucosal secretions"
    ],
    "van_exp_071": [
        "Externally Lobated with 15 to 25 distinct superficial lobes, and lacks a renal pelvis",
        "Smooth multipyramidal kidney with single central renal pelvis and crest",
        "Heart-shaped right kidney and bean-shaped left kidney with terminal calyces"
    ],
    "van_exp_072": [
        "Heart-shaped right kidney, while the left kidney is bean-shaped",
        "Lobated right kidney, while the left kidney is completely smooth",
        "Elongated flattened right kidney, while left kidney is spherical"
    ],
    "van_exp_075": [
        "Sigmoid Flexure (Flexura sigmoidea of penis)",
        "Corpus cavernosum (Erectile venous cavernous tissue)",
        "Os penis / Baculum (Splanchnic penile bone)"
    ],
    "van_exp_076": [
        "Processus urethrae (Vermiform urethral appendage)",
        "Corona glandis (Expanded dorsal rim of the glans)",
        "Bulbus glandis (Spherical vascular erectile bulb)"
    ],
    "van_exp_077": [
        "Spiral corkscrew terminal twist that locks into the sow's cervix",
        "Prominent os penis bone grooved ventrally for the urethra",
        "Folded prepuce containing a dorsal preputial diverticulum sac"
    ],
    "van_exp_079": [
        "Convex in the Cow, but Concave (cup-shaped) in the Ewe",
        "Flat in the Cow, but Highly Branched (villous) in the Ewe",
        "Zonary in the Cow, but Diffuse and Follicular in the Ewe"
    ],
    "van_exp_080": [
        "Interdigitating mucosal prominences (Pulvini cervicales) that occlude the lumen",
        "Transverse circular mucosal rings (annular folds) numbering 3 to 4 in total",
        "Smooth longitudinal mucosal folds extending continuously into the fornix"
    ],
    "van_exp_082": [
        "Right Ventricle (connecting the interventricular septum to parietal wall)",
        "Left Ventricle (anchoring the mitral valve cusps to papillary muscles)",
        "Right Atrium (spanning the terminal crest to the coronary sinus valve)"
    ],
    "van_exp_086": [
        "L1 to L4 (between the crura of the diaphragm in dorsal abdomen)",
        "T10 to T13 (adjacent to the thoracic duct in posterior mediastinum)",
        "L5 to S2 (within the pelvic canal dorsal to the internal iliac vessels)"
    ],
    "van_exp_087": [
        "Superficial Cervical Lymph Node (Prescapular lymph node center)",
        "Subiliac Lymph Node (Prefemoral lymph node in flank fold)",
        "Popliteal Lymph Node (Deep caudal stifle lymph node center)"
    ],
    "van_exp_088": [
        "Tensor fasciae latae muscle, in the fold of the flank",
        "Biceps brachii muscle, at the cranial border of shoulder",
        "Sternocephalicus muscle, along the ventral jugular furrow"
    ],
    "van_exp_089": [
        "Splenic vein, Cranial Mesenteric vein, and Caudal Mesenteric vein",
        "Renal vein, Hepatic vein, and Phrenicoabdominal venous trunk",
        "Internal Iliac vein, External Iliac vein, and Caudal Vena Cava"
    ],
    "van_exp_091": [
        "Cribriform plate of the Ethmoid bone (Lamina cribrosa)",
        "Hypoglossal canal of the Occipital bone (Canalis hypoglossi)",
        "Stylomastoid foramen of the Temporal bone (Foramen stylomastoideum)"
    ],
    "van_exp_092": [
        "Optic Canal of the Presphenoid bone (Canalis opticus)",
        "Foramen orbitorotundum of the Sphenoid complex bone",
        "Foramen lacerum of the Basioccipital and Temporal bones"
    ],
    "van_exp_093": [
        "CN III (Oculomotor), CN IV (Trochlear), and CN VI (Abducent)",
        "CN II (Optic), CN V (Trigeminal), and CN VII (Facial)",
        "CN IX (Glossopharyngeal), CN X (Vagus), and CN XII (Hypoglossal)"
    ],
    "van_exp_094": [
        "Foramen Ovale (or notch in the foramen lacerum)",
        "Foramen Rotundum (transmitting maxillary nerve CN V2)",
        "Orbital Fissure (transmitting ophthalmic nerve CN V1)"
    ],
    "van_exp_095": [
        "Cranial Nerve VII (Facial Nerve), exiting through the Stylomastoid Foramen",
        "Cranial Nerve V (Trigeminal Nerve), exiting through the Oval Foramen",
        "Cranial Nerve XII (Hypoglossal Nerve), exiting through the Hypoglossal Canal"
    ],
    "van_exp_096": [
        "Cricoarytenoideus Dorsalis muscle (CAD, the sole laryngeal abductor)",
        "Cricoarytenoideus Lateralis muscle (CAL, laryngeal adductor muscle)",
        "Thyroarytenoideus muscle (vocal fold relaxer and sphincter muscle)"
    ],
    "van_exp_099": [
        "Obturator Nerve inside the pelvic canal against the shaft of the ilium",
        "Femoral Nerve as it penetrates the deep lacuna musculorum",
        "Pudendal Nerve within the ischiorectal fossa near the pelvic outlet"
    ],
    "van_exp_101": [
        "Suprascapular Nerve as it winds around the cranial border of scapula",
        "Radial Nerve as it enters the spiral groove of the humerus shaft",
        "Musculocutaneous Nerve as it passes between coracobrachialis heads"
    ],
    "van_exp_102": [
        "Femoral Nerve (innervating the Quadriceps Femoris muscle)",
        "Sciatic Nerve (innervating the Hamstring and distal limb muscles)",
        "Peroneal Nerve (innervating the Cranial Tibial and digital extensors)"
    ],
    "van_exp_103": [
        "Oculosympathetic pathway (cervical sympathetic trunk / T1-T3)",
        "Parasympathetic oculomotor pathway (Edinger-Westphal nucleus / CN III)",
        "Trigeminal sensory pathway (Ophthalmic division CN V1 axons)"
    ],
    "van_exp_104": [
        "First Intercoccygeal space (Co1-Co2) or Sacrococcygeal space (S5-Co1)",
        "Lumbosacral space (L6-S1 in ruminants / L7-S1 in carnivores)",
        "Interlumbar space between Lumbar 4 and Lumbar 5 vertebrae"
    ],
    "van_exp_105": [
        "Lumbar 7 (L7) and Sacral 1 (S1) vertebrae (Lumbosacral space)",
        "Thoracic 13 (T13) and Lumbar 1 (L1) vertebrae (Thoracolumbar space)",
        "Lumbar 3 (L3) and Lumbar 4 (L4) vertebrae (Mid-lumbar space)"
    ],
    "van_exp_106": [
        "Atlanto-Occipital Space (between the occipital condyles and atlas)",
        "Atlanto-Axial Space (between the atlas and axis dorsal spines)",
        "Lumbosacral Space (between the last lumbar vertebra and sacrum)"
    ],
    "van_exp_107": [
        "Relaxation and desensitization of the retractor penis muscle",
        "Total motor paralysis of the hindlimbs and recumbency of the bull",
        "Complete sympathetic block causing severe systemic hypotension"
    ],
    "van_exp_108": [
        "Zygomaticotemporal nerve (branch of Trigeminal CN V1 / V2)",
        "Infratrochlear nerve (branch of Nasociliary nerve CN V1)",
        "Supraorbital nerve (branch of Frontal nerve of Trigeminal)"
    ],
    "van_exp_109": [
        "T13 (Costoabdominal), L1 (Iliohypogastric), and L2 (Ilioinguinal) nerves",
        "L3 (Genitofemoral), L4 (Femoral), and L5 (Obturator) spinal nerves",
        "T10, T11, and T12 intercostal nerves along the caudal costal arch"
    ],
    "van_exp_110": [
        "Sternocephalicus muscle (specifically sternomandibularis in ox)",
        "Brachiocephalicus muscle (cleidomastoideus and cleido-occipitalis)",
        "Omohyoideus muscle (subclavius and omohyoid cervical fascia)"
    ],
    "van_exp_111": [
        "Fibrocartilage (e.g., intervertebral discs and pelvic symphysis)",
        "Costal cartilage (hyaline cartilage of the thoracic wall ribs)",
        "Elastic cartilage (auricular cartilage of the external ear pinna)"
    ],
    "van_exp_112": [
        "Volkmann's canals (Perforating vascular channels)",
        "Haversian canals (Longitudinal central osteonal canals)",
        "Canaliculi (Microscopic osteocyte cytoplasmic processes)"
    ],
    "van_exp_113": [
        "One central T-tubule flanked by two sarcoplasmic reticulum terminal cisternae",
        "Two longitudinal T-tubules flanked by a single central sarcoplasmic cisterna",
        "Three parallel myofibrils encircled by continuous subsarcolemmal caveolae"
    ],
    "van_exp_120": [
        "Pacinian corpuscles (Lamellar mechanoreceptors sensing vibration)",
        "Meissner's corpuscles (Tactile encapsulated receptors sensing light touch)",
        "Ruffini corpuscles (Spindle-shaped mechanoreceptors sensing skin stretch)"
    ],
    "van_exp_121": [
        "Space of Disse (Perisinusoidal space containing Ito / stellate cells)",
        "Space of Mall (Periportal space between connective tissue and hepatocytes)",
        "Canal of Hering (Bile ductule lined by cholangiocytes and hepatocytes)"
    ],
    "van_exp_124": [
        "Hassall's corpuscle (Thymic corpuscle of degenerated reticular cells)",
        "Malpighian corpuscle (Splenic lymphoid follicle with central arteriole)",
        "Herring body (Neurosecretory terminal dilatations in neurohypophysis)"
    ],
    "van_exp_127": [
        "Type II Pneumocyte (Great alveolar cell synthesizing surfactant)",
        "Type I Pneumocyte (Squamous cell providing gas exchange barrier)",
        "Alveolar macrophage (Dust cell phagocytosing particulate debris)"
    ],
    "van_exp_129": [
        "The axial skeleton (vertebrae, neural arches, and ribs)",
        "All skeletal musculature of the body trunk and limbs",
        "Dermis of the dorsal trunk skin and subcutaneous connective tissue"
    ],
    "van_exp_133": [
        "Ligamentum teres hepatis (Round ligament of the liver)",
        "Ligamentum venosum (Fibrous remnant of the ductus venosus)",
        "Ligamentum arteriosum (Fibrous remnant of the ductus arteriosus)"
    ],
    "van_exp_135": [
        "Paramesonephric duct (Müllerian duct forming uterus and oviducts)",
        "Mesonephric duct (Wolffian duct forming epididymis and deferent duct)",
        "Pronephric duct (Transient non-functional cranial embryonic pronephros)"
    ],
    "van_exp_140": [
        "Right and Left Clavicles (along with the median interclavicle)",
        "Two Coracoid bones (struts bracing the shoulder against sternum)",
        "Two Scapulae (sword-like blade bones dorsal to the rib cage)"
    ],
    "van_exp_141": [
        "Pectoralis muscle (Pectoralis major causing the wing downstroke)",
        "Supracoracoideus muscle (Deep pectoral causing the wing upstroke)",
        "Latissimus dorsi muscle (Superficial dorsal muscle retracting wing)"
    ],
    "van_exp_143": [
        "Parabronchi (Air capillaries) with unidirectional airflow",
        "Blind alveolar saccules with bidirectional tidal airflow",
        "Alveolar ducts and sacs terminating in respiratory bronchioles"
    ],
    "van_exp_145": [
        "Koilin layer (hardened protein secreted by mucosal tubular glands)",
        "Keratinized stratified squamous epithelium with stratum corneum",
        "Dense mucosal glycocalyx layer with high neutral mucin content"
    ]
}

with open('scripts/overrides_van_87.json', 'w', encoding='utf-8') as f:
    json.dump(VAN_OVERRIDES, f, indent=2)

print(f"Successfully generated {len(VAN_OVERRIDES)} VAN overrides in scripts/overrides_van_87.json")
