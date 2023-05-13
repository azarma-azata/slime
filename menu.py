import pygame
import manager

texts = manager.getTexts()

class mainMenu():
    def __init__(self):
        pass

class pauseMenu():
    def __init__(self, screenSize):
        #self.creditsMenu = fcredits()

        #settings
        self.gameLanguage = "fr"

        self.buttons = [pygame.Rect(screenSize[0]//2-150, screenSize[1]//2+((k-2)*60)-15, 300, 30) for k in range(5)]
        self.text = tuple(texts[self.gameLanguage][0:6])
        print(self.text)
    
    def update(self, screen, police):
        s=pygame.Surface(screen.get_size())
        s.set_alpha(100)
        s.fill((0,0,0))
        screen.blit(s, (0,0))

        for k in range(len(self.buttons)):
            pygame.draw.rect(screen, (180,180,180), self.buttons[k])
            pygame.draw.rect(screen, (0,0,0), self.buttons[k], 2)
            texte = police.render(self.text[k], 0, (0,0,0))
            screen.blit(texte, (self.buttons[k].midtop[0]-texte.get_size()[0]//2, self.buttons[k].midtop[1]+15-texte.get_size()[1]//2))
        
        screen.blit(screen, (0,0))


    class videoSettingsMenu():
        def __init__(self):
            pass

    class creditsMenu():
        def __init__(self):
            pass

    class languageMenu():
        def __init__(self):
            pass

pauseMenu((0,0))