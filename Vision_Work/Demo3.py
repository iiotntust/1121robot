# -*- coding: utf-8 -*-


import cv2
import numpy as np

img = cv2.imread('./data/messi5.jpg')

height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('resize', res)
cv2.imshow('src img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
