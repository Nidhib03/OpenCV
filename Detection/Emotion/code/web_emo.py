import cv2 
from deepface import DeepFace
faceCascade =cv2.CascadeClassifier('/home/rao/anaconda3/envs/Emotion/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(-1)
while True:
    ret, frame = cap.read()
    result = DeepFace.analyze(frame, actions = ['emotion'])
    print(result)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (60,60),
                    font, 1,
                    (0,0,255),
                    2,
                    cv2.LINE_4)
        cv2.imshow('Original video', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()