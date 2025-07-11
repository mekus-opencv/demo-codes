# | Object Tracking with Template Matching using OpenCV
# | Author: Team Mekus
# | Description:
# | This Python script is intended for academic purposes only.
# | It demonstrates object tracking using template matching with OpenCV.
# | Have fun and enjoy learning!

import cv2

# Constants
CAMERA_INDEX = 0  # Default camera index (0 for built-in webcam)

MATCHING_METHOD = (
    cv2.TM_CCOEFF_NORMED
)  # Normalized cross-correlation coefficient

WAIT_KEY_DELAY = 1  # Delay for waitKey in milliseconds
ESC_KEY = 27  # ASCII code for ESC key

DETECTION_THRESHOLD = 0.8  # Threshold for detection confidence

TEXT_POSITION = (10, 30)  # Position for displaying text
FONT_SIZE = 0.8  # Font size for text
COLOR_GREEN = (0, 255, 0)  # Green color in BGR format
PIXEL_THICKNESS = 2  # Thickness of the rectangle and text in pixels

# === Initialize video capture ===
cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# === Capture initial frame ===
is_success, frame = cap.read()
if not is_success:
    print("Error: Could not capture frame.")
    cap.release()
    exit()

# === Let user select ROI (Region of Interest) ==
roi = cv2.selectROI("Select Object to Track", img=frame, fromCenter=False)
cv2.destroyWindow("Select Object to Track")  # Close the selection window

# === Print selected ROI ===
print(f"ROI selected: {roi}")

# === Extract template from ROI ===
# Unpack ROI coordinates (x, y, width, height)
roi_x, roi_y, roi_width, roi_height = roi

# Create the template from the selected ROI through slicing
template = frame[roi_y : roi_y + roi_height, roi_x : roi_x + roi_width]

# Unpack template dimensions (height, width, channels)
template_height, template_width, template_channels = template.shape

# === Main tracking loop ===
while True:
    is_success, frame = cap.read()

    # Exit the loop if frame capture fails
    if not is_success:
        print("Error: Could not read frame.")
        break

    # === Perform TEMPLATE MATCHING ===
    result = cv2.matchTemplate(
        image=frame, templ=template, method=MATCHING_METHOD
    )

    # Unpack min and max values and locations
    # (min_val, max_val, min_loc, max_loc)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Only draw rectangle if we have a good match (if max_val exceeds threshold)
    if max_val > DETECTION_THRESHOLD:
        top_left = max_loc  # Top-left corner of the matched area
        bottom_right = (
            top_left[0] + template_width,
            top_left[1] + template_height,
        )  # Bottom-right corner of the matched area

        # === Draw rectangle around matched area ===
        cv2.rectangle(
            img=frame,
            pt1=top_left,
            pt2=bottom_right,
            color=COLOR_GREEN,  # Green
            thickness=PIXEL_THICKNESS,
        )

    # === Display the match confidence ===
    cv2.putText(
        img=frame,
        text=f"Match Confidence: {max_val:.2f}",
        org=TEXT_POSITION,
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=FONT_SIZE,
        color=COLOR_GREEN,
        thickness=PIXEL_THICKNESS,
    )

    # === Show the frame with the tracking rectangle ===
    cv2.imshow("Object Tracking", frame)

    # Exit on ESC key
    if cv2.waitKey(WAIT_KEY_DELAY) == ESC_KEY:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
