# arithmetic operation of bitwise AND of two images
	
import cv2
import numpy as np
	
# path to input images are specified and images are loaded with imread command
img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')

# cv2.bitwise_and is applied over the image inputs with applied parameters
btw_and = cv2.bitwise_and(img2, img1, mask = None)

# the window showing output image with the Bitwise AND operation on the input images
cv2.imshow('Bitwise And', btw_and)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
