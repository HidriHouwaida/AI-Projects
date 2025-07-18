import face_recognition
from PIL import Image
# Localisation des visages dans une image 
image=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Group/group_1.jpg')
face_locations=face_recognition.face_locations(image)
print(face_location)


# Compter le nombre des visages dans une image 
print(f"Il y a {len(face_locations)} personnes dans cette image ")


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
index=0
# Isolation de chaque visage dans l'image et l'enregistrer  
for face_location in face_locations : 
    top, right, bottom, left=face_location
    face_image=image[top:bottom, left:right]
    pil_image=Image.fromarray(face_image)
    index=index+1
    #pil_image.show() 
    pil_image.save(f'visage_{index}.jpg', quality=95)
# Dessiner les Contours de visage d'Albert 
face_landmarks_list = face_recognition.face_landmarks(Albert_Einstein)
# Convertir l'image numpy array en image PIL
pil_image = Image.fromarray(Albert_Einstein)
draw = ImageDraw.Draw(pil_image)
# Dessiner les landmarks sur l'image
for face_landmarks in face_landmarks_list:
    for facial_feature, points in face_landmarks.items():
        # Dessiner des lignes entre les points pour chaque partie du visage
        draw.line(points, fill=(0, 0, 255), width=1) 

# Afficher l'image avec les landmarks
pil_image.show()
