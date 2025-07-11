# | Video Capture Example
# | Author: Mekus Team
# | Description:
# | This code captures video from a file and displays it in a window.
# | It resizes the video frames to a fixed size for consistency.
# | Press 'ESC' to exit the video feed.

import cv2

ESC_KEY = 27  # ASCII code for ESC key
WAIT_KEY_DELAY = 1  # Delay for waitKey in milliseconds
FRAME_SIZE = (640, 480)  # Fixed size for video frames

cap = cv2.VideoCapture(
    "video.mp4"
)  # Initialize video capture from default camera

if not cap.isOpened():
    print("Error: Could not initialize video stream.")
    exit()

while True:
    ret, frame = cap.read()  # Read a single frame from the camera

    if not ret:
        print("Empty frame received, exiting...")
        break  # Exit if frame capture fails

    resized_frame = cv2.resize(
        frame, FRAME_SIZE
    )  # Resize the frame to a fixed size for consistency

    # Display the resulting frame
    cv2.imshow("Video Feed", resized_frame)

    # Wait indefinitely for a key press (0 = wait forever)
    if cv2.waitKey(WAIT_KEY_DELAY) == ESC_KEY:
        break  # Exit loop if 'ESC' key is pressed

cap.release()  # Release the camera resource
cv2.destroyAllWindows()  # Close all OpenCV windows
