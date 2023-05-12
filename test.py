import pygame
from pygame.locals import *
import math as m

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

def trigo(a):
    b = m.sqrt(250**2-(a**2))
    print(b)
    pygame.draw.circle(screen, (255,255,0), (a+300,b+300), 2)

pygame.draw.circle(screen, (255,0,0), (300,300), 250, 1)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONUP:
            trigo(int(input("x ? : ")))
        if event.type== pygame.KEYUP:
            #for k in range(0, 260, 10):
            #    trigo(k)
            s=pygame.Surface((600,600))
            s.set_alpha(50)
            s.fill(pygame.Color(0, 0, 0))
            screen.blit(s, (0,0))
    
    pygame.display.flip()

pygame.quit()