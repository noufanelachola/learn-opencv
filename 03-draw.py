import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
# cv.imshow("blank",blank)

#Paint the image
# blank[200:300,200:300] = 0,0,255
# cv.imshow("red",blank)

# draw rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
cv.imshow("rectangle",blank)

#Draw circle
cv.circle(blank,(250,250),20,(255,255,255),thickness=-1)
cv.imshow("Circle",blank) 

#Drraw Line
cv.line(blank,(0,0),(250,250),(0,255,255),thickness=5)
cv.imshow("line",blank)

#Write text
cv.putText(blank,"Hello noufu..",(0,250),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(250,45,200))
cv.imshow("text",blank)

cv.waitKey(0)