import cv2 as cv
import numpy as np

img = cv.imread("Photos\img.png")
cv.imshow("Image",img)

# transformation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
cv.imshow("Translated",translated)

# rotation
def rotate(img,angle,rotPoint=None):
    height,width = img.shape[0:2]

    if rotPoint is None : 
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)

    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,90)
cv.imshow("Rotated",rotated)

cv.waitKey(0)