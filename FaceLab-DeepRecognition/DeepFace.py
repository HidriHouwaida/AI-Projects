from deepface import DeepFace
# Comparaison des visages dans deux images 
Comparaison = DeepFace.verify(
  img1_path= "C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png",
  img2_path = "C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/Erwin.jpg",
  model_name="Facenet",

)
print(Comparaison)

# Recherche des images semblable à une image spécifique dans un dossier 
Recherche = DeepFace.find(
    img_path="C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png",
    db_path="C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown",
    model_name="Facenet"
)
chemins_similaires = Recherche[0]['identity'].tolist()  # Convertit la colonne en liste
print("Images similaires trouvées:")
for chemin in chemins_similaires:
    print(chemin)
# Analyse démographique et émotionnelle
result = DeepFace.analyze(img_path='C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/garcon_riant.jpg', actions=['age','gender','race','emotion'])[0]
genre_dominant = max(result['gender'].items(), key=lambda x: x[1])[0]

print(f"""
Analyse faciale simplifiée :
- Âge estimé : {result['age']} ans
- Genre : {genre_dominant}
- Origine ethnique : {result['dominant_race']}
- Émotion : {result['dominant_emotion']}
""")
