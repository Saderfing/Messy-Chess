import pygame

class Window():
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.clockTime = 60
        self.bg = None
        self.screen = pygame.display.set_mode((self.width,self.height))
    
    def CreatGameWindow(self):
        pygame.display.set_caption("Messy Chess")  
        
    
    def GetGameStat(self):
        return self.isRunning
    
    def GetClockTime(self):
        return self.clockTime
    
    def GetBackground(self):
        return self.bg

main = Window()
main.CreatGameWindow()
pygame.init()

while main.GetGameStat():
    clock.tick(GetClockTime)
        