import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Change codec to XVID
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    for frame_number in range(total_frames - 1, -1, -1):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Reversed Video", frame)
        cv2.waitKey(int(1000 / fps))
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = r"C:\Users\sanja\Downloads\car_-_2165 (360p).mp4"
    output_video_path = "output_video.avi"  # Change output video format to AVI
    reverse_video(input_video_path, output_video_path)
    cv2.destroyAllWindows()
