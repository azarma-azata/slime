import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.inv = pygame.sprite.Group()
        self.currentMoney = 0
        self.currentItem = None
        self.isOpen = False
        self.selectedItem = None
        self.case = 78
        self.interCase = self.case//8

        self.dropped = pygame.sprite.Group()
        self.changed = False

    def update(self, screen):
        self.fcases(screen)
        if self.isOpen: self.drawSelf(screen)

    def gettingClicked(self, screen, playerRect):
        mousePos=pygame.mouse.get_pos()
        a=pygame.Rect(mousePos+(1,1))
        c=a.collidelist(self.cases)
        if c >-1:
            c+=1
            if not self.selectedItem:
                for i in self.inv: 
                    if i.invNumber == c: self.selectedItem = i
                    self.inv.remove(i)
            else:
                self.selectedItem.invNumber = c
                self.inv.add(self.selectedItem)
                self.selectedItem = None
        elif self.selectedItem:
            self.selectedItem.invNumber = None
            self.selectedItem.rect.bottomright = playerRect.bottomleft
            self.dropped.add(self.selectedItem)
            self.changed = True
            self.selectedItem = None

    def drawSelf(self, screen):
        mousePos=pygame.mouse.get_pos()

        a=screen.get_size()
        b=((a[0]-self.case*5-self.interCase*6)//2, (a[1]-self.case*2-self.interCase*3)//2)
        pygame.draw.rect(screen, (127,127,127), b+(self.case*5+self.interCase*6, self.case*2+self.interCase*3))
        for n in range(2):
            for k in range(5):
                pygame.draw.rect(screen, (0,0,0), self.cases[k+n*5], 3)
                for i in self.inv:
                    if i.invNumber == k+1+n*5:
                        temp = pygame.transform.scale(i.image, (64,64))
                        screen.blit(temp, [m+7 for m in self.cases[k+n*5]])
        
        if self.selectedItem:
            temp = pygame.transform.scale(self.selectedItem.image, (64,64))
            screen.blit(temp, mousePos)

    def pickUp(self):
        a=pygame.mouse.get_pos()
        for k in self.dropped:
            if k.rect.collidepoint(a):
                self.isOpen = True
                self.dropped.remove(k)
                self.selectedItem = k
                self.changed = True

    def fcases(self, screen):
        a=screen.get_size()
        b=((a[0]-self.case*5-self.interCase*6)//2, (a[1]-self.case*2-self.interCase*3)//2)

        self.cases = []
        for n in range(2):
            for k in range(5):
                l=(b[0]+self.case*k+self.interCase*(k+1), b[1]+self.case*n+self.interCase*(n+1))
                self.cases.append(pygame.Rect(l, tuple([self.case]*2)))

    def openInv(self):
        self.isOpen = not self.isOpen

    def addItem(self, item, place):
        a=item
        a.invNumber = place
        self.inv.add(a)
    
    def changeCurrentItem(self, item, destination):
        if self.currentItem != None: destination.add(self.currentItem)
        self.currentItem = item
        self.inv.remove(item)
          
    def deleteItem(self, item): self.inv.remove(item)
    