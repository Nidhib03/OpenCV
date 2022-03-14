import cv2
face_cascade=cv2.CascadeClassifier('/home/rao/Documents/pyPro/CV/Detection/haarcascade_frontalface_default.xml')
img= cv2.imread('/home/rao/Documents/pyPro/CV/Detection/crowd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
cv2.imshow('img', img)
cv2.waitKey()
