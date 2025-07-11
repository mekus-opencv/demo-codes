import cv2
import numpy as np

img = cv2.imread("image.png")
img = cv2.resize(img, (600, 400))

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(img, -1, sharpen_kernel)

cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()