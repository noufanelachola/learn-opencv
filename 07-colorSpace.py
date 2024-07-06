import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./Photos/img.png")
cv.imshow("Image",img)

plt.imshow(img)
plt.show()

