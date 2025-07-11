import cv2

# Load the original image
image = cv2.imread("image.png")

height, width, channel = image.shape
print(image.shape)

# Draw a green line
cv2.line(image, (50, 50), (500, 150), (0, 255, 0), 3)

cv2.imshow("Line Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()