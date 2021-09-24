import pygame
from pygame.mixer import fadeout
import Sprites
from Reference import Ref,WIDTH,HEIGHT
import pygame

ref = Ref((WIDTH,HEIGHT))

map = Sprites.Map()
map.SetObjectPosition("eponge", (0,0))

class Window:
    def __init__(self):
        self.CHECKERBOARDIMG = pygame.image.load("assets/checkerboard.png").convert()
        self.rectCheckerBoard = self.CHECKERBOARDIMG.get_rect()
        self.rectCheckerBoard.x = self.rectCheckerBoard.width/2

        self.bg = pygame.image.load("assets/bg.png").convert()

        self.whitePotato = pygame.image.load("assets/whitePotato.png").convert_alpha()

    def DrawMisc(self):
        pygame.Surface.blit(ref.GetScreen(),game.CHECKERBOARDIMG,(ref.GetWidth()/2 - game.rectCheckerBoard.x,0))

    def DrawBackground(self):
        pygame.Surface.blit(ref.GetScreen(),self.bg,(0,0))

    def DrawMap(self):
        localMap = Sprites.map.GetMap()
        for i in localMap.keys():
            if Sprites.map.IsEmpty(i):
                pass
            else:pygame.Surface.blit(ref.SCREEN, self.whitePotato, (280+i[0]*180, i[1]*180))


run = True
game = Window()
while run:
    game.DrawBackground()
    game.DrawMisc()
    game.DrawMap()


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

pygame.quit()
