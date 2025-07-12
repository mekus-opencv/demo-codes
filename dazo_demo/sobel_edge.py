import cv2
import numpy as np

img = cv2.imread("image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", cv2.convertScaleAbs(sobel_x))
cv2.imshow("Sobel Y", cv2.convertScaleAbs(sobel_y))
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()