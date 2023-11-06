import cv2
import numpy as np


img=cv2.imread('./data/messi5.jpg')

ball=img[280:340,330:390]

w=ball.shape[0]
h=ball.shape[1]

img[280:280+w,130:130+h]=ball

cv2.namedWindow("messi",0)
cv2.imshow("messi",img)
cv2.waitKey(0)