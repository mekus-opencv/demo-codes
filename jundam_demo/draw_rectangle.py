import cv2

# Load the original image
image = cv2.imread("image.png")

height, width, channel = image.shape
print(image.shape)

# Draw a red rectangle
cv2.rectangle(image, (150, 100), (300, 200), (0, 0, 255), 3)

cv2.imshow("Rectangle Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()