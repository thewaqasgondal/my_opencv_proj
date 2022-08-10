import numpy as np
import cv2

img = cv2.imread('./images/flemingo.jpg') # bgr

img

img.shape

b,g,r = cv2.split(img)

b

cv2.imshow('color',img)
cv2.imshow('blue',b)
cv2.imshow('red',r)
cv2.imshow('green',g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Color Converter


img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('color_bgr',img)
cv2.imshow('color_rgb',img_rgb)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('GRAY.png',gray)