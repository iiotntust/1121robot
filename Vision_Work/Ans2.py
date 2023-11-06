import numpy as np
import cv2

cap = cv2.VideoCapture('./data/vtest.avi')


# frame
fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
# How many frames are there in total?
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('How many frames are there in total : ', num_frames,)
#
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('Hight：', frame_height, 'Width：', frame_width)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
print('Now frames', FRAME_NOW)  # 'Now frames

# Read the specified frame
# frame_no = 121
# cap.set(1, frame_no)  # Where frame_no is the frame you want
# ret, frame = cap.read()  # Read the frame
# cv2.imshow('frame_no'+str(frame_no), frame)
#
# FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
# print('Now frames', FRAME_NOW)  # Now frames 122.0

while cap.isOpened():
    ret, frame = cap.read()
    FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # Now frames
    print('Now frames', FRAME_NOW)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
