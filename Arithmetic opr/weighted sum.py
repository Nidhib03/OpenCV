# Python program to illustrate arithmetic operation of addition of two images

import cv2
import numpy as np

image1 = cv2.imread('Collapsed.jpg')
image2 = cv2.imread('Galaxy.jpg')

# cv2.addWeighted is applied over the image inputs with applied parameters
weightedSum = cv2.addWeighted(image1,0.9, image2, 1, 0)

# the window showing output image with the weighted sum
cv2.imshow('Weighted Image', weightedSum)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
