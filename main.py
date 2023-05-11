import pygame
from pygame.locals import *
import math as m
import pytmx, pyscroll

import manager, mobs, gameItems
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
pygame.display.set_caption('Slime')
pygame.display.set_icon(pygame.image.load("data/player.png"))

player = Player()
hostileMobs = pygame.sprite.Group()
hostileMobs.add(mobs.Fighter)

tmx_data = pytmx.util_pygame.load_pygame("test data/carte.tmx")
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())

spawnPoint = tmx_data.get_object_by_name("spawnPoint")
player.rect.x = spawnPoint.x
player.rect.y = spawnPoint.y

walls = []
for obj in tmx_data.get_layer_by_name("Collisions"):
    walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

def groupReset():
    group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
    group.add(player)
    group.add(hostileMobs)
    return group

def barre_vie(x,y):
    icon = pygame.image.load("data/player.png")
    pygame.draw.rect(screen,(0,0,0),[x-55,y-7,116,20])
    pygame.draw.rect(screen,(200,0,0),[x-25,y-5,player.pv*4.2,16])
    pygame.draw.polygon(screen,(0,0,0),((x+60,y-5),(x+60,y+10) ,(x+35,y+10), (x+55,y-5)))
    pygame.draw.circle(screen,(0,0,0),(x-55,y+5),30)
    screen.blit(icon, (x-70,y-10))

def update():
    player.update(walls)
    player.inv.update(player.rect)
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
    #barre_vie(100,50)
    pass

group = groupReset()

doContinue = True
while doContinue:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            doContinue = False
        if event.type == VIDEORESIZE:
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
            group = groupReset()
        
        if event.type == KEYDOWN:
            pressedKeys[event.dict["scancode"]] = True
        if event.type == KEYUP:
            pressedKeys[event.dict["scancode"]] = False
            if event.key == K_i:
                player.inv.changeCurrentItem(gameItems.weapons["long-sword"], player.inv.inv)
                group.add(player.inv.currentItem)
                player.pv -= 1
    
    update()

    group.center(player.rect)
    group.draw(screen)
    pygame.display.flip()

pygame.quit()