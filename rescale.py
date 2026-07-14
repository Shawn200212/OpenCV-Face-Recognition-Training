import cv2 as cv


def rescaleFrame(frame, scale = .2):
    #works for all shape[0] for width [1]for height
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Video/Videos.mp4')

while True:
    isTrue,frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()