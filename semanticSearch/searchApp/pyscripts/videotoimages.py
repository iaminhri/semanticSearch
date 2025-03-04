import cv2
import logging

logging.basicConfig(level=logging.INFO)

def extract_frame(video_path, time_sec, output_path="/vol/web/media/images/temp_frame.jpg"):
    logging.info(f"Extracting frame from {video_path} at {time_sec}s")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logging.error("Error: Could not open video.")
        return None

    cap.set(cv2.CAP_PROP_POS_MSEC, time_sec * 1000)
    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite(output_path, frame)
        logging.info(f"Frame saved to {output_path}")
        return output_path
    else:
        logging.error("Failed to extract frame.")
        return None
