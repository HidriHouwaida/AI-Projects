from deepface import DeepFace
# Comparaison des visages dans deux images 
Comparaison = DeepFace.verify(
  Albert = 'C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png',
  Erwin = 'C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/Erwin.jpg',
)
print(Comparaison)

# Recherche des images semblable à une image spécifique dans un dossier 
Recherche = DeepFace.find(
  Albert = 'C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png',
  Dossier_De_Recherche = 'C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/',
)
print(Recherche)

# Analyse démographique et émotionnelle
Detaction_ED = DeepFace.analyze(
  img_path = 'C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/garcon_riant.jpg', 
  actions = ['age', 'gender', 'race', 'emotion'],
)
print(Detaction_ED)
