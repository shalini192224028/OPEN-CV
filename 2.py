import cv2

def apply_gaussian_blur(image_path, kernel_size=(5, 5), sigma_x=0):
    # Read the image
    img = cv2.imread(image_path)
    
    
    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(img, kernel_size, sigma_x)
    
    # Display the original and blurred images
    cv2.imshow('Original Image', img)
    cv2.imshow('Blurred Image', blurred_img)
    
  
# Path to the image file
image_path = r"C:\Users\benic\OneDrive\Pictures\wallpaper.jpg"

# Call the function to apply Gaussian blur to the image
apply_gaussian_blur(image_path, kernel_size=(15, 15), sigma_x=0)
