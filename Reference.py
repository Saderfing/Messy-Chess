import pygame

class Ref():
    def __init__(self, dimension:tuple):
        self.dimension = dimension
        self.SCREEN = pygame.display.set_mode(self.dimension) 
    
    def GetDim(self):
        return self.dimension

    def GetWidth(self):
        return self.dimension[0]

    def GetHeight(self):
        return self.dimension[1]
    
    def GetScreen(self):
        return self.SCREEN

WIDTH = 1280
HEIGHT = 720
