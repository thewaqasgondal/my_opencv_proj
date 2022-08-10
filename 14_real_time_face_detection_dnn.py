import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_detection_model = cv2.dnn.readNetFromCaffe('./models_dnn/deploy.prototxt.txt',
                                                './models_dnn/res10_300x300_ssd_iter_140000_fp16.caffemodel')

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    img_detection = face_detection_dnn(frame)

    cv2.imshow('Real Time Face Detection with DNN', img_detection)
    if cv2.waitKey(1) == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()