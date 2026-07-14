import cv2 as cv

img = cv.imread('Photo/image.png')

cv.imshow('1',img)

# averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average', average)

#Gaussian
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian', gaussian)

#Median
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bileteral', bilateral)

cv.waitKey(0)