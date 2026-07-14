import cv2 as cv
import numpy as np

img = cv.imread('Photo/image.png')

cv.imshow('Me',img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x],[0, 1, y]])
    diminsions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, diminsions)

translated = translate(img, -100, -100)
# cv.imshow('Translated',translated)

# -x = Left
# -y = Up
# +x = Right
# +Y = Down


#Rotation
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (w//2, h//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimiinsions = (w, h)

    return cv.warpAffine(img, rotMat, dimiinsions)

rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

#Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#Flip
flipped = cv.flip(img, -1)
# cv.imshow('Flipped', flipped)

# Cropping
cropped = img[100:400, 100:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)