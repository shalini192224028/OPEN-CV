import cv2
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_slow = cv2.VideoWriter('output_video_slow.mp4', fourcc, fps / 2, (output_width, output_height))
output_video_fast = cv2.VideoWriter('output_video_fast.mp4', fourcc, fps * 2, (output_width, output_height))  a

# Read and process each frame
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Apply slow motion
    output_video_slow.write(frame)
    output_video_slow.write(frame)

    # Apply fast motion
    output_video_fast.write(frame)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
output_video_slow.release()
output_video_fast.release()
cv2.destroyAllWindows()
