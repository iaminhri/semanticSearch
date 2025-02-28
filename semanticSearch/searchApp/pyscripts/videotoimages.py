import cv2

def extract_frame(video_path, time_sec):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None
    
    # Set the time position to the specified second
    cap.set(cv2.CAP_PROP_POS_MSEC, time_sec*1000)

    ret, frame = cap.read()
    cap.release()

    if ret:
        # Save the frame as an image file
        frame_filename = f'/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/images/temp_frame.jpg'
        cv2.imwrite(frame_filename, frame)
        return frame_filename
    return None
