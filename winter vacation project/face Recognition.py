## this is the programme to detect typical points on a person's face


import cv2
import dlib
import time
# time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('D:\python\shape_predictor_68_face_landmarks.dat')
# time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
# print(time_end-time_start)
img = cv2.imread('D:\python\how to think like a computer scientists\\basketball1.jpg')
faces = detector(img,1)
# time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
# print(time_end-time_start)
if (len(faces) > 0):
    for k,d in enumerate(faces):
        cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
        shape = landmark_predictor(img,d)
        for i in range(68):
            print(shape.part(i).x, shape.part(i).y)
            cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
            cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
# time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
# print(time_end - time_start)
cv2.imshow('Frame',img)
cv2.waitKey(0)



## in this part, we use the camera and we are able to show it on a pygame interface
import cv2
import pygame

pygame.init()
surface = pygame.display.set_mode((960, 480))
cap = cv2.VideoCapture(0)
while True:
    # get a frame
    ret, frame = cap.read()
    ev = pygame.event.poll()  # Look for any event
    cv2.imwrite("szf.jpg", frame)
    # img2 = pygame.transform.scale(pygame.image.load(frame), (960, 560))
    ball = pygame.image.load("szf.jpg")
    if ev.type == pygame.QUIT:
        break
    pygame.display.flip()
    surface.blit(ball, (0,0))
    # show a frame
    # cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
