import numpy as np
import cv2

img = cv2.imread('./images/bird.jpg')


def display(winname,image):
    cv2.imshow(winname,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

display('winname',img)

img.shape

type(img)

# acess first 100 rows and 100 columns
corners = img[0:100,0:100]

display('corner',corners)

cv2.imshow('original',img)
cv2.imshow('cornor',corners)
cv2.waitKey(0)
cv2.destroyAllWindows()

# change first 100 rows and 100 columns to green color
green = (0,255,0)
img[0:100,0:100] = green

display('manipulate',img)

