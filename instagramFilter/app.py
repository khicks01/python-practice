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
#create UI (window and track bars)
cv2.namedWindow('app')

cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
 
#todo: remove this line
cv2.waitKey(0)
cv2.destroyAllWindows()