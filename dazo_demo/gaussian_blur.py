import cv2

img = cv2.imread("image.png")
img = cv2.resize(img, (600, 400))

gaussian_blur = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()