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
    "dague" : weapon("Dague", 1,38,1,"dague.png", 2),
    "sword" : weapon("Basic sword",2, 43, 3, "sword.png", 4),
    "long-sword" : weapon("Basic long sword",4, 50, 5, "long-sword.png", 7)
}