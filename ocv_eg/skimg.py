# import cv2
# from cv2 import imread
# # defining the variable which read the image path for the image to be Processed
# img_1 = imread('car.jpg')
# # defining the coordinated for the four corners represented y,x,h and w which are used to crop the source image appropriately
# y1=100
# x1=100
# h1=500
# w1=500
# cropimage_1 = img_1[x1:w1, y1:h1] # Displaying the output image which has been cropped as per the provided coordinates
# cv2.imshow("Cropped", cropimage_1)
# cv2.waitKey(0)

'''Draw bounding box around contours – skimage
'''

import numpy as np
from skimage.draw import polygon_perimeter

from skimage.measure import find_contours
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

orig_img = imread('abcd.png')
gray_img = rgb2gray(orig_img)
plt.imshow(gray_img,interpolation='nearest', cmap=plt.cm.gray)

bounding_boxes = []

contours = find_contours(gray_img, 0.8)

fig, ax = plt.subplots()
ax.imshow(gray_img, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contours[n][:, 1], contours[n][:, 0], linewidth=2)

plt.show()

for contour in contours:
    Xmin = np.min(contour[:,0])
    Xmax = np.max(contour[:,0])
    Ymin = np.min(contour[:,1])
    Ymax = np.max(contour[:,1])
    
    bounding_boxes.append([Xmin, Xmax, Ymin, Ymax])


with_boxes  = np.copy(gray_img)

for box in bounding_boxes:
    #[Xmin, Xmax, Ymin, Ymax]
    r = [box[0],box[1],box[1],box[0], box[0]]
    c = [box[3],box[3],box[2],box[2], box[3]]
    rr, cc = polygon_perimeter(r, c, with_boxes.shape)
    with_boxes[rr, cc] = 1 #set color white

plt.imshow(with_boxes, interpolation='nearest', cmap=plt.cm.gray)
plt.show()
