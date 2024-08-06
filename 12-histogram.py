import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos\IMGL7539.jpg")
resize = cv.resize(img,(800,500),cv.INTER_AREA)
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
blank = np.zeros(gray.shape[0:2],dtype="uint8")

circle = cv.circle(blank,(gray.shape[1]//2,gray.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(gray,gray,mask=circle)

gray_hist = cv.calcHist([gray],[0],circle,[256],[0,256])

plt.figure()
plt.title("Grayscale histogram")

plt.plot(gray_hist)

plt.xlabel("Bins")
plt.ylabel("# of pixels")

plt.xlim([0,256])


cv.imshow("image",gray)
cv.imshow("masked",mask)
# plt.show()

# Color histogram

colors = ("b","g","r")

plt.figure()
plt.title("Colorscale histogram")

plt.xlabel("Bins")
plt.ylabel("# of pixels")

plt.xlim([0,256])


for i,color in enumerate(colors):
    hist = cv.calcHist([resize],[i],circle,[256],[0,256])
    plt.plot(hist,color=color)

plt.show()

cv.waitKey(0)