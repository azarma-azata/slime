import pygame
import math as m

import gameItems

class hostileMob(pygame.sprite.Sprite):
    def __init__(self, atk, pvs, imgPath, weapon, detectRange):
        super().__init__()

        self.atk = atk
        self.pv = pvs
        self.image = pygame.image.load(imgPath)
        self.rect = self.image.get_rect()
        self.weapon = weapon
        self.detectRange = detectRange
        self.isPlayerFounded = False
        self.relativeCoos, self.centerCoos = (0,0), (0,0)

    def update(self, playerCoos):
        #self.detection(playerCoos)
        self.weapon.rect.x = self.rect.x + self.rect.width
        self.weapon.rect.y = self.rect.y + self.rect.height-10
        return self.rect

    def detection(self, playerCoos):
        if self.rect.x+self.detectRange > playerCoos[0] and self.rect.x-self.detectRange < playerCoos[0]:
            a = m.sqrt(self.detectRange**2-(playerCoos[0]**2))
            if abs(playerCoos[1])<a:
                self.isPlayerFounded = True
            else:
                self.isPlayerFounded = False

Fighter = hostileMob(1,10,"data/deep_elf_fighter_new.png",gameItems.weapons["sword"],150)