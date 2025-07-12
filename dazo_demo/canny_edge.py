import cv2

img = cv2.imread("image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny_edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()