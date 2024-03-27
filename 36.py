import cv2
image_path = r"C:\Users\benic\OneDrive\Pictures\Saved Pictures.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to load image.")
    exit()
print("Loading Haar cascade for watch detection...")
watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_watch.xml')
if watch_cascade.empty():
    print("Error: Unable to load the Haar cascade for watch detection.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Detecting watches...")
watches = watch_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Detected Watches', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
