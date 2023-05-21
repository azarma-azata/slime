import pygame, time
from pygame.locals import *
import math as m

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

a=pygame.image.load("data/items/sword.png")
image=pygame.transform.scale(a, (200,200))
i=0
meh=False

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
        if event.type== pygame.KEYUP:
            #for k in range(0, 260, 10):
            #    trigo(k)
            if event.key == K_1:
                s=pygame.Surface((600,600))
                s.set_alpha(50)
                s.fill(pygame.Color(0, 0, 0))
                screen.blit(s, (0,0))
            if event.key == K_2:
                trigo(int(input("x ? : ")))
            if event.key == K_3:
                meh = True


    if meh:
        b=pygame.transform.rotate(image, 10*i)
        screen.blit(b, (200,200))
        pygame.display.flip()
        i+=1
        time.sleep(1/10)
    
    if i==20:
        meh=False
        i=0

    pygame.display.flip()

pygame.quit()