import numpy as np
import cv2

img = cv2.imread('./images/flemingo.jpg')

def display(winame,img):
    cv2.imshow(winame,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

display('bird',img)

# Image Translation
tx = 100 # right
ty = 150 # download
M = np.float32([[1,0,tx],
         [0,1,ty]])
M


shifted_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
display('shifted righ 100, down 150',shifted_img)

def translation(image,tx,ty):
    M = np.float32([[1,0,tx],
         [0,1,ty]])
    shifted_img = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    display('shifted',shifted_img)

translation(img,-100,-150)

# Rotate

display('bird', img)

center = (img.shape[1] // 2, img.shape[0] // 2)

M = cv2.getRotationMatrix2D(center, 45, 1)
M

rotate_45 = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

display('rotate 45 anti clock', rotate_45)


def rotate(image, angle, scale):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotate_img = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    display('rotate', rotate_img)


rotate(img,-30,0.3)

# Resixe
img.shape

img_resize = cv2.resize(img,(300,300),interpolation=cv2.INTER_AREA)

display('resize',img)

cv2.imshow('orginal',img)
cv2.imshow('resize',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_resize = cv2.resize(img,(400,300),interpolation=cv2.INTER_AREA)

cv2.imshow('orginal',img)
cv2.imshow('resize',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Flipping
flip_img = cv2.flip(img,0) # 1,-1,0

cv2.imshow('orignal_image',img)
cv2.imshow('flip image',flip_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cropping
display('image',img)

crop = img[100:400,100:400]

display('crop',crop)
