from cv2 import SIFT
import numpy as np
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

#reading images in grayscale format
image1 = cv2.imread('per.jpg',0)
image2 = cv2.imread('Rotate.jpg',0)

#finding out the keypoints and their descriptors
# kp1,ds1 = cv2.detectAndCompute(image1,None)
kp1 , ds1 = cv2.SIFT().detectAndCompute(image1, None)
kp2 , ds2 = cv2.SIFT().detectAndCompute(image2, None)
keypoints = SIFT.detect(image1, None)
keypoints = SIFT.detect(image2, None)

#matching the descriptors from both the images 
bf = cv2.BFMatcher()
matches = bf.knnMatch(ds1,ds2,k = 2)

#selecting only the good features
good_matches = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good_matches.append([m])

image3 = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good_matches,flags = 2)