import cv2 as cv

img = cv.imread("Photos\IMGL7539.jpg")

resize = cv.resize(img,(800,500),cv.INTER_AREA)
cv.imshow("image",resize)

average = cv.blur(resize,(3,3))
cv.imshow("average",average)

gauss = cv.GaussianBlur(resize,(3,3),0)
cv.imshow("Gaussian",gauss)

median = cv.medianBlur(resize,3)
cv.imshow("Median",median)

bilateral = cv.bilateralFilter(resize,10,35,25)
cv.imshow("Bilateral",bilateral)


cv.waitKey(0)