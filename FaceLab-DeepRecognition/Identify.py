import face_recognition
from PIL import Image, ImageDraw


#Encodage des deux visages qu'on va les chercher 
Albert_Einstein=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Albert.png')
Albert_face_encoding=face_recognition.face_encodings(Albert_Einstein)[0]

Nelson=face_recognition.load_image_file('C:/Users/PC/Desktop/FaceRecognition/Pictures/Known/Nelson.png')
Nelson_face_encoding=face_recognition.face_encodings(Nelson)[0]

#Create Array of encoding and names 
known_face_encodings=[


    Nelson_face_encoding, 
    Albert_face_encoding
]

known_face_names=[
    "Nelson ", 
    "Albert Einstein"
    
]

#Load Test image to find faces in 
test_img=face_recognition.load_image_file("C:/Users/PC/Desktop/FaceRecognition/Pictures/Group/IM.jpg")

face_locations=face_recognition.face_locations(test_img)
face_encodings=face_recognition.face_encodings(test_img, face_locations)

# Convert to PIL format 
pil_image=Image.fromarray(test_img)

# Create an ImageDraw instance 

draw=ImageDraw.Draw(pil_image)

for (top, right,bottom,left), face_encoding in zip(face_locations,face_encodings):
    matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
    name="Unknown Person"
    if True in matches :
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]
# Draw Box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
# Draw Label 
   # Dessin de l'étiquette avec le nom
    # Correction 1: Utilisation correcte de textbbox
    bbox = draw.textbbox((left, bottom), name)  # Arguments requis
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Correction 2: Positionnement correct du rectangle de fond
    draw.rectangle(
        ((left, bottom - text_height - 10), (right, bottom)),
        fill=(0, 0, 0),
        outline=(0, 0, 0)
    )
    
    # Correction 3: Positionnement correct du texte
    draw.text(
        (left + 6, bottom - text_height - 5),
        name,
        fill=(255, 255, 255),
    )

del draw

# Display Image 
pil_image.show()
