import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
#show OpenCV version
print(cv2.__version__)
#read image and convert to grayscale
image = cv2.imread('per.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#instantiate surf object
surf  = cv2.xfeatures2d.SURF_create(400)
keypoints = surf.detect(gray, None)
#calculate keypoints and their orientation
keypoints, descriptors = surf.detectAndCompute(gray,None)

with_keypoints = cv2.drawKeypoints(gray,keypoints, None)

plt.imshow(with_keypoints)
plt.show()



''' ERROR
Traceback (most recent call last):
  File "surf_.py", line 11, in <module>
    surf  = cv2.xfeatures2d.SURF_create(400)
cv2.error: OpenCV(4.5.5) /io/opencv_contrib/modules/xfeatures2d/src/surf.cpp:1027: error: (-213:The function/feature is not implemented) 
This algorithm is patented and is excluded in this configuration; 
Set OPENCV_ENABLE_NONFREE CMake option and rebuild the library in function 'create'
'''
