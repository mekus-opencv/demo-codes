import cv2

image = cv2.imread("image.png")
resized = cv2.resize(image, (300, 200))

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()