import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.inv = pygame.sprite.Group()
        self.currentItem = None
        self.maxWeight = 40
        self.currentWeight = 0

    def update(self, playerRect):
        if self.currentItem:
            self.currentItem.rect.x = playerRect.x + playerRect.width
            self.currentItem.rect.y = playerRect.y + playerRect.height-10

    def addItem(self, item):
        if self.currentWeight+item.weight > self.maxWeight : print("Poids dépassé")
        self.currentWeight += item.weight
        self.inv.add(item)
    
    def changeCurrentItem(self, item, destination):
        if self.currentItem != None: destination.add(self.currentItem)
        self.currentItem = item
        self.inv.remove(item)
          
    def deleteItem(self, item): self.inv.remove(item)
    