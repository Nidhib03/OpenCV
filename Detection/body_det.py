import cv2 
import imutils 
   
# Initializing the HOG person 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
   
# Reading the Image 
image = cv2.imread('/home/rao/Documents/pyPro/CV/Detection/frame.jpg') 
   
# Resizing the Image 
image = imutils.resize(image, 
                       width=min(500, image.shape[1])) 
   
# Detecting all humans 
(humans, _) = hog.detectMultiScale(image,  
                                    winStride=(1, 1), 
                                    padding=(0, 0), 
                                    scale=1.21)
# getting no. of human detected
print('Human Detected : ', len(humans))
   
# Drawing the rectangle regions
for (x, y, w, h) in humans: 
    cv2.rectangle(image, (x, y),  
                  (x + w, y + h),  
                  (125, 142, 2), 2) 
  
# Displaying the output Image 
cv2.imshow("Human", image) 
cv2.waitKey(0) 
   
cv2.destroyAllWindows()