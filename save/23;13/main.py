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
pressedKeys2 = {}

pygame.init()
sounds = {"oof":pygame.mixer.Sound("data/sounds/oof.wav")}
for key in sounds.keys(): sounds[key].set_volume(0.001)
pygame.mixer.init()
gameClock = pygame.time.Clock()
#screen = pygame.display.set_mode((800,450), RESIZABLE)
screen = pygame.display.set_mode((1080,720), RESIZABLE)
pygame.display.set_caption('Slime')
pygame.display.set_icon(pygame.image.load("data/images/player.png"))

music = {"rush E": pygame.mixer.Sound("data/sounds/rush_E.wav"), "bombjack": pygame.mixer.Sound("data/sounds/bombjack.wav")}
musicChannel = pygame.mixer.Channel(1)
musicChannel.set_volume(0.001)
musicChannel.play(music["bombjack"])

police = pygame.font.Font("data/fonts/alagard.ttf", 20)

player = Player()
hostileMobs = mobs.Fighter
#hostileMobs = pygame.sprite.Group()
#hostileMobs.add(mobs.Fighter)
gameMenu = menu.pauseMenu(screen.get_size())

tmx_data = pytmx.util_pygame.load_pygame("data/tilemaps/carte.tmx")
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
map_layer.zoom = screen.get_width()/800

group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)
group.add(player)
group.add(hostileMobs)
group.add(hostileMobs.weapon)
group.add(player.inv.currentItem)

spawnPoint = tmx_data.get_object_by_name("spawnPoint")
player.rect.x = spawnPoint.x
player.rect.y = spawnPoint.y

fighter_spawnPoint = tmx_data.get_object_by_name("fighter_spawnPoint")
hostileMobs.setSpawnPoint((fighter_spawnPoint.x, fighter_spawnPoint.y))

collisions = []
for obj in tmx_data.get_layer_by_name("Collisions"):
    collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

def update():
    hostileMobs.update(collisions, player)
    #for k in hostileMobs:
    #    if k.isDead: hostileMobs.remove(k)
    player.update(collisions, hostileMobs, screen)
    keyEventsManager(pressedKeys)

def groupReset():
    group2 = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
    for k in group:
        group2.add(k)
    a = screen.get_width()/800
    b = screen.get_height()/400
    if a<b: map_layer.zoom = a
    else: map_layer.zoom = b

    return group2

def healthBar(x,y):
    a=8
    pygame.draw.rect(screen, (0,0,0), (x-11, y-11, 93, 23))
    pygame.draw.rect(screen, (255,0,0), (x+2, y-a, 76*(player.pv/player.maxPv), 2*a))
    pygame.draw.polygon(screen, (215,200,140), ((x,y), (x,y+10), (x+80, y+10), (x+80,y-10), (x, y-10), (x,y), (x+2, y), (x+2, y-a), (x+80-2, y-a), (x+80-2*a, y+a), (x+2, y+a), (x+2, y)))
    pygame.draw.circle(screen, (0,0,0),(x-30, y),30)
    screen.blit(player.image, (x-45,y-15))

def keyEventsManager(events):
    global pressedKeys2
    toDo = {"up":player.up, "down":player.down, "left":player.left, "right":player.right, "inventory":player.inv.openInv, "pickUp":player.inv.pickUp}
    dico=manager.getKeys()
    for key, active in pressedKeys.items():
        #if not active: continued 
        a=False
        for k,n in dico.items():
            if n[1]==key: a=k
        if not a: continue
        if dico[a][0]==1 or (dico[a][0]==0 and (not key in pressedKeys2.keys())):
            #if (player.inv.status == "waiting" and player.inv.activeMenu == 3): player.inv.keySettings.changeKey(key)
            #else: 
            toDo[a]()
    pressedKeys2 = pressedKeys.copy()

    return

def drawAll():
    screen.fill((255,255,255))
    group.center(player.rect)
    group.draw(screen)
    healthBar(80,50)
    #pygame.draw.line(screen, (255,0,0), player.rect.center, player.target.rect.center)
    player.inv.update(screen)
    if player.inv.changed:
        group.add(player.inv.dropped)
        player.inv.changed = False
        print("changed")
    
    #print([(a,a.groups()) for a in player.inv.inv], [a for a in player.inv.dropped], player.inv.selectedItem)

def fpausedMenu(menuId):
    global gamePaused
    if menuId == 5: 
        gamePaused = False
        m=gameMenu.activeMenu = None
        gameMenu.i = 0
    else: 
        gameMenu.activeMenu = gameMenu.menus[menuId]

groupReset()
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
        
        #print(event)
        if event.type == KEYDOWN:
            pressedKeys[event.dict["key"]] = True
        if event.type == KEYUP:
            #print(event.dict)
            
            del pressedKeys[event.dict["key"]]
            
            if event.scancode == 41:
                if not gamePaused: gamePaused = True
            if event.key == K_i:
                player.pv -= 5
                player.inv.addItem(gameItems.weapons["fire-wand"], 1)
            if event.key == K_j:
                player.inv.addItem(gameItems.weapons["fire-wand"], 2)
        
        if event.type == MOUSEBUTTONUP:
            if gamePaused:
                gameMenu.gettingClicked()
            if player.inv.isOpen:
                player.inv.gettingClicked(screen, player.rect)
    
    if not gamePaused: update()

    if not player.isDead: drawAll()
    if gamePaused:
        a=gameMenu.update(screen, police)
        if a: fpausedMenu(a)
    pygame.display.flip()


pygame.quit()