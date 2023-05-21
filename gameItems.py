import pygame

class weapon(pygame.sprite.Sprite):
    def __init__(self, name, atk, atkRange, price, imgPath, weight, cooldown):
        super().__init__()

        self.name = name
        self.damage = atk
        self.atkRange = atkRange
        self.cost = price
        self.image = pygame.image.load("data/items/"+imgPath)
        self.initialImage = self.image
        self.rect = self.image.get_rect()
        self.weight = weight
        self.cooldown = cooldown

        self.isAttacking = False
        self.isRecharging = False
        self.currentPos = 0
        self.currentCooldown = 0

    def update(self):
        if self.isAttacking:
            self.currentPos+=1
            self.image = pygame.transform.rotate(self.initialImage, -20*self.currentPos)
        
        if self.currentPos == 10:
            self.currentPos = 0
            self.isAttacking = False
            self.isRecharging = True

        if self.isRecharging:
            self.currentCooldown +=1
            if self.currentCooldown<=10: self.image = pygame.transform.rotate(self.initialImage, -10*(10-self.currentCooldown))
        
        if self.currentCooldown == self.cooldown:
            self.isRecharging = False
            self.currentCooldown = 0
    
    def attack(self):
        self.isAttacking = True


weapons = {
    "dague" : weapon("Dague", 1,38,1,"dague.png", 2, 60),
    "sword" : weapon("Basic sword",2, 43, 3, "sword.png", 4, 85),
    "long-sword" : weapon("Basic long sword",4, 53, 5, "long-sword.png", 7, 100)
}