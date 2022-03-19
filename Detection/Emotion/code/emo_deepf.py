# from traceback import print_tb
from turtle import color
import matplotlib.pyplot as plt
from deepface import DeepFace
import cv2
img = cv2.imread("/home/rao/anaconda3/envs/Emotion/20220319_160147.jpg")
plt.imshow(img)
# plt.show()

predictions= DeepFace.analyze(img)
predictions['dominant_emotion']
faceCascade = cv2.CascadeClassifier("/home/rao/anaconda3/envs/Emotion/haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1,4)
for (x, y, w, h) in faces:
    font= cv2.FONT_HERSHEY_SIMPLEX
    org = (60, 60)
    fontScale = 1
    color=(255,0,0)
    thickness= 1
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.putText(img, predictions['dominant_emotion'], org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()