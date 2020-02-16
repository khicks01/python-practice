# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

#dummy function
def dummy(value):
    pass

color_orig = cv2.imread('Mallie.jpg')
gray_orig = cv2.cvtColor(color_orig,cv2.COLOR_BGR2GRAY)

#create UI (window and track bars)
cv2.namedWindow('app')

cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy) # TODO: add filters
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)
 
#main UI loop
while True:
    #read all trackbar values
    grayscale = cv2.getTrackbarPos('greyscale', 'app')
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        # TODO: save image
        pass
    if grayscale == 0:
        cv2.imshow('app',color_orig)
    else:
        cv2.imshow('app', gray_orig)
cv2.waitKey(0)
cv2.destroyAllWindows()