import cv2
import mediapipe as mp

cap = cv2.VideoCapture("/home/rao/Documents/pyPro/CV/Detection/2face.mp4")

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)

            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (112, 25, 15), 3)

    cv2.imshow("Faces", img)
    cv2.waitKey(1)


                      # OR
# # Load the cascade
# face_cascade = cv2.CascadeClassifier('/home/rao/Documents/pyPro/CV/Detection/haarcascade_frontalface_default.xml')

# # To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# # To use a video file as input 
# cap = cv2.VideoCapture('/home/rao/Documents/pyPro/CV/Detection/2face.mp4')

# while True:
#     # Read the frame
#     _, img = cap.read()
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Detect the faces
#     faces = face_cascade.detectMultiScale(gray, 1.2, 4)
#     # Draw the rectangle around each face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+w), (146, 35, 0), 3)
#     # Display
#     cv2.imshow('faces', img)
#     # Stop if escape key is pressed
#     k = cv2.waitKey(30) & 0xff
#     if k==27:
#         break
# # Release the VideoCapture object
# cap.release()