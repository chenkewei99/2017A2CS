## this is the programme to detect typical points on a person's face


import cv2
import dlib
import time
import pygame


def recognize(img, faces):
    if (len(faces) > 0):
        for k,d in enumerate(faces):
            cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
            v = landmark_predictor(img,d)
    return v
            # for i in range(68):
            #     # print(shape.part(i).x, shape.part(i).y)
            #     cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
            #     cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
# time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
# print(time_end - time_start)
# cv2.imshow('Frame',img)
# cv2.waitKey(0)

def face(mode,shape):
    if mode == "smile":
        # if abs(shape.part(46).y-shape.part(54).y)<50 and (shape.part(51).y-shape.part(57).y)>50:
        return True
    return False

# in this part, we use the camera and we are able to show it on a pygame interface
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('D:\python\shape_predictor_68_face_landmarks.dat')
score=0
pygame.init()
my_font = pygame.font.SysFont('data\\font\\TORK____.ttf', 50)
surface = pygame.display.set_mode((960, 480))
cap = cv2.VideoCapture(0)
k=0
while True:
    # get a frame
    ret, frame = cap.read()
    ev = pygame.event.poll()  # Look for any event
    cv2.imwrite("szf.jpg", frame)
    # img2 = pygame.transform.scale(pygame.image.load(frame), (960, 560))
    szf = pygame.image.load("szf.jpg")
    img = cv2.imread('szf.jpg')
    faces = detector(img, 1)
    if ev.type == pygame.QUIT:
        break
    # show a frame
    # cv2.imshow("capture", frame)
    surface.fill((0, 200, 255))
    s=str(score)
    the_text = my_font.render(s, True, (255, 0, 0))
    surface.blit(the_text, (800, 240))
    surface.blit(szf, (0, 0))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if k==20:
        s = recognize(img,faces)
        if face("smile",s):
            score += 10
        k=0
    k+=1
    pygame.display.flip()
cap.release()
cv2.destroyAllWindows()


# detector = dlib.get_frontal_face_detector()
# landmark_predictor = dlib.shape_predictor('D:\python\shape_predictor_68_face_landmarks.dat')
# img = cv2.imread('D:\python\how to think like a computer scientists\\szf.jpg')
# faces = detector(img,1)
# if (len(faces) > 0):
#     for k, d in enumerate(faces):
#         cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255, 255, 255))
#         shape = landmark_predictor(img, d)
#     for i in range(68):
#         # print(shape.part(i).x, shape.part(i).y)
#         cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
#         cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
# print(shape.part(46).y,shape.part(54).y)
# cv2.imshow('Frame',img)
# cv2.waitKey(0)
