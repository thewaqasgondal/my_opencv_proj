import numpy as np
import cv2

#
# Real Time Brightness Control


def nothing(x):
    pass

cv2.namedWindow('Brightness Control')
bright = cv2.createTrackbar('Brightness','Brightness Control',75,255,nothing)
img = cv2.imread('./images/bird.jpg')
value = np.ones_like(img,dtype='uint8')

def brightness_ctrl(image, bright):
    bar = bright - 127

    if bar >= 0:
        value = np.ones_like(image, dtype='uint8') * bar
        img_ctrl = cv2.add(image, value)

    else:
        bright = 127 - bright
        value = np.ones_like(image, dtype='uint8') * bright
        img_ctrl = cv2.subtract(image, value)

    return img_ctrl


cap = cv2.VideoCapture('./images/clip.mp4')
cv2.namedWindow('Brightness Control')
bright = cv2.createTrackbar('Brightness', 'Brightness Control', 75, 255, nothing)
value = np.ones_like(img, dtype='uint8')

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    bright = cv2.getTrackbarPos('Brightness', 'Brightness Control')
    img_ctrl = brightness_ctrl(frame, bright)

    cv2.imshow('Brightness Control', img_ctrl)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
cap.release()