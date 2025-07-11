import cv2

# Load the original image
image = cv2.imread("image.png")

height, width, channel = image.shape
print(image.shape)

# Draw yellow text
cv2.putText(
    image,
    "Dann Kyle Jundam",
    (100, 150),
    cv2.FONT_HERSHEY_TRIPLEX,
    1,
    (0, 255, 255),
    1,
)

cv2.imshow("Text Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()