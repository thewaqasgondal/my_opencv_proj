# Control Brightness of Image

import numpy as np
import cv2

img = cv2.imread('./images/bird.jpg')
cv2.imshow('car', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def nothing(x):
    pass


cv2.namedWindow('Brightness Control')
bright = cv2.createTrackbar('Brightness', 'Brightness Control', 75, 255, nothing)
value = np.ones_like(img, dtype='uint8')

while True:
    bright = cv2.getTrackbarPos('Brightness', 'Brightness Control')
    bar = bright - 127

    if bar >= 0:
        value = np.ones_like(img, dtype='uint8') * bar
        img_ctrl = cv2.add(img, value)

    else:
        bright = 127 - bright
        value = np.ones_like(img, dtype='uint8') * bright
        img_ctrl = cv2.subtract(img, value)

    cv2.imshow('Brightness Control', img_ctrl)

    if cv2.waitKey(1) == 27:  # esc button
        break

cv2.destroyAllWindows()

