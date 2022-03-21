from numpy import asarray
from PIL import Image
import mtcnn
import matplotlib.pyplot as plt
import cv2

def extract_face_from_image(image_path, required_size=(224, 224)):
  # load image and detect faces
    image = cv2.imread(image_path)               # plt.imread(image_path)  ->o/p in blue
    detector = mtcnn.MTCNN()
    faces = detector.detect_faces(image)
    face_images = []

    for face in faces:
        # extract the bounding box from the requested face
        x1, y1, w, h = face['box']
        x2, y2 = x1 + w, y1 + h
       
        # extract the face
        face_boundary = image[y1:y2, x1:x2]
        cv2.imwrite("cropimg/"+str(w) + str(h) + '_faces.jpg', face_boundary)
        
        # resize pixels to the model size
        face_image = Image.fromarray(face_boundary)
        face_image = face_image.resize(required_size)
        face_array = asarray(face_image)
        face_images.append(face_array)
    return face_images

extracted_face = extract_face_from_image('stu.jpg')

# Display the first face from the extracted faces
plt.imshow(extracted_face[1])
plt.show()
