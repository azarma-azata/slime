import pygame
from pygame.locals import *
import math as m
import pytmx, pyscroll

import manager, mobs, gameItems, menu
from player import Player

buttonActions = []
username = "Slime"
gamePaused = False
pressedKeys = {}

pygame.init()
gameClock = pygame.time.Clock()
screen = pygame.display.set_mode((800,450), RESIZABLE)
pygame.display.set_caption('Slime')
pygame.display.set_icon(pygame.image.load("data/images/player.png"))

police = pygame.font.Font("data/fonts/alagard.ttf", 20)

player = Player()
hostileMobs = mobs.Fighter
#hostileMobs = pygame.sprite.Group()
#hostileMobs.add(mobs.Fighter)
gameMenu = menu.pauseMenu(screen.get_size())

tmx_data = pytmx.util_pygame.load_pygame("data/tilemaps/carte.tmx")
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())

group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)
group.add(player)
group.add(hostileMobs)
group.add(hostileMobs.weapon)
group.add(player.inv.currentItem)

spawnPoint = tmx_data.get_object_by_name("spawnPoint")
player.rect.x = spawnPoint.x
player.rect.y = spawnPoint.y

fighter_spawnPoint = tmx_data.get_object_by_name("fighter_spawnPoint")
hostileMobs.rect.x = fighter_spawnPoint.x
hostileMobs.rect.y = fighter_spawnPoint.y

collisions = []
for obj in tmx_data.get_layer_by_name("Collisions"):
    collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

def groupReset():
    group2 = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
    for k in group:
        group2.add(k)
    map_layer.zoom = screen.get_width()/800
    return group2

def barre_vie(x,y):

    a=8

    pygame.draw.rect(screen, (0,0,0), (x-11, y-11, 93, 23))
    pygame.draw.rect(screen, (255,0,0), (x+2, y-a, 76*(player.pv/player.maxPv), 2*a))
    pygame.draw.polygon(screen, (215,200,140), ((x,y), (x,y+10), (x+80, y+10), (x+80,y-10), (x, y-10), (x,y), (x+2, y), (x+2, y-a), (x+80-2, y-a), (x+80-2*a, y+a), (x+2, y+a), (x+2, y)))
    pygame.draw.circle(screen, (0,0,0),(x-30, y),30)
    screen.blit(player.image, (x-45,y-15))

    pygame.draw.circle(screen, (255,255,0), (x,y), 1)

    """icon = pygame.image.load("data/images/player.png")
    pygame.draw.rect(screen,(0,0,0),[x-55,y-7,116,20])
    pygame.draw.rect(screen,(200,0,0),[x-25,y-5,84*(player.pv/player.maxPv),16])
    pygame.draw.polygon(screen,(0,0,0),((x+60,y-5),(x+60,y+10) ,(x+35,y+10), (x+55,y-5)))
    pygame.draw.circle(screen,(0,0,0),(x-55,y+5),30)
    screen.blit(icon, (x-70,y-10))"""

    #a = police.render(username, 0, (255,255,255))
    #screen.blit(a, (x-25, y+15))

def update():
    a=hostileMobs.update(collisions, player.rect)
    if a: player.pv-=a
    player.update(collisions, hostileMobs)
    player.inv.update(player.rect)
    keyEventsManager(pressedKeys)

def keyEventsManager(events):
    toDo = {"up":player.up, "down":player.down, "left":player.left, "right":player.right}
    dico=manager.getKeys()
    for key, active in pressedKeys.items():
        if not active: continue
        if key in dico.keys(): toDo[dico[key]]()
    return

def drawAll():
    barre_vie(80,50)
    pass

def fpausedMenu(menuId):
    global gamePaused
    if menuId == 5: gamePaused = False

doContinue = True
while doContinue:
    gameClock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            doContinue = False
        if event.type == VIDEORESIZE:
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
            group = groupReset()
            gameMenu = menu.pauseMenu(screen.get_size())
        
        if event.type == KEYDOWN:
            pressedKeys[event.dict["scancode"]] = True
        if event.type == KEYUP:
            del pressedKeys[event.dict["scancode"]]
            
            if event.key == K_ESCAPE:
                if not gamePaused: gamePaused = True
            if event.key == K_i:
                player.pv -= 1
        
        if event.type == MOUSEBUTTONUP:
            if gamePaused:
                gameMenu.gettingClicked(pygame.mouse.get_pos())
    
    if not gamePaused: update()

    group.center(player.rect)
    group.draw(screen)
    drawAll()
    if gamePaused:
        #print(gameMenu.update(screen, police))
        a=gameMenu.update(screen, police)
        if a: fpausedMenu(a)
    pygame.display.flip()

pygame.quit()