import cv2

# Load an image
image = cv2.imread("image.png")  # You can replace this image

# Let the user draw a region of interest
roi = cv2.selectROI("Select ROI", image, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

# roi is a tuple: (x, y, w, h)
x, y, w, h = roi

# Crop the selected region from the original image
cropped_roi = image[y:y+h, x:x+w]

# Display the cropped region
cv2.imshow("Selected ROI", cropped_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()