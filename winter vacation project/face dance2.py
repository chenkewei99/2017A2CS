import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 30)

image1 = 'Angry.png'
image2 = 'rollingeyes.png'
image3 = 'Smiling.png'
image4 = 'black.jpg'

bgimage1 = pygame.image.load(image1).convert()
bgimage2 = pygame.image.load(image2).convert()
bgimage3 = pygame.image.load(image3).convert()
bgimage4 = pygame.image.load(image4).convert()
bgimage = [bgimage4,bgimage1,bgimage2,bgimage3]

x1, y1 = 0, 0
# 第一张左上角的坐标

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    x1 -= 6 #滑动的速度
    if x1 <= -2000:
        bgimage = bgimage[1:]+bgimage[:1]
        bgimage1,bgimage2,bgimage3,bgimage4 = bgimage
        x1 = 0

    screen.blit(bgimage4, (x1, y1))
    screen.blit(bgimage4, (x1+600, y1))
    screen.blit(bgimage1, (x1+1200, y1))
    screen.blit(bgimage4, (x1+1800, y1))
    screen.blit(bgimage4, (x1+2400, y1))
    screen.blit(bgimage2, (x1+3000, y1))
    screen.blit(bgimage4, (x1+3600, y1))
    screen.blit(bgimage4, (x1+4200, y1))
    screen.blit(bgimage3, (x1+4800, y1))
    screen.blit(bgimage4, (x1+5400, y1))
    screen.blit(bgimage4, (x1+6000, y1))

    pygame.display.update()