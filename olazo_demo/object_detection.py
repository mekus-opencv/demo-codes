# | Object Detection with Haar Cascade (Real-Time)
# | Author: Team Mekus
# | Description:
# | This demo shows live face detection using Haar cascades in OpenCV.
# | It's built for learning and exploration.
# | Feel free to tweak values and experiment!

import cv2
from cv2.data import haarcascades  # Built-in path to cascade models

# === Constants ===
CAMERA_INDEX = 0  # Default camera index (0 for built-in webcam)

# Haar Cascade model for frontal face detection
FRONTAL_FACE_MODEL = "haarcascade_frontalface_default.xml"

SCALE_FACTOR = 1.1  # Shrink image by 10% each time
MIN_NEIGHBORS = 12  # Minimum overlap to confirm detection

WAIT_KEY_DELAY = 1  # Delay for waitKey in milliseconds
ESC_KEY = 27  # ASCII code for ESC key

COLOR_GREEN = (0, 255, 0)  # BGR format for green
THICKNESS = 2  # Thickness for rectangle border

# === Load Haar Cascade Model ===
cascade_classifier = cv2.CascadeClassifier(
    haarcascades + FRONTAL_FACE_MODEL
)

# === Start Webcam ===
capture = cv2.VideoCapture(CAMERA_INDEX)  # Use index 0 for default camera

if not capture.isOpened():
    print("Error: Could not access camera.")
    exit()

# === Main Detection Loop ===
while True:
    is_success, frame = capture.read()

    # Exit if frame capture fails
    if not is_success:
        print("Error: Could not read frame.")
        break

    # Convert to grayscale for better accuracy
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using Haar cascade
    faces = cascade_classifier.detectMultiScale(
        image=gray_img,
        scaleFactor=SCALE_FACTOR,  # Shrinks image by 10% each time
        minNeighbors=MIN_NEIGHBORS,  # Minimum overlap to confirm detection
    )

    # Draw rectangles around detected faces
    for face in faces:
        x_coord, y_coord, width, height = face
        cv2.rectangle(
            img=frame,
            pt1=(x_coord, y_coord),
            pt2=(x_coord + width, y_coord + height),
            color=COLOR_GREEN,
            thickness=THICKNESS,
        )

    # Display the annotated frame
    cv2.imshow("Real-Time Face Detection", frame)

    # Break loop on ESC key
    if cv2.waitKey(WAIT_KEY_DELAY) == ESC_KEY:
        break

# === Clean up ===
capture.release()
cv2.destroyAllWindows()
