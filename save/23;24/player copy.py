import pygame
import math as m

import gameItems
from inventory import Inventory

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("data/images/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.maxPv = 20
        self.pv = self.maxPv
        self.speed = 3
        self.detectRange=300
        self.isDead = False
        self.target = None
        self.inv = Inventory()
        self.inv.changeCurrentItem(gameItems.weapons["long-sword"], self.inv.inv)
        self.i = 0
    
    def update(self, collisions, hostileMobs, screen):
        self.collisions = collisions
        self.feet = pygame.Rect(self.rect.midbottom+(0,0))
        #if self.pv <= 0: self.isDead = True
        if self.isDead: self.died(screen)
        
        a=m.sqrt(abs((self.rect.center[0]-hostileMobs.rect.center[0])**2)+abs((self.rect.center[1]-hostileMobs.rect.center[1])**2))
        if a<self.detectRange:
            self.target = hostileMobs
        self.updateWeapon()
    
    def updateWeapon(self):
        a=0
        if self.target:
            if self.rect.center[0]-self.target.rect.center[0] != 0: 
                a=m.atan((self.target.rect.center[1]-self.rect.center[1])/(self.rect.center[0]-self.target.rect.center[0]))
                if a<=0: a=m.pi+a
                if (self.target.rect.center[1]-self.rect.center[1])<0: a=m.pi+a
        
        a=m.pi-a

        if a==0: 
            if (self.rect.center[0]-self.target.rect.center[0])>0:
                if self.inv.currentItem.isReversed == False: self.inv.currentItem.reverse()
            elif self.inv.currentItem.isReversed == True: self.inv.currentItem.reverse()
        elif self.inv.currentItem.isReversed == True:
            self.inv.currentItem.reverse()

        print(a*(180/m.pi))
        b=self.rect.copy()

        b.x+=(b.width)*m.cos(a)
        b.y+=(b.height-10)*m.sin(a)

        self.inv.currentItem.update(b, -a*(180/m.pi))
        #self.inv.currentItem.update(b, a)
        pass

    def up(self):
        if pygame.Rect(self.rect.x, self.rect.y-self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y-=self.speed
    def down(self):
        if pygame.Rect(self.rect.x, self.rect.y+self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y+=self.speed
    def left(self):
        if pygame.Rect(self.rect.x-self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x-=self.speed
    def right(self):
        if pygame.Rect(self.rect.x+self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x+=self.speed
    
    def selfCoos(self, screenSize): return (screenSize[0]//2-(self.rect[2]//2), screenSize[1]//2-(self.rect[3]//2))
    
    def died(self, screen):
        screen.fill((0,0,0))
        a=pygame.image.load("data/images/uDied.png")
        b=((screen.get_size()[0]//2-a.get_size()[0]//2), (screen.get_size()[1]//2-a.get_size()[1]//2))
        screen2 = pygame.Surface(screen.get_size())
        screen2.set_alpha(255*(self.i/150))
        screen2.blit(a, b)
        screen.blit(screen2, (0,0))
        if self.i <= 150: self.i += 1