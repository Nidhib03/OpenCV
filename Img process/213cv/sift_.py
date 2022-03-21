from pydoc import describe
import cv2
from cv2 import DescriptorMatcher
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
#show OpenCV version
print(cv2.__version__)
#read the iamge and convert to grayscale
image = cv2.imread('per.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#create sift object
sift  = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray, None)
#calculate keypoints and their orientation
keypoints, Descriptors = sift.detectAndCompute(gray, None)
#plot keypoints on the image
with_keypoints = cv2.drawKeypoints(gray, keypoints, None)
#plot the image
plt.imshow(with_keypoints)
plt.show()