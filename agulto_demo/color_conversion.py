import cv2

image = cv2.imread("image.png")
converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Output Image", converted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()