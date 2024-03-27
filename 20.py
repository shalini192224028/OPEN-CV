import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\benic\OneDrive\Pictures\wallpaper.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Laplacian filter with a negative center coefficient
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)
sharpened_image = gray_image - 0.6 * laplacian  # You can adjust the coefficient value (-0.6 in this case)

# Convert back to uint8
sharpened_image = np.uint8(sharpened_image)

# Add the sharpened image to the original image
final_image = cv2.addWeighted(gray_image, 1.5, sharpened_image, -0.5, 0)

# Display the original image, sharpened image, and final result
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('Final Sharpened Result', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
