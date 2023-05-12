import pygame
from pygame.locals import *
import math as m
import manager
import mobs
import gameItems
from player import Player

pressedKeys = {}

#TO DO
"""

-tiles system
-collisions system
-GUI system
-attack system
-inventory system

"""

pygame.init()
#pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode((800,450), RESIZABLE)

player = Player()
hostileMobs = pygame.sprite.Group()
hostileMobs.add(mobs.Fighter)

def update():
    player.update()
    hostileMobs.update(player.rect)
    keyEventsManager(pressedKeys)
    drawAll()

def keyEventsManager(events):
    toDo = {"up":player.up, "down":player.down, "left":player.left, "right":player.right}
    dico=manager.getKeys()
    for key, active in pressedKeys.items():
        if not active: continue
        if key in dico.keys(): toDo[dico[key]]()
    return

def drawAll():
    #Background (tiles)
    screen.fill((255,255,255))
    #Player
    screen.blit(player.image, player.selfCoos(screen.get_size()))
    #Mobs
    a=(screen.get_size()[0]//2-player.rect.x, screen.get_size()[1]//2-player.rect.y)
    for sprite in hostileMobs:
        screen.blit(sprite.image, sprite.selfCoos(a))
        pygame.draw.circle(screen, (255,0,0), sprite.centerCoos, sprite.detectRange, 2)
    #Items
    if player.activeItem : 
        b=(player.selfCoos(screen.get_size())[0]+player.rect[2], player.selfCoos(screen.get_size())[1]+player.rect[3]//2)
        """temp=pygame.mouse.get_pos()
        deltaCoos = (temp[0]-a[0],temp[1]/a[1])
        l=m.atan(deltaCoos[0]/deltaCoos[1])
        tangente = m.sqrt(deltaCoos[0]**2+deltaCoos[1]**2)
        b=(m.sin(180-90-l)*tangente, m.sin(l)*tangente)"""
        screen.blit(player.activeItem.image, b)
    #GUI
    c=player.selfCoos(screen.get_size())
    pygame.draw.rect(screen, (0,0,0), (c[0], c[1]+player.rect[3]+3, player.rect[2], 5))
    pygame.draw.rect(screen, (255,0,0), (c[0]+1, c[1]+player.rect[3]+4, (player.rect[2]-2)*(player.pv/player.maxPv), 3))
    
    return

doContinue = True
while doContinue:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            doContinue = False
        if event.type == KEYDOWN:
            pressedKeys[event.dict["scancode"]] = True
        if event.type == KEYUP:
            pressedKeys[event.dict["scancode"]] = False
            if event.key == K_i:
                player.addToInventory(gameItems.weapons["sword"])
                player.pv -= 1

    update()
    pygame.display.flip()

pygame.quit()