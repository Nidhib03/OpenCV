''' code 1'''
import numpy as np
import cv2

im = cv2.imread('word.jpg')
im[im == 255] = 1
im[im == 0] = 255
im[im == 1] = 0
im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im2,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(0, len(contours)):
    if (i % 2 == 0):
       cnt = contours[i]
       #mask = np.zeros(im2.shape,np.uint8)
       #cv2.drawContours(mask,[cnt],0,255,-1)
       x,y,w,h = cv2.boundingRect(cnt)
       cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
       cv2.imshow('Features', im)
       cv2.imwrite(str(i)+'.jpg', im)

cv2.destroyAllWindows()

'''code 2'''
# import cv2

# image = cv2.imread('word.jpg')
# copy = image.copy()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# ROI_number = 0
# for c in cnts:
#     x,y,w,h = cv2.boundingRect(c)
#     ROI = image[y:y+h, x:x+w]
#     cv2.imwrite('ROI_{}.jpg'.format(ROI_number), ROI)
#     cv2.rectangle(copy,(x,y),(x+w,y+h),(36,255,12),2)
#     ROI_number += 1

# cv2.imshow('thresh', thresh)
# cv2.imshow('copy', copy)
# cv2.waitKey()