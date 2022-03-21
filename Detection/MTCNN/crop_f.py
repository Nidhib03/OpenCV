import cv2

# Read the input image
img = cv2.imread('/home/rao/anaconda3/envs/Detect/people_with_phones.png')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('/home/rao/anaconda3/envs/haarcascade_frontalface_default.xml')

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h),(0, 0, 255), 2)
    faces = img[y:y + h, x:x + w]
    cv2.imshow("face",faces)
    cv2.imwrite('1.jpg', faces)
# Display the output
cv2.imwrite('detcted.jpg', img)
cv2.imshow('img', img)
cv2.waitKey()