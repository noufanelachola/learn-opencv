import cv2 as cv

img = cv.imread("Photos\BC.png")
resized = cv.resize(img,(400,450),cv.INTER_AREA)
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

# cv.imshow("Image",img)
# cv.imshow("Resize",resized)
cv.imshow("Gray",gray)

#Simple thresholding

threshold,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow("Simple Threshold",thresh)

#Adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adptive Threshold",adaptive_thresh)


cv.waitKey(0)