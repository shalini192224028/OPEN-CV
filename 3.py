import cv2
def apply_canny_edge_detection(image_path, min_threshold, max_threshold):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, min_threshold, max_threshold)
    cv2.imshow('Original Image', img)
    cv2.imshow('Edge Detected Image', edges)
image_path = r"C:\Users\benic\OneDrive\Pictures\wallpaper.jpg"
min_threshold = 100
max_threshold = 200
apply_canny_edge_detection(image_path, min_threshold, max_threshold)
