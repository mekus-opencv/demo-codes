import cv2

# Load and resize the image
image = cv2.imread("image.png")

height, width, channel = image.shape
print(image.shape)

# Crop a region
cropped_img = image[200:500, 400:750]

cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()