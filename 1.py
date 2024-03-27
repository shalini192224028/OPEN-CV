import cv2
def convert_to_grayscale(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image.")
        return
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = r"C:\Users\benic\OneDrive\Pictures\wallpaper.jpg"
convert_to_grayscale(image_path)
