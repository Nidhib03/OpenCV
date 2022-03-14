import cv2
face_cascade=cv2.CascadeClassifier('/home/rao/Documents/pyPro/CV/Detection/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(-1)

while True:
    ret, im = cap.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow('Webcam',im)
    
    k= cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()