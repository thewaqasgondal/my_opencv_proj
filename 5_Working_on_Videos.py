import numpy as np
import cv2
import time

cap = cv2.VideoCapture('./data/clip.mp4')
fps = 0
while True:
    start_time = time.time()  # start time
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.putText(frame, 'FPS: {:.0f}'.format(fps), (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                (255, 255, 255), 1)
    cv2.imshow('video', frame)
    if cv2.waitKey(41) == ord('q'):
        break

    time_taken = time.time() - start_time  # time taken in seconds
    fps = 1 / time_taken  # frames per seconds

cap.release()
cv2.destroyAllWindows()

1000/24
#
# # Accessing the Web Camera
#
# cap0 = cv2.VideoCapture(0)  # 0 , 1 , ...
# cap1 = cv2.VideoCapture(1)  # 0 , 1 , ...
# fps = 0
# while True:
#     start_time = time.time()  # start time
#     ret, frame0 = cap0.read()
#     ret, frame1 = cap1.read()
#
#     cv2.putText(frame0, 'FPS: {:.0f}'.format(fps), (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
#                 (255, 255, 255), 1)
#     cv2.putText(frame1, 'FPS: {:.0f}'.format(fps), (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
#                 (255, 255, 255), 1)
#
#     # horizantal stack
#     hstack = np.hstack((frame0, frame1))
#
#     cv2.imshow('camera-1', frame0)
#     cv2.imshow('camera-2', frame1)
#     cv2.imshow('camera-12', hstack)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
#     time_taken = time.time() - start_time  # time taken in seconds
#     fps = 1 / time_taken  # frames per seconds
#
# cap.release()
# cv2.destroyAllWindows()
#
# frame0.shape
#
# frame1.shape