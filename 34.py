import cv2
import numpy as np
image = cv2.imread(r"C:\Users\benic\OneDrive\Desktop\OPEN CV\royal.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)  
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
top_hat = cv2.subtract(image, opening)
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
