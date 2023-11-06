import numpy as np
import cv2

img = cv2.imread('./data/messi5.jpg',cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (640, 480))
rows,cols,ch=img.shape
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

print("rows=",rows)
print("cols=",cols)


cv2.imshow('image', img)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()