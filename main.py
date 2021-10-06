import pygame
from pygame.mixer import fadeout
import Sprites
from Reference import Ref,WIDTH,HEIGHT
import pygame

#ref = Ref((WIDTH,HEIGHT))


class Window:
    def __init__(self):
        self.CHECKERBOARDIMG = pygame.image.load("assets/checkerboard.png").convert()
        self.rectCheckerBoard = self.CHECKERBOARDIMG.get_rect()
        self.rectCheckerBoard.x = self.rectCheckerBoard.width/2

        self.bg = pygame.image.load("assets/bg.png").convert()

        self.whitePotato = pygame.image.load("assets/whitePotato.png").convert_alpha()

    def DrawMisc(self):
        pygame.Surface.blit(ref.GetScreen(),window.CHECKERBOARDIMG,(ref.GetWidth()/2 - window.rectCheckerBoard.x,0))

    def DrawBackground(self):
        pygame.Surface.blit(ref.GetScreen(),self.bg,(0,0))

    def DrawMap(self):
        localMap = Sprites.map.GetMap()
        for i in localMap.keys():
            if Sprites.map.IsEmpty(i):
                pass
            else:pygame.Surface.blit(ref.SCREEN, self.whitePotato, (280+i[0]*180, i[1]*180))

class Consol():
    def __init__(self):
        self.turn = 0
        self.pieceListe = ("eponge", "patate", "dejavu", "billy")
        self.action = {"attack": self.MovePiece, "move": self.MovePiece}
        
    def NewRound(self):
        pieces = Sprites.game.GetPieceDict()
        turn = None
        while turn is None:
            turn = str(input("Que voulez-vous faire ? : (attack/move): ")).lower()
            if turn in self.action.keys():
                self.action[turn]()
            else: 
                print("la fonction n'est pas reconnue")
        
    def MovePiece(self):
        piece = self.DefPiece()
        color = self.GetColor()
        dir = self.DefDir()
        if piece in ("patate", "dejavu"):
            lenght = self.GetColor()
    
    def DefDir(self):
        _dir = None
        while _dir is None:
            _dir = input("Quelle distance ? : ")
            if type(_dir) is type(int):
                return _dir
            else:
                _dir = None
    
    def DefPiece(self):
        print(f"Vous pouvez jouez les pièces {self.pieceListe}")
        _piece = None
        while _piece == None:
            _piece = str(input("Quelle piece voulez-vous jouer ? : ")).lower()
            if _piece in self.pieceListe:
                return _piece
            else:
                return None
            
            
run = True
while run:
    pass
