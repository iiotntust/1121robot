# -*-coding:utf8-*-#


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/lena.jpg', 0)
img2 = img.copy()
template = cv2.imread('./data/Lean_face.jpg', 0)

w, h = template.shape[::-1]
img = img2.copy()

# Apply template Matching
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print("min_loc",min_loc)
top_left = min_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, 255, 2)

plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
