import pygame
import math as m

import gameItems

class hostileMob(pygame.sprite.Sprite):
    def __init__(self, atk, pvs, speed, imgPath, weapon, detectRange, deathWorth):
        super().__init__()

        self.atk = atk
        self.pv = pvs
        self.speed = speed
        self.image = pygame.image.load(imgPath)
        self.rect = self.image.get_rect()
        self.weapon = weapon
        self.detectRange = detectRange
        self.deathWorth = deathWorth
        self.spawnPoint = (0,0)
        self.playerDistance = int
        #self.relativeCoos, self.centerCoos = (0,0), (0,0)
        self.tag = "hostileMob"
        self.isReversed = True
        self.target = pygame.Rect(0,0,0,0)
        self.isDead = False
        
        self.weapon.reverse()

    def update(self, collisions, player):
        print(self.pv)

        if self.pv<=0:
            self.died()
        if self.isDead: return

        self.updateWeapon()

        self.playerDistance = self.detection(player.rect)
        self.collisions = collisions

        #l=m.sqrt(abs((self.rect.center[0]-self.spawnPoint[0])**2)+abs((self.rect.center[1]-self.spawnPoint[1])**2))
        
        b=self.isReversed
        if self.playerDistance and self.playerDistance < self.detectRange:
            self.target = player
            if self.rect.x-player.rect.x > 0: self.isReversed = True
            elif self.rect.x-player.rect.x < 0: self.isReversed = False
            self.move(player.rect)
        elif self.rect[:2] != self.spawnPoint:
            self.move(self.spawnPoint)

        if b!= self.isReversed: self.reverse()
    
    def updateWeapon(self):
        if not self.isReversed: a=+12
        else: a=-30
        
        c = self.rect.x + self.rect.width//2+a
        d = self.rect.y + self.rect.height-self.weapon.rect.width-(self.weapon.rect.height//2)
        
        b=pygame.Rect(c,d,0,0)
        
        self.weapon.update(b)
    
    def reverse(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.weapon.reverse()
        
    
    def attack(self):
        if (self.weapon.isRecharging or self.weapon.isAttacking): return
        self.weapon.attack()
        self.target.pv-=self.weapon.damage

    def move(self, destination):
        if self.target:
            if self.weapon.rect.colliderect(self.target.rect): 
                self.attack()
                return
        
        if abs(self.rect.x-destination[0]) > self.speed:
            if self.rect.x-destination[0] > 0: self.left()
            else: self.right()
        
        if abs(self.rect.y-destination[1]) > self.speed:
            if self.rect.y-destination[1] > 0: self.up()
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

    def setSpawnPoint(self, spawnPoint):
        self.spawnPoint = spawnPoint
        self.rect.x = self.spawnPoint[0]
        self.rect.y = self.spawnPoint[1]

    def died(self):
        self.isDead = True
        self.target.inv.currentMoney += self.deathWorth


Fighter = hostileMob(1,10,1.5,"data/images/deep_elf_fighter_new.png",gameItems.weapons["sword"],200, 10)