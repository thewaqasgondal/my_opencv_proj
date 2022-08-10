# Bitwise Operations

import numpy as np
import cv2

rectangle = np.zeros((300,300),dtype='uint8')
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)

cv2.imshow('rectangle',rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

circle = np.zeros((300,300),dtype='uint8')
cv2.circle(circle,(150,150),150,255,-1)

cv2.imshow('circle',circle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# AND
img_and = cv2.bitwise_and(rectangle,circle)

cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.imshow('AND',img_and)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OR
img_or = cv2.bitwise_or(rectangle,circle)

cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.imshow('OR',img_or)
cv2.waitKey(0)
cv2.destroyAllWindows()

# NOT
img_not = cv2.bitwise_not(rectangle)

cv2.imshow('img',rectangle)
cv2.imshow('not',img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_not = cv2.bitwise_not(circle)

cv2.imshow('img',circle)
cv2.imshow('not',img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

# XOR
img_xor = cv2.bitwise_xor(rectangle,circle)

cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.imshow('XOR',img_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Masking
img = cv2.imread('./images/beach.jpg')

cv2.imshow('beach',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask = np.zeros(img.shape[:2],dtype='uint8')

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cx,cy = mask.shape[1]//2, mask.shape[0]//2

cv2.rectangle(mask,(cx-200,cy-200),(cx+200,cy+200),255,-1)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_mask = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('original',img)
cv2.imshow('masked image',img_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask_not = cv2.bitwise_not(mask)

cv2.imshow('masknot',mask_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_mask_not = cv2.bitwise_and(img,img,mask=mask_not)

cv2.imshow('original',img)
cv2.imshow('masked image not',img_mask_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

# circle
mask_c = np.zeros(img.shape[:2],dtype='uint8')
cx,cy = mask_c.shape[1]//2, mask_c.shape[0]//2

cv2.circle(mask_c,(cx,cy),200,255,-1)
cv2.imshow('circle',mask_c)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_mask_circle = cv2.bitwise_and(img,img,mask=mask_c)

cv2.imshow('original',img)
cv2.imshow('masked image circle',img_mask_circle)
cv2.waitKey(0)
cv2.destroyAllWindows()


