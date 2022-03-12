import cv2
import numpy as np

FILE_NAME = 'rao.png'
try:
	img = cv2.imread(FILE_NAME)

	# Get number of pixel horizontally and vertically.
	(height, width) = img.shape[:2]

	# Specify the size of image along with interploation methods.
	# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBI is used for zooming.
	res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite('Scale.jpg', res)

except IOError:
	print ('Error while reading files !!!')