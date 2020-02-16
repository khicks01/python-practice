import cv2
import numpy as np

#dummy function
def dummy(value):
    pass

color_orig = cv2.imread('Mallie.jpg')
gray_orig = cv2.cvtColor(color_orig,cv2.COLOR_BGR2GRAY)

#create UI (window and track bars)
cv2.namedWindow('app')

cv2.createTrackbar('contrast', 'app', 1, 3, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy) # TODO: add filters
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)
 
#main UI loop
while True:
    #read all trackbar values
    grayscale = cv2.getTrackbarPos('greyscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    
    color_modified = cv2.addWeighted(color_orig, contrast, np.zeros_like(color_orig), 0, (brightness-50))
    gray_modified = cv2.addWeighted(gray_orig, contrast, np.zeros_like(gray_orig), 0, (brightness-50))

    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('s'):
        # TODO: save image
        pass
    if grayscale == 0:
        cv2.imshow('app',color_modified)
    else:
        cv2.imshow('app', gray_modified)
cv2.destroyAllWindows()