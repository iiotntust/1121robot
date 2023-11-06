# -*- coding: utf-8 -*-


import cv2
import numpy as np

img = cv2.imread('./data/j.png', 0)
cv2.imshow('./data/j.png', img)
print(img.shape)

#You can think of the kernel as a small matrix that we slide over the image to perform (convolution) operations
# such as blurring,sharpening, edge detection, or other image processing operations.
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('erode', erosion)
cv2.moveWindow('erode', x=img.shape[1], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()
