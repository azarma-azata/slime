import pygame
import math as m

class hostileMob(pygame.sprite.Sprite):
    def __init__(self, atk, pvs, imgPath, atkRange, detectRange):
        super().__init__()

        self.atk = atk
        self.pv = pvs
        self.image = pygame.image.load(imgPath)
        self.rect = self.image.get_rect()
        self.atkRange = atkRange
        self.detectRange = detectRange
        self.isPlayerFounded = False
        self.relativeCoos, self.centerCoos = (0,0), (0,0)

    def update(self, playerCoos):
        a=self.relativeCoos
        self.centerCoos = (a[0]+(self.rect[2]//2), a[1]+(self.rect[3]//2))
        self.detection(playerCoos)

    def selfCoos(self, a): 
        self.relativeCoos = (a[0]-(self.rect[2]//2), a[1]-(self.rect[3]//2))
        return self.relativeCoos

    def detection(self, playerCoos):
        if self.rect.x+self.detectRange > playerCoos[0] and self.rect.x-self.detectRange < playerCoos[0]:
            a = m.sqrt(self.detectRange**2-(playerCoos[0]**2))
            if abs(playerCoos[1])<a:
                self.isPlayerFounded = True
            else:
                self.isPlayerFounded = False

Fighter = hostileMob(1,10,"data/assets\Dungeon Crawl Stone Soup Full\monster\deep_elf_fighter_new.png",100,150)