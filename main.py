import pygame
from pygame.mixer import fadeout
import Sprites
from Reference import Ref,WIDTH,HEIGHT


ref = Ref((WIDTH,HEIGHT))


class Window:
    def __init__(self):
        self.CHECKERBOARDIMG = pygame.image.load("assets/checkerboard.png").convert()
        self.rectCheckerBoard = self.CHECKERBOARDIMG.get_rect()
        self.rectCheckerBoard.x = self.rectCheckerBoard.width/2

        self.bg = pygame.image.load("assets/bg.png").convert()

        self.whiteSponge = pygame.image.load("assets/whiteEponge.png").convert_alpha()
        self.blackSponge = pygame.image.load("assets/blackEponge.png").convert_alpha()
        self.whitePotato = pygame.image.load("assets/whitePotato.png").convert_alpha()
        self.blackPotato = pygame.image.load("assets/blackPotato.png").convert_alpha()
        self.whiteBilly = pygame.image.load("assets/whitBilly.png").convert_alpha()
        self.blackBilly = pygame.image.load("assets/blackBilly.png").convert_alpha()
        self.whiteDejaVu = pygame.image.load("assets/whiteDejavu.png").convert_alpha()
        self.blackDejaVu = pygame.image.load("assets/blackDejaVu.png").convert_alpha()

        self.dictImgPiece = {"WhiteSponge":self.whiteSponge, "BlackSponge":self.blackSponge, "WhitePatate":self.whitePotato, "BlackPatate":self.blackPotato, "WhiteBilly":self.whiteBilly, "BlackBilly": self.blackBilly,"WhiteDeja-Vu":self.whiteDejaVu, "BlackDeja-Vu":self.blackDejaVu}

    def DrawMisc(self):
        pygame.Surface.blit(ref.GetScreen(),window.CHECKERBOARDIMG,(ref.GetWidth()/2 - window.rectCheckerBoard.x,0))

    def DrawBackground(self):
        pygame.Surface.blit(ref.GetScreen(),self.bg,(0,0))

    def DrawMap(self):
        localMap = Sprites.map.GetMap()
        for i in localMap.keys():
            if Sprites.map.IsEmpty(i):
                pass
            else:
                pygame.Surface.blit(ref.SCREEN, self.dictImgPiece[localMap[i]], (280+i[0]*180, i[1]*180))

class Consol():
    def __init__(self):
        self.turn = 0
        self.INPUT_TO_INDEX = {"up":0, "down":1, "right":2, "left":3, "attack":5}
        self.PIECELISTE = ("eponge", "patate", "dejavu", "billy")
        self.ACTION = {"attack": self.Attack, "move": self.MovePiece}
        self.ACTIONLISTE = ("attack", "move",)
        self.DIR = ("up","down","right","left")
        self.COLOR = ("white", "black")
        self.OBJECTCOMANDS = {"epongewhite":[Sprites.epongeBlanche.Up,Sprites.epongeBlanche.Down,Sprites.epongeBlanche.Left,Sprites.epongeBlanche.Right,Sprites.epongeBlanche.Attack], 
                        "epongeblack":[Sprites.epongeNoire.Up,Sprites.epongeNoire.Down,Sprites.epongeNoire.Left,Sprites.epongeNoire.Right,Sprites.epongeNoire.Attack],
                        "patatewhite":[Sprites.patateBlanche.Up,Sprites.patateBlanche.Down,Sprites.patateBlanche.Left,Sprites.patateBlanche.Right,Sprites.patateBlanche.Attack], 
                        "patatblack":[Sprites.patateNoire.Up,Sprites.patateNoire.Down,Sprites.patateNoire.Left,Sprites.patateNoire.Right,Sprites.patateNoire.Attack], 
                        "billywhite":[Sprites.billyBlanc.Up,Sprites.billyBlanc.Down,Sprites.billyBlanc.Left,Sprites.billyBlanc.Right,Sprites.billyBlanc.Attack],
                        "billyblack":[Sprites.billyNoire.Up,Sprites.billyNoire.Down,Sprites.billyNoire.Left,Sprites.billyNoire.Right,Sprites.billyNoire.Attack],
                        "dejavuwhite":[Sprites.dejaVuBlanc.UpLeft,Sprites.dejaVuBlanc.UpRight,Sprites.dejaVuBlanc.DownLeft,Sprites.dejaVuBlanc.DownRight,Sprites.dejaVuBlanc.Attack],
                        "dejavublack":[Sprites.dejaVuNoire.UpLeft,Sprites.dejaVuNoire.UpRight,Sprites.dejaVuNoire.DownLeft,Sprites.dejaVuNoire.DownRight,Sprites.dejaVuNoire.Attack] }
        
    def NewRound(self):
        print(f"Nouveau tour, au {self.COLOR[self.turn]} de jouer")
        turn = None
        while turn is None:
            turn = str(input(f"Que voulez-vous faire ? : {self.ACTIONLISTE}: ")).lower()
            if turn in self.ACTION.keys():
                self.ACTION[turn]()
            else: 
                print("La fonction n'est pas reconnue")
    
    def SetTurn(self):
        self.turn = 1 if self.turn == 0 else 0
    
    def Attack(self):
        piece = None
        while piece is None:
            piece = str(input(f"Quelle pièce doit attaquer: {self.PIECELISTE}: ")).lower()
            if piece in self.PIECELISTE:
                self.OBJECTCOMANDS[piece+self.COLOR[self.turn]][4]
                self.SetTurn()
            else: 
                print("Erreur")
                piece = None
    
    def MovePiece(self):
        piece = self.DefPiece()
        color = self.COLOR[self.turn]
        dir = self.DefDir()
        dist = None
        if piece in ("patate", "dejavu"):
            dist = self.DefDist()
        self.OBJECTCOMANDS[piece+color][dir](dist)
        self.SetTurn()
        
        
    def DefDir(self):
        _dir = None
        while _dir is None:
            _dir = str(input(f"Quelle direction ? : {self.DIR}: ")).lower()
            if _dir in self.DIR:
                return self.INPUT_TO_INDEX[_dir]
            else:
                print(f"La direction {_dir} n'existe pas")
                _dir = None
        
    
    def DefDist(self):
        _dist = None
        while _dist is None:
            _dist = int(input("Quelle distance ? : "))
            if _dist in (0, 1, 2, 3):
                return _dist
            else:
                _dist = None
    

    def DefPiece(self):
        _piece = None
        while _piece == None:
            _piece = str(input(f"Quelle piece voulez-vous jouer ? :{self.PIECELISTE}: ")).lower()
            if _piece in self.PIECELISTE:
                return _piece
            else:
                return None
            
run = True
consol = Consol()
window = Window()
while run:
    window.DrawBackground()
    window.DrawMisc()
    window.DrawMap()



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()