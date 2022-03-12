import cv2
import numpy as np

img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')

btw_not1 = cv2.bitwise_not(img1, mask = None)
btw_not2 = cv2.bitwise_not(img2, mask = None)

cv2.imshow('Bitwise NOT on image 1', btw_not1)
cv2.imshow('Bitwise NOT on image 2', btw_not2)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()