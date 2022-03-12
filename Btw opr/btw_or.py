# arithmetic operation of bitwise OR of two images
	
import cv2
import numpy as np
	
img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')

# cv2.bitwise_or is applied over the image inputs with applied parameters
btw_or = cv2.bitwise_or(img2, img1, mask = None)

# the window showing output image with the Bitwise OR operation on the input images
cv2.imshow('Bitwise OR', btw_or)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()