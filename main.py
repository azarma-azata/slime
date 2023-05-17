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

group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
group.add(player)
group.add(hostileMobs)

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
    return group2

def barre_vie(x,y):
    icon = pygame.image.load("data/images/player.png")
    pygame.draw.rect(screen,(0,0,0),[x-55,y-7,116,20])
    pygame.draw.rect(screen,(200,0,0),[x-25,y-5,84*(player.pv/player.maxPv),16])
    pygame.draw.polygon(screen,(0,0,0),((x+60,y-5),(x+60,y+10) ,(x+35,y+10), (x+55,y-5)))
    pygame.draw.circle(screen,(0,0,0),(x-55,y+5),30)
    screen.blit(icon, (x-70,y-10))

    #a = police.render(username, 0, (255,255,255))
    #screen.blit(a, (x-25, y+15))

def update():
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
    barre_vie(100,50)
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
            pressedKeys[event.dict["key"]] = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                if not gamePaused: gamePaused = True
                #elif gameMenu.activeMenu == None: gamePaused = False
            
            #pressedKeys[event.dict["scancode"]] = False
            del pressedKeys[event.dict["key"]]
            if event.key == K_i:
                player.inv.changeCurrentItem(gameItems.weapons["long-sword"], player.inv.inv)
                group.add(player.inv.currentItem)
                group.add(hostileMobs.weapon)
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