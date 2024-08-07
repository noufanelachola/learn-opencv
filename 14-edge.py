import cv2 as cv
import numpy as np

img = cv.imread("Photos\BC.png")
resized = cv.resize(img,(400,450),cv.INTER_AREA)
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian",lap)

sobelX = cv.Sobel(gray,cv.CV_64F,1,0)
sobelY = cv.Sobel(gray,cv.CV_64F,0,1)

sobel = cv.bitwise_or(sobelX,sobelY)

cv.imshow("SobelX",sobelX)
cv.imshow("SobelY",sobelY)
cv.imshow("Sobel",sobel)

canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)