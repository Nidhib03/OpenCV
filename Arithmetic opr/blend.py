'''IMAGE Blending''' 
 
import cv2  
 
img1 = cv2.imread('raoit.png')
img2 = cv2.imread('opnc.png')
bln = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('img blending',bln)
cv2.waitKey(0)
cv2.destroyAllWindows() 
 
 