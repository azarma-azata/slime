import pygame
import math as m

import gameItems

class hostileMob(pygame.sprite.Sprite):
    def __init__(self, atk, pvs, speed, imgPath, weapon, detectRange):
        super().__init__()

        self.atk = atk
        self.pv = pvs
        self.speed = speed
        self.image = pygame.image.load(imgPath)
        self.rect = self.image.get_rect()
        self.weapon = weapon
        self.detectRange = detectRange
        self.playerDistance = int
        #self.relativeCoos, self.centerCoos = (0,0), (0,0)
        self.tag = "hostileMob"

    def update(self, collisions, playerRect):
        self.weapon.update()

        self.playerDistance = self.detection(playerRect)
        self.collisions = collisions

        self.weapon.rect.x = self.rect.x + self.rect.width
        self.weapon.rect.y = self.rect.y + self.rect.height-10

        a=0
        if self.playerDistance and self.playerDistance < self.detectRange:
            a=self.move(playerRect)
        
        return a

    def attack(self):
        if (self.weapon.isRecharging or self.weapon.isAttacking): return
        self.weapon.attack()
        return self.weapon.damage

    def move(self, playerRect):
        if self.weapon.rect.colliderect(playerRect): 
            return self.attack()

        if self.rect.x-playerRect.x > 0: self.left()
        else: self.right()

        if self.rect.y-playerRect.y > 0: self.up()
        else: self.down()

        return 0

    def up(self):
        if pygame.Rect(self.rect.x, self.rect.y-self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y-=self.speed
    def down(self):
        if pygame.Rect(self.rect.x, self.rect.y+self.speed, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.y+=self.speed
    def left(self):
        if pygame.Rect(self.rect.x-self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x-=self.speed
    def right(self):
        if pygame.Rect(self.rect.x+self.speed, self.rect.y, self.rect.width, self.rect.height).collidelist(self.collisions) ==-1: self.rect.x+=self.speed
    

    def detection(self, playerRect):
        if playerRect.x > self.rect.x-self.detectRange and playerRect.x < self.rect.x+self.detectRange:
            a=m.sqrt(abs((self.rect.center[0]-playerRect.center[0])**2)+abs((self.rect.center[1]-playerRect.center[1])**2))
            return a

Fighter = hostileMob(1,10,1.5,"data/images/deep_elf_fighter_new.png",gameItems.weapons["sword"],150)