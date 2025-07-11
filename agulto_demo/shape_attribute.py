import cv2

image = cv2.imread("image.png")
print(image.shape)

cv2.imwrite("output.jpg", image)