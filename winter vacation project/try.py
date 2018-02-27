# import cv2
#
# img = cv2.imread("D:\\python\how to think like a computer scientists\zhy5.jpg")
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey (0)
# cv2.destroyAllWindows()

# import cv2
# import dlib
# import time
# time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数
# detector = dlib.get_frontal_face_detector()
# landmark_predictor = dlib.shape_predictor('D:\python\shape_predictor_68_face_landmarks.dat')
# time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
# print(time_end-time_start)
# img = cv2.imread('D:\python\how to think like a computer scientists\\basketball1.jpg')
# faces = detector(img,1)
# time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
# print(time_end-time_start)
# if (len(faces) > 0):
#     for k,d in enumerate(faces):
#         cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
#         shape = landmark_predictor(img,d)
#         for i in range(68):
#             cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
#             cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
# # time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
# # print(time_end - time_start)
# cv2.imshow('Frame',img)
# cv2.waitKey(0)

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("尚壮飞照片.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()
