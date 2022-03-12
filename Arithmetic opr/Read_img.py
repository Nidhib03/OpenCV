# Python code to read image
import cv2

img = cv2.imread("rao.png", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen first Parameter is windows title (should be in string format) Second Parameter is image array
cv2.imshow("rao", img)

# To hold the window on screen, we use cv2.waitKey method
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will hold the screen until user close it.
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
