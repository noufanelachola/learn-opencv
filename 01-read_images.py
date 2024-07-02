import cv2 as cv



#Reading Images
# img = cv.imread("Photos\Screenshot 2024-04-25 095632.png", 0)
# cv.imshow("Window",img)
# cv.waitKey()


#Reading videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    if isTrue : 
        cv.imshow("Video",frame)
        # cv.imshow("Video",cv.cvtColor(frame, cv.COLOR_BGR2GRAY))

        
        if cv.waitKey(20) & 0xFF==ord("d"):
            print("Button pressed")
            break

    else : 
        print("no more frames")
        break        

capture.release()
cv.destroyAllWindows()

