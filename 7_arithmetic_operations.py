
# Arithmetic Operations

import numpy as np
import cv2

img = cv2.imread('./images/car.jpg')

cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Addition
value = np.ones_like(img,dtype='uint8')*50

cv2.imshow('value',value)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_add = cv2.add(img,value)

cv2.imshow('original',img)
cv2.imshow('addition',img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Subtraction

value = np.ones_like(img,dtype='uint8')*75

img_sub = cv2.subtract(img,value)

cv2.imshow('original',img)
cv2.imshow('subtrated',img_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blending IUmages

img1 = cv2.imread('./images/blend_1.jpg')
img2 = cv2.imread('./images/blend_2.jpg')

blend = cv2.addWeighted(img1,0.5,img2,0.5,40)

cv2.imshow('blend image',blend)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./output/blending.jpg',blend)