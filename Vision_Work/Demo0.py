# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)


# img = cv2.imread('messi5.jpg',cv2.IMREAD_COLOR)#Read in a color image. Image transparency is ignored
# img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)# Load an color image in grayscale 
img = cv2.imread('./data/messi5.jpg',cv2.IMREAD_UNCHANGED)

img = cv2.resize(img, (640, 480))

rows,cols,ch=img.shape

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)

cv2.imshow('image', img) #
# Press any key on the window to exit
cv2.waitKey(delay=0)
cv2.destroyAllWindows()
