import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
# cv.imshow('Blank', blank)

#Draw a space
#blank[200:300 , 200:300] = 255,255,0
#cv.imshow('Green', blank)

#draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=1)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=5)
cv.imshow('line', blank)

#draw a line 2
cv.line(blank,(0,0),(0,255),(255,255,255),thickness=1)
cv.imshow('Line2',blank)

#draw a text
cv.putText(blank,'Hello',(225,125), cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),5)
cv.imshow('Text',blank)

cv.waitKey(0)