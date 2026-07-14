import cv2 as cv

img = cv.imread('Photo/image.png')

cv.imshow('Me',img)

cv.waitKey(0)