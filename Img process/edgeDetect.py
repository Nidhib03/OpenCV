import cv2
import numpy as np

FILE_NAME = 'rao.png'
try:
	img = cv2.imread(FILE_NAME)

	# Canny edge detection.
	edges = cv2.Canny(img, 100, 200)

	cv2.imwrite('Edg.jpg', edges)
except IOError:
	print ('Error while reading files !!!')
