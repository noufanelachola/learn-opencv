import cv2 as cv
import numpy as np

img = cv.imread("Photos/IMGL7539.jpg")
resized = cv.resize(img,(800,500),cv.INTER_AREA)
blank = np.zeros(resized.shape[0:2],dtype="uint8")

mask = cv.circle(blank,(resized.shape[1]//2,resized.shape[0]//2),100,255,-1)

cv.imshow("Resized",resized)
cv.imshow("Blank",blank)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(resized,resized,mask=mask)
cv.imshow("Masked",masked)


cv.waitKey(0)