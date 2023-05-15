import pygame
import manager

texts = manager.getTexts()

class pauseMenu():
    def __init__(self, screenSize):
        #self.creditsMenu = fcredits()
        self.activeMenu = None
        
        #settings
        self.gameLanguage = "fr"
        
        self.buttonsRect = [pygame.Rect(screenSize[0]//2-150, screenSize[1]//2+((k-2)*60)-15, 300, 30) for k in range(5)]
        self.text = tuple(texts[self.gameLanguage][0:6])
        self.buttons = [Button(self.text[k], (180,180,180), self.buttonsRect[k], k) for k in range(5)]
        
        self.idToReturn = None
    
    def update(self, screen, police):
        s=pygame.Surface(screen.get_size())
        s.set_alpha(100)
        s.fill((0,0,0))
        screen.blit(s, (0,0))
        
        for k in self.buttons:
            if k.update(screen, police):
                return k.update(screen, police)
        
        
        """for k in range(len(self.buttons)):
            pygame.draw.rect(screen, (180,180,180), self.buttons[k])
            pygame.draw.rect(screen, (0,0,0), self.buttons[k], 2)
            texte = police.render(self.text[k], 0, (0,0,0))
            screen.blit(texte, (self.buttons[k].midtop[0]-texte.get_size()[0]//2, self.buttons[k].midtop[1]+15-texte.get_size()[1]//2))
        
        screen.blit(screen, (0,0))"""

    def gettingClicked(self, coos):
        for k in self.buttons:
            if k.rect.collidepoint(coos):
                return(k.gotClicked())
    
    
    class videoSettingsMenu():
        def __init__(self):
            pass

    class creditsMenu():
        def __init__(self):
            pass

    class languageMenu():
        def __init__(self):
            pass

class Button():
    def __init__(self, text, color, rect, id):
        self.id = id
        self.text = text
        self.color = color
        self.originalColor = self.color
        self.rect = rect
        self.returnBack = 0
        self.maxReturnBack = 5
    
    def update(self, screen, police):
        if self.returnBack!=0 and self.returnBack != self.maxReturnBack: self.returnBack += 1
        elif self.returnBack == self.maxReturnBack:
            self.returnBack = 0
            self.color = self.originalColor
            return self.id
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)
        texte = police.render(self.text, 0, (0,0,0))
        screen.blit(texte, (self.rect.midtop[0]-texte.get_size()[0]//2, self.rect.midtop[1]+15-texte.get_size()[1]//2))
    
    def gotClicked(self):
        print(self.text, self.id)
        self.color = (255,255,255)
        self.returnBack = 1