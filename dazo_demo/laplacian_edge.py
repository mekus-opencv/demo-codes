import cv2

img = cv2.imread("image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow("Laplacian Edge Detection", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()