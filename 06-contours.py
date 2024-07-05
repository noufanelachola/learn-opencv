import cv2 as cv
import numpy as np

img = cv.imread("Photos\img.png")


resize = cv.resize(img,(800,500),interpolation=cv.INTER_AREA)
cv.imshow("Image",resize)

blank = np.zeros(resize.shape[0:2],dtype="uint8")
cv.imshow("Blank",blank)

gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# blur = cv.GaussianBlur(gray,(5,5),0,borderType=cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("Canny",canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank,contours,-1,(255,0,0),1)
cv.imshow("Contours",blank)

cv.waitKey(0)