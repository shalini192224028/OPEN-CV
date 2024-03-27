import cv2
image = cv2.imread(r"C:\Users\benic\OneDrive\Pictures\wallpaper.jpg")
height, width = image.shape[:2]
bigger_scale = 1.5
smaller_scale = 0.5
bigger_image = cv2.resize(image, (int(width * bigger_scale), int(height * bigger_scale)))
smaller_image = cv2.resize(image, (int(width * smaller_scale), int(height * smaller_scale)))
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
