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

 # Localisation des visages dans une image 
   ```python
import face_recognition
image=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Group/group_1.jpg')
face_location=face_recognition.face_locations(image)
print(face_location)
```
##### Fonctionnalité 
Le code permet de localiser avec précision tous les visages présents dans l'image (groupe_1) en retournant leurs positions sous forme de coordonnées rectangulaires.
##### Résultat 
<img width="1831" height="186" alt="image" src="https://github.com/user-attachments/assets/6e811569-3ad4-42ec-b261-985e376ebbac" />

