import cv2 as cv

img = cv.imread('Photo/image.png')

cv.imshow('Me',img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#converting to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('BLUR',blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny',canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), 3)
# cv.imshow('Diliated',dilated)

#Eroding
eroded = cv.erode(dilated,(3,3), 1)
# cv.imshow('Eroded',eroded)

#Resize
resize = cv.resize(img, (750,750), interpolation=cv.INTER_CUBIC)
# cv.imshow('resize',resize)

#Cropping
cropped = img[50:200,200:400]
# cv.imshow('Cropped',cropped)

cv.waitKey(0)