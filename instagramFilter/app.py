import cv2
import numpy as np

#dummy function
def dummy(value):
    pass

identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
gauss_k1 = cv2.getGaussianKernel(3, 0)
gauss_k2 = cv2.getGaussianKernel(1, 5)
box_k = np.ones(9, np.float32) / 9.0

kernels = [identity_kernel, sharpen_kernel, gauss_k1, gauss_k2, box_k ]


color_orig = cv2.imread('Mallie.jpg')
gray_orig = cv2.cvtColor(color_orig,cv2.COLOR_BGR2GRAY)

#create UI (window and track bars)
cv2.namedWindow('app')

cv2.createTrackbar('contrast', 'app', 1, 3, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy) # TODO: add filters
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)

count = 0
#main UI loop
while True:
    #read all trackbar values
    grayscale = cv2.getTrackbarPos('greyscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    kernel = cv2.getTrackbarPos('filter', 'app')
    
    #apply filters
    color_modified = cv2.filter2D(color_orig, -1, kernels[kernel])
    gray_modified = cv2.filter2D(gray_orig, -1, kernels[kernel])
    
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_orig), 0, (brightness-50))
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_orig), 0, (brightness-50))

    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('s'):
        if grayscale == 0:
            cv2.imwrite('output-{}.png'.format(count), color_modified)
        else:
            cv2.imwrite('output-{}.png'.format(count), gray_modified)
        count +=1
        pass
    if grayscale == 0:
        cv2.imshow('app',color_modified)
    else:
        cv2.imshow('app', gray_modified)
cv2.destroyAllWindows()