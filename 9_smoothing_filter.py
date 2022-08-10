import numpy as np
import cv2

img = cv2.imread('./images/beach.jpg')

cv2.imshow('beach',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Average Blur
blur_avg3 = cv2.blur(img,(3,3))
blur_avg5 = cv2.blur(img,(5,5))
blur_avg7 = cv2.blur(img,(7,7))
blur_avg9 = cv2.blur(img,(9,9))

cv2.imshow('original image',img)
cv2.imshow('blur 3',blur_avg3)
cv2.imshow('blur 5',blur_avg5)
cv2.imshow('blur 7',blur_avg7)
cv2.imshow('blur 9',blur_avg9)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur
blur_gauss_3 = cv2.GaussianBlur(img,(3,3),0)
blur_gauss_5 = cv2.GaussianBlur(img,(5,5),0)
blur_gauss_7 = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow('original',img)
cv2.imshow('blur 3',blur_gauss_3)
cv2.imshow('blur 5',blur_gauss_5)
cv2.imshow('blur 7',blur_gauss_7)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Median Blur
sp = cv2.imread('./images/sp_noise.jpg')

cv2.imshow('salt pepper',sp)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur_median_3 = cv2.medianBlur(sp,3)

cv2.imshow('original',sp)
cv2.imshow('median blur',blur_median_3)

cv2.waitKey(0)
cv2.destroyAllWindows()

blur_median_5 = cv2.medianBlur(sp,5)
blur_median_7 = cv2.medianBlur(sp,7)

cv2.imshow('original',sp)
cv2.imshow('median blur3',blur_median_3)
cv2.imshow('median blur5',blur_median_5)
cv2.imshow('median blur7',blur_median_7)

cv2.waitKey(0)
cv2.destroyAllWindows()