import cv2

# Read the image.
img = cv2.imread('Blur.png')

# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

# Save the output.
cv2.imwrite('bilateral.png', bilateral)