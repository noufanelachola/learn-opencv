import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype="uint8")

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
bitwise_and = cv.bitwise_and(circle,rectangle)
bitwise_or = cv.bitwise_or(circle,rectangle)
bitwise_Xor = cv.bitwise_xor(circle,rectangle)
bitwise_not = cv.bitwise_not(circle)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)
cv.imshow("Bitwise And",bitwise_and)
cv.imshow("Bitwise Or",bitwise_or)
cv.imshow("Bitwise Xor",bitwise_Xor)
cv.imshow("Inverted Circle",bitwise_not)

cv.waitKey(0)