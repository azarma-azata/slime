import pygame

class weapon(pygame.sprite.Sprite):
    def __init__(self, name, description, atk, atkRange, price, imgPath, weight, cooldown):
        super().__init__()

        self.name = name
        self.description = description
        self.damage = atk
        self.atkRange = atkRange
        self.cost = price
        self.image = pygame.image.load("data/items/"+imgPath)
        self.initialImage = self.image
        self.rect = self.image.get_rect()
        self.weight = weight
        self.cooldown = cooldown
        self.isReversed = False

        self.isAttacking = False
        self.isRecharging = False
        self.currentPos = 0
        self.currentCooldown = 0

    def update(self, newRect, rotation=0):
        
        self.rect.x = newRect.x
        self.rect.y = newRect.y
        
        self.initialImage2 = self.initialImage
        self.image = pygame.transform.rotate(self.initialImage, rotation)

        if self.isAttacking:
            self.currentPos+=1
            if not self.isReversed: self.image = pygame.transform.rotate(self.initialImage, -20*self.currentPos)
            else: self.image = pygame.transform.rotate(self.initialImage, 20*self.currentPos)
        
        if self.currentPos == 10:
            self.currentPos = 0
            self.isAttacking = False
            self.isRecharging = True

        if self.isRecharging:
            self.currentCooldown +=1
            if self.currentCooldown<=10:
                if not self.isReversed: self.image = pygame.transform.rotate(self.initialImage, -10*(10-self.currentCooldown))
                else: self.image = pygame.transform.rotate(self.initialImage, 10*(10-self.currentCooldown))
        
        if self.currentCooldown == self.cooldown:
            self.isRecharging = False
            self.currentCooldown = 0
    
    def attack(self):
        self.isAttacking = True

    def reverse(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.initialImage = self.image
        self.isReversed = not self.isReversed
    
    
weapons = {
    "dague" : weapon("Dague", "", 1,38,1,"dague.png", 2, 60),
    "sword" : weapon("Basic sword", "", 2, 43, 3, "sword.png", 4, 85),
    "long-sword" : weapon("Basic long sword", "", 4, 53, 5, "long-sword.png", 7, 100),
    "40m-sword" : weapon("Bruh", "", 19, 530, 999, "40m-sword.png", 100, 300)
}