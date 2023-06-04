"""import pygame, time
from pygame.locals import *
import math as m
import mobs

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

a=pygame.image.load("data/items/sword.png")
image=pygame.transform.scale(a, (200,200))
i=0
meh=False
size = 1
group=pygame.sprite.Group()

def trigo(a):
    b = m.sqrt(250**2-(a**2))
    print(b)
    pygame.draw.circle(screen, (255,255,0), (a+300,b+300), 2)

pygame.draw.circle(screen, (255,0,0), (300,300), 250, 1)

continuer = True
while continuer:
    screen.fill((255,255,255))
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
            if event.key == K_4:
                size+=1
            if event.key == K_5:
                group.add(mobs.Fighter)
            if event.key == K_6:
                group.remove(mobs.Fighter)

    print(group)
    if meh:
        b=pygame.transform.rotate(image, 10*i)
        screen.blit(b, (200,200))
        pygame.display.flip()
        i+=1
        time.sleep(1/10)
    
    if i==20:
        meh=False
        i=0

    
    group.draw(screen)
    pygame.draw.rect(screen, (255,255,0), (100,100,100,100), size)
    pygame.display.flip()

pygame.quit()"""

with open("test.csv", "r", encoding="utf-8") as file:
    a=[k.rstrip().split(";") for k in file.readlines()]
print(a)

with open("test.csv", "w+", encoding="utf-8") as file:
    a[2][2]='152'
    print(a)
    for k in a:
        for n in k:
            file.write(n+";")
        file.write("\n")

with open("test.csv", "r", encoding="utf-8") as file:
    a=[k.rstrip().split(";") for k in file.readlines()]
print(a)