#importing the required libraries 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
# %matplotlib inline 
image = cv2.imread('rao.png') 
#converting RGB image to Binary 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(gray_image, 127, 255, 0) 
#calculate the contours from binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
with_contours = cv2.drawContours(image, contours, -1, (0,255,0), 3) 
plt.imshow(with_contours)
plt.show()