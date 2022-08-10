import numpy as np
import cv2

img = cv2.imread('./images/flemingo.jpg')

print(img)

img.shape

cv2.imshow('example',img)
cv2.waitKey(10000) # millseconds
cv2.destroyAllWindows()

cv2.imshow('example',img)
cv2.waitKey(0) # millseconds
cv2.destroyAllWindows()

cv2.imwrite('./images/example.png',img)