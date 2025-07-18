# Projet de Reconnaissance Faciale
## Comparaison entre face_recognition et DeepFace

Ce projet explore deux bibliothèques populaires pour la reconnaissance faciale en Python
 * face_recognition : est une bibliothèque Python dédiée à la reconnaissance faciale, offrant des fonctionnalités essentielles pour le traitement d'images :

    * ✅ Comparaison de visages entre deux ou plusieurs images

    * ✅ Détection et identification des visages dans une image

    * ✅ Comptage automatique du nombre de visages présents

    * ✅ Annotation des visages (ajout de cadres ou traits autour des visages détectés)
  * DeepFace : est une bibliothèque avancée de reconnaissance faciale offrant des fonctionnalités d'analyse approfondie :
    * 🔍 Identification démographique : estimation précise de l'âge et du genre

    * 😊 Analyse des émotions : détection des expressions faciales (joie, colère, tristesse ....)

    * 🆔 Reconnaissance faciale avancée avec plusieurs modèles (VGG-Face, Facenet, ArcFace)

    * 📊 Métriques détaillées : scores de confiance et comparaisons faciales
    
### Exploration de face_recognition
#### Prérequis d'installation
Avant d'installer face_recognition, assurez-vous que : 
  * CMake est installé et ajouté au PATH (lien d'installation : https://cmake.org/download/)
  * Wheel est installé  (commande d'installation : pip install wheel)
  * dlib est correctement compilé (requiert un compilateur C++ comme Visual Studio Build Tools sous Windows https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/).
#### Comparaison faciale 
##### Commande de base pour la comparaison faciale
```python
face_recognition C:\Users\PC\Desktop\FaceRecognition\Pictures/Known C:\Users\PC\Desktop\FaceRecognition\Pictures/Unknown
```
##### Fonctionnalité 
Cette commande compare chaque image du dossier Unknown avec les images du dossier Known et retourne :
* Le nom de la personne reconnue (si une correspondance est trouvée).
* unknown_person (si aucun visage connu n'est détecté).
##### Explication 
* Dossier Known : contient  des images de références 
* Dossier Unknown : Contient les images à analyser (visages non étiquetés)
* Sortie : Un rapport CSV-like affichant les paires image_inconnue, personne_identifiée.
  
  <img width="1687" height="261" alt="Cmparaison" src="https://github.com/user-attachments/assets/c571ab45-d050-4c9c-8b64-1810aebc636e" />

 #### Localisation des visages dans une image 
   ```python
import face_recognition
image=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Group/group_1.jpg')
face_location=face_recognition.face_locations(image)
print(face_location)
```
##### Fonctionnalité 
Le code permet de localiser avec précision tous les visages présents dans l'image (groupe_1) en retournant leurs positions sous forme de coordonnées rectangulaires.
##### Sortie 
<img width="1831" height="186" alt="image" src="https://github.com/user-attachments/assets/6e811569-3ad4-42ec-b261-985e376ebbac" />

#### Comptage des visages dans une image
 ```python
print(f"Il y a {len(face_locations)} personnes dans cette image ")
```
##### Fonctionnalité
Ce code permet de déterminer le nombre de visages détectés dans une image en utilisant la longueur de la liste retournée par face_recognition.face_locations().
##### Sortie 
<img width="1841" height="212" alt="image" src="https://github.com/user-attachments/assets/a9a243b4-3f7d-475b-938e-ef5fce9bb2a8" />

#### Encodage des visages
 ```python
Albert_Einstein=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png')
Albert_face_encoding=face_recognition.face_encodings(Albert_Einstein)[0]
```
##### Fonctionnalité
La fonction face_recognition.face_encodings() convertit les visages détectés en signatures numériques uniques (vecteurs de 128 dimensions), permettant des comparaisons et identifications précises.
#### Comparaison de visages avec face_encoding et compare_faces
 ```python
# Encodage des deux visages dans deux images différent 
Albert_Einstein=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png')
Albert_face_encoding=face_recognition.face_encodings(Albert_Einstein)[0]

Unknown_img=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Unknown/Erwin.jpg')
Unknown_img_face_encoding=face_recognition.face_encodings(Unknown_img)[0]

# Comparaison des deux visages 

Resultat=face_recognition.compare_faces([Albert_face_encoding],Unknown_img_face_encoding)
if Resultat[0]:
    print("c'est Albert Einstein ") 
else :
   print("ce n'est pas Albert Einstein ")
```
##### Fonctionnalité
Ce code permet de comparer deux visages en générant leurs signatures numériques (face_encoding) puis en évaluant leur similarité avec compare_faces, affichant si le visage inconnu correspond à Albert Einstein.
##### Sortie 
<img width="1826" height="180" alt="image" src="https://github.com/user-attachments/assets/590e9c95-7992-46af-aee3-cab07ab68f39" />

#### Extraction et Sauvegarde des Visages Détectés
 ```python
index=0
# Isolation de chaque visage dans l'image et l'enregistrer  
for face_location in face_locations : 
    top, right, bottom, left=face_location
    face_image=image[top:bottom, left:right]
    pil_image=Image.fromarray(face_image)
    index=index+1
    #pil_image.show()
    pil_image.save(f'visage_{index}.jpg', quality=95)
```
##### Fonctionnalité
Ce code isole chaque visage détecté dans une image et l'enregistre individuellement sous forme de fichier JPEG.

#### Détection et Annotation des Points Clés Faciaux
```python
image = face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png')
face_landmarks_list = face_recognition.face_landmarks(image)
# Convertir l'image numpy array en image PIL
pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)
# Dessiner les landmarks sur l'image
for face_landmarks in face_landmarks_list:
    for facial_feature, points in face_landmarks.items():
        # Dessiner des lignes entre les points pour chaque partie du visage
        draw.line(points, fill=(0, 0, 255), width=1) 

# Afficher l'image avec les landmarks
pil_image.show()
```
##### Fonctionnalité
Ce code détecte les 68 points clés du visage (yeux, nez, bouche) d'Albert Einstein via face_landmarks, permettant de visualiser ses traits faciaux



### Exploration de DeepFace
