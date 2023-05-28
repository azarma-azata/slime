import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.inv = pygame.sprite.Group()
        self.currentItem = None
        self.isOpen = False

    def update(self, screen):
        if self.isOpen: self.drawSelf(screen)

    def drawSelf(self, screen):
        a=screen.get_size()
        b=(a[0]//2-32*5-3*6, a[1]//2-32*2-3*3)
        pygame.draw.rect(screen, (127,127,127), b+(64*5+3*6, 64*2+3*3))
        for n in range(2):
            for k in range(5):
                pygame.draw.rect(screen, (0,0,0), (b[0]+68*k+3,b[1]+68*n+3,64,64), 5)

    def openInv(self):
        self.isOpen = not self.isOpen

    def addItem(self, item):
        self.inv.add(item)
    
    def changeCurrentItem(self, item, destination):
        if self.currentItem != None: destination.add(self.currentItem)
        self.currentItem = item
        self.inv.remove(item)
          
    def deleteItem(self, item): self.inv.remove(item)
    