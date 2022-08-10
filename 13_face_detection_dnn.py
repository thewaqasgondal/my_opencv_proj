
import numpy as np
import cv2

img = cv2.imread('faces.jpg')

cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

face_detection_model = cv2.dnn.readNetFromCaffe('./models_dnn/deploy.prototxt.txt',
                                                './models_dnn/res10_300x300_ssd_iter_140000_fp16.caffemodel')


def face_detection_dnn(img):
    # step-1: blob from image
    blob = cv2.dnn.blobFromImage(img,1,(300,300),(104,177,123),swapRB=True)
    # step-2: set blob as input
    face_detection_model.setInput(blob)
    # step-3: get the output
    detections = face_detection_model.forward()
    #  step-4: drawing boundng box on top of face detected
    image = img.copy()
    h,w = image.shape[:2]
    for i in range(0,detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence > 0.5:
            # diagonal points 3: 7
            box = detections[0,0,i,3:7]*np.array([w,h,w,h])
            box = box.astype('int')
            pt1 = (box[0],box[1])
            pt2 = (box[2],box[3])
            # draw rectangle
            cv2.rectangle(image,pt1,pt2,(0,255,0),1)

            text = 'score : {:.0f} %'.format(confidence*100)
            cv2.putText(image,text,pt1,cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    return image

img_detect = face_detection_dnn(img)

cv2.imshow('face detection',img_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()

