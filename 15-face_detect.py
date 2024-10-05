import cv2 as cv

img = cv.imread("Photos\download.jpg")
# img = cv.imread("Photos\BC.png")
resized = cv.resize(img,(400,450),cv.INTER_AREA)

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("haar_cascade.xml")

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors = 3 )
print(faces_rect)

for (x,y,w,g) in faces_rect:
    cv.rectangle((resized),(x,y),(x+w,y+g),(0,255,0),thickness=2)

cv.imshow("Image",resized)
cv.imshow("Gray",gray)

print(f"Number of people is = {len(faces_rect)}")

cv.waitKey(0)