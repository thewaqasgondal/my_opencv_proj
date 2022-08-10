# Masking

import numpy as np
import cv2

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