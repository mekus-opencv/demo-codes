import cv2

filename = "image.png"
img = cv2.imread(filename)

cv2.imshow("Image Preview", img)

cv2.waitKey(0)
cv2.destroyAllWindows()