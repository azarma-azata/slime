import pygame
import manager

texts = manager.getTexts()

class pauseMenu():
    def __init__(self, screenSize):
        #self.creditsMenu = fcredits()
        
        self.activeMenu = None
        self.status = None
        
        #settings
        self.gameLanguage = "fr"
        
        self.text = tuple(texts[self.gameLanguage][0:7])
        self.buttonsRect = [pygame.Rect(screenSize[0]//2-150, screenSize[1]//2+((k-2)*60)-15, 300, 30) for k in range(len(self.text))]
        self.buttons = [Button(self.text[k], (180,180,180), self.buttonsRect[k], k) for k in range(len(self.text))]
        
        self.idToReturn = None

        self.i = 0

    def gettingClicked(self):
        coos=pygame.mouse.get_pos()

        if not self.activeMenu:
            for k in self.buttons:
                if k.rect.collidepoint(coos):
                    k.gotClicked()
        else: pass
    
    
    def videoSettingsMenu(self, screen):
        pass

    def audioSettingsMenu(self, screen):
        pass

    def keySettingsMenu(self, screen, police):

        def changeKey(self, key):
            print(key)

            with open("test.csv", "r", encoding="utf-8") as file:
                n=[k.rstrip().split(";") for k in file.readlines()]
            with open("test.csv", "w+", encoding="utf-8") as file:
                n[self.buttonToChange.id][2] = str(key)
                for k in n:
                    for i in k:
                        file.write(n[k][i])
                        if i!=2: file.write(";")
                    file.write("\n")

        a=manager.getKeys()
        b=manager.getTexts()[self.gameLanguage]

        texts=b[6:12]
        if self.i == 0:
            self.menuButtons=[]
            i=0
            for value in a.values():
                print(value)
                self.menuButtons.append(Button(pygame.key.name(value[1]), (180,180,180), pygame.Rect((screen.get_width()//4)*3, 40*i+80,32,32), i))
                i+=1
            self.i=1

        i=0
        for k in self.menuButtons:
            if k.update(screen, police):
                self.status="waiting"
                self.buttonToChange = k
            pygame.draw.rect(screen, (0,0,0), (screen.get_width()//2-270, k.rect.y, 500, 30))
            pygame.draw.rect(screen, (180,180,180), (screen.get_width()//2-270+2, k.rect.y+2, 500-4, 30-4))
            temp = police.render(texts[i], 0, (0,0,0))
            screen.blit(temp, (screen.get_width()//2-250, k.rect.centery-temp.get_height()//2))
            i+=1
    


    def creditsMenu(self, screen):
        pass

    def languageMenu(self, screen):
        pass

    def update(self, screen, police):
        self.menus = [self.videoSettingsMenu, self.audioSettingsMenu, self.keySettingsMenu, self.languageMenu, self.creditsMenu]

        s=pygame.Surface(screen.get_size())
        s.set_alpha(100)
        s.fill((0,0,0))
        screen.blit(s, (0,0))

        if not self.activeMenu:
            for k in self.buttons:
                a=k.update(screen, police)
                if a: return a
        else:
            self.activeMenu(screen, police)

        return False


class Button():
    def __init__(self, text, color, rect, myId):
        self.id = myId
        self.text = str(text)
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
        return False
    
    def gotClicked(self):
        self.color = (255,255,255)
        self.returnBack = 1