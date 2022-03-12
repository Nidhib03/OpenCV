import cv2
import numpy as np
	
img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')

btw_xor = cv2.bitwise_xor(img1, img2, mask = None)

cv2.imshow('Bitwise XOR', btw_xor)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()