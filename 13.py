import cv2
import numpy as np
video_capture = cv2.VideoCapture(r"C:\Users\benic\OneDrive\Desktop\OPEN CV\imax.mp4")
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
source_points = np.float32([[50, 50], [300, 50], [300, 200], [50, 200]])
destination_points = np.float32([[100, 100], [250, 50], [200, 300], [50, 250]])
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (width, height))
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (width, height))
    output_video.write(transformed_frame)
    cv2.imshow('Transformed Frame', transformed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
output_video.release()
cv2.destroyAllWindows()
