import cv2

img = cv2.imread("image.png")

box_blur = cv2.blur(img, (10, 10))

cv2.imshow("Box Blur", box_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()