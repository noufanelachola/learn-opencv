import cv2 as cv
import numpy as np

img = cv.imread("Photos\IMG-20240428-WA0019.jpg")

height,width = img.shape[0:2]
ratio = width/height
resize = cv.resize(img,(int(800*ratio),800),interpolation=cv.INTER_AREA)

blank = np.zeros(resize.shape[:2],dtype="uint8")

b,g,r = cv.split(resize)

# cv.imshow("image",resize)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

# merged = cv.merge([b,g,r])
# cv.imshow("merged",merged)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)