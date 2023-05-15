import pygame

class weapon(pygame.sprite.Sprite):
    def __init__(self, name, atk, atkRange, price, imgPath, weight):
        super().__init__()

        self.name = name
        self.damage = atk
        self.atkRange = atkRange
        self.cost = price
        self.image = pygame.image.load("data/items/"+imgPath)
        self.rect = self.image.get_rect()
        self.weight = weight


weapons = {
    "sword" : weapon("rusty sword", 2,10,1,"sword.png", 4),
    "long-sword" : weapon("Basic long sword",5, 25, 6, "long-sword.png", 5)
}