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
  * dlib est correctement compilé (requiert un compilateur C++ comme Visual Studio Build Tools sous Windows).
    
