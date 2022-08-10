import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")

def display(winname,image):
    cv2.imshow(winname,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

display('canvas',canvas)

cv2.imwrite('canvas.png',canvas)

green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
display('canvas',canvas)

red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)
display('canvas', canvas)

# Drawing Rectangle

cv2.rectangle(canvas,(10,10),(60,60),green)
display('canvas',canvas)

cv2.rectangle(canvas,(50,200),(200,225),red,5)
display('canvas',canvas)

blue = (255,0,0)
cv2.rectangle(canvas,(200,50),(225,200),blue,-1)
display('canvas',canvas)

# Circles
canvas = np.zeros((300,300,3),dtype='uint8')

centerx, centery = (canvas.shape[1] //2 , canvas.shape[0] // 2)
white = (255,255,255)

for r in range(0,175,25):
    cv2.circle(canvas,(centerx,centery),r,white)

display('circles',canvas)

# Abstract Drawing
for i in range(0, 25):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 256, size=(3,)).tolist()
    pt = np.random.randint(0, 300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

display('canvas', canvas)

cv2.imwrite('canvas.png',canvas)


