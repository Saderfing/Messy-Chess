import pygame
from pygame.mixer import fadeout
import Sprites

class Window():
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.isRunning = True
        self.FPS = 60
        self.bg = None
        self.screen = pygame.display.set_mode((self.width,self.height))
    
    def CreatGameWindow(self):
        pygame.display.set_caption("Messy Chess")  
        
    
    def GetGameStat(self):
        return self.isRunning
    
    def SetGameStat(self, stat:bool):
        self.isrunning = False
    
    def SetTick(self):
        clock.tick(60)
    
    def GetBackground(self):
        return self.bg
    

main = Window()
main.CreatGameWindow()
pygame.init()
clock = pygame.time.Clock()

while main.GetGameStat():
    main.SetTick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                main.SetGameStat(False)
                pygame.quit()