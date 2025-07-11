import cv2

# Load the original image
image = cv2.imread("image.png")

height, width, channel = image.shape
print(image.shape)

# Draw a blue circle
cv2.circle(image, (100, 100), 40, (255, 0, 0), 2)

cv2.imshow("Circle Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()