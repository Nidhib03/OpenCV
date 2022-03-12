# Python program to explain cv2.imread() method

import cv2

path = r'rao.png'

# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)

# Displaying the image
cv2.imshow('image', img)