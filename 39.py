import cv2

# Load the pre-trained cascade classifier for detecting cars
car_cascade = cv2.CascadeClassifier(r"C:\Users\sanja\Downloads\haarcascade_car.xml")

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\sanja\Downloads\car_-_2165 (360p).mp4")

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the grayscale frame
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the frame with detected cars
    cv2.imshow('frame', frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
