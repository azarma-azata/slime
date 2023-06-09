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
        self.inv = Inventory()
        self.inv.changeCurrentItem(gameItems.weapons["long-sword"], self.inv.inv)
    
    def update(self, collisions, hostileMobs):
        self.collisions = collisions
        self.feet = pygame.Rect(self.rect.midbottom+(0,0))
        if self.pv == 0:
            self.died()
        """if self.inv.currentItem:
        #for k in hostileMobs:
            a=m.sqrt((self.rect.center[0]-hostileMobs.rect.center[0])**2 + (self.rect.center[1]-hostileMobs.rect.center[1])**2)
            print(a)
            if a<self.inv.currentItem.atkRange:
                print("detekted")
            else:
                print("not detekted")"""
                
        

    def up(self):
        if pygame.Rect(self.rect.x, self.rect.y-self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y-=self.speed
    def down(self):
        if pygame.Rect(self.rect.x, self.rect.y+self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y+=self.speed
    def left(self):
        if pygame.Rect(self.rect.x-self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x-=self.speed
    def right(self):
        if pygame.Rect(self.rect.x+self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x+=self.speed
    
    def selfCoos(self, screenSize): return (screenSize[0]//2-(self.rect[2]//2), screenSize[1]//2-(self.rect[3]//2))
    
    def died(self):
        print("U DIED (NOOB)")