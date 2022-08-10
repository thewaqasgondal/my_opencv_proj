import numpy as np
import cv2

img = cv2.imread('faces.jpg')

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')


def face_detection(img):
    image = img.copy()
    # step-1: Convert image into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # step-2: apply gray scale image to cascasde classifier
    box, detections = face_cascade.detectMultiScale2(gray, minNeighbors=8)
    # step-3: drawing bounding box
    for x, y, w, h in box:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    return image


img_detect = face_detection(img)

cv2.imshow('face detection', img_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()