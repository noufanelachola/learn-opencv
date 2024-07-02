import cv2 as cv

img = cv.imread("Photos\img.png")
# cv.imshow("image",img)

#cvtColor
grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",grayImg)

# Gaussian blur
gaussian = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian",gaussian)

#Edge ditection
edge = cv.Canny(gaussian,50,100)
cv.imshow("Canny",edge)

#dilate
dilate = cv.dilate(edge,(3,3),iterations=5)
cv.imshow("dilated",dilate)

# erode
erode = cv.erode(dilate,(3,3),iterations=5)
cv.imshow("Erode",erode)

# Rezise
resize = cv.resize(img,(500,200),interpolation=cv.INTER_AREA)
cv.imshow("resize",resize)

cropped = img[200:500,250:int(img.shape[1])]
cv.imshow("cropped",cropped)

cv.waitKey(0)