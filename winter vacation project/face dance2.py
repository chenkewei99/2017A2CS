import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 24)

image1 = 'Angry.png'
image2 = 'rollingeyes.png'
image3 = 'Smiling.png'

bgimage1 = pygame.image.load(image1).convert()
bgimage2 = pygame.image.load(image2).convert()
bgimage3 = pygame.image.load(image3).convert()
bgimage = [bgimage1, bgimage2, bgimage3]

x1, y1 = 0, 0
# 第一张左上角的坐标

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    x1 -= 6 #滑动的速度
    if x1 <= -500:
        bgimage = bgimage[1:]+bgimage[:1]
        bgimage1, bgimage2, bgimage3 = bgimage
        x1 = 0

    screen.blit(bgimage1, (x1, y1))
    screen.blit(bgimage2, (x1+600, y1))
    screen.blit(bgimage3, (x1+1200, y1))

    pygame.display.update()