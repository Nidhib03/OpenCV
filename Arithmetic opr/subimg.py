# Python program to illustrate arithmetic operation of subtraction of pixels of two images

import cv2
import numpy as np

image1 = cv2.imread('star.jpg')
image2 = cv2.imread('dot.jpg')

# cv2.subtract is applied over the image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image with the subtracted image
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()