import cv2 as cv

def rescaleframe (frame,scale = 0.75) : 
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

def resChange(capture, width, height):
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)


img = cv.imread("Photos\Screenshot 2024-04-25 095632.png")
rescaledImg = rescaleframe(img)

cv.imshow("Image",img)
cv.imshow("Rescaled Img",rescaledImg)


capture = cv.VideoCapture(0)
# capture = cv.VideoCapture("E:\BACK-UP\CASTLE\ASDF\Ma'din\Xth\VID-20220611-WA0026.mp4")

if not capture.isOpened() : 
    print("Couldn't open the file")
    
elif capture.isOpened() : 
    resChange(capture,10,10)
    while True :
        isTrue,frame = capture.read()
        # rescaledVideoFrame = rescaleframe(frame)

        if isTrue : 
            cv.imshow("video",frame)
            # cv.imshow("Rescaled video",rescaledVideoFrame)
            
            if cv.waitKey(20) & 0xFF == ord("q") : 
                print("q pressed")    
                break

        else : 
            print("No more frames")
            break

    capture.release()
    cv.destroyAllWindows()
