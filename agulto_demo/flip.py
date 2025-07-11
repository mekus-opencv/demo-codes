import cv2

image = cv2.imread("sample.jpg")

# Flip vertically (upside down)
flipped = cv2.flip(image, 0)

cv2.imshow("Flipped Image", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
