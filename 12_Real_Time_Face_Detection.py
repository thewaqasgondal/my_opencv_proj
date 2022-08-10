import numpy as np
import cv2


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    img_detect = face_detection(frame)

    cv2.imshow('Real Time Face Detection' ,img_detect)
    if cv2.waitKey(1) == ord('a'):
        break


cap.release()
cv2.destroyAllWindows()