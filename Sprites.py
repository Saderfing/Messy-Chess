from random import random

class Map():
    def __init__(self):
        self.EMPTY = "               "
        self.map = {(0,0):self.EMPTY, (1,0):self.EMPTY, (2,0):self.EMPTY, (3,0):self.EMPTY,
                    (0,1):self.EMPTY, (1,1):self.EMPTY, (2,1):self.EMPTY, (3,1):self.EMPTY,
                    (0,2):self.EMPTY, (1,2):self.EMPTY, (2,2):self.EMPTY, (3,2):self.EMPTY,
                    (0,3):self.EMPTY, (1,3):self.EMPTY, (2,3):self.EMPTY, (3,3):self.EMPTY}

    def __str__(self):
        return f"""
                     |                 |                 |
     {self.map[0,0]} | {self.map[1,0]} | {self.map[2,0]} | {self.map[3,0]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[0,1]} | {self.map[1,1]} | {self.map[2,1]} | {self.map[3,1]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[0,2]} | {self.map[1,2]} | {self.map[2,2]} | {self.map[3,2]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[0,3]} | {self.map[1,3]} | {self.map[2,3]} | {self.map[3,3]}
                     |                 |                 |
    """

    def GetMap(self):
        return self.map

    def SetObjectPosition(self, objName:str, newPos:tuple, lastPos=None):
            if lastPos != None:
                self.map[lastPos] = self.EMPTY
            if newPos in self.map.keys():
                self.map[newPos] = objName
            else:
                print("invalid position")



    def IsEmpty(self, pos:tuple):
        if self.EMPTY == self.map[pos]:
            return True
        else:
            return False
    def SetEmpty(self,pos):
        self.map[pos] = self.EMPTY

class Piece():
    def __init__(self, name:str, color:str,hp:int, strenght:int, range:int, pos:tuple):
        self.name = name
        self.color = color
        self.hp = hp
        self.df = None # ajout de la défence ?
        self.strenght = strenght
        self.range = range
        self.pos = pos
        map.SetObjectPosition(self.GetColorName(), self.pos)


    def GetName(self):
        return self.name

    def GetPos(self):
        return self.pos

    def GetColor(self):
        return self.color

    def Move(self, newPos:tuple):
        if map.IsEmpty(newPos):
            map.SetObjectPosition(self.name, newPos)
        else:
            print("already somthing")

    def GetHp(self):
        return self.hp

    def Damage(self, strenght):
        self.hp -= 10*round(random()*strenght)



    def GetColorName(self):
        return self.color+self.name

    def SetKill(self):
        map.SetEmpty(self.pos)

class Patate(Piece):
    def __init__(self, color:str, hp:int, strenght:int, pos:tuple):
        self.name = "Patate"
        self.range = 1
        super().__init__(self.name,color,hp,strenght,self.range,pos)

    def CapDist(self, dist):
        if dist < 1:
            return 1
        if dist > 4:
            return 4
        return dist

    def Up(self, dist): # déplacement en Y vers le haut
        localMap = map.GetMap()
        pos = list(self.pos)
        dist = self.CapDist(dist)
        newPos = (pos[0], pos[1] - dist)
        if map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos,self.pos)
            self.pos = newPos

    def Down(self, dist):# déplacement en Y vers le bas
        localMap = map.GetMap()
        pos = list(self.pos)
        dist = self.CapDist(dist)
        newPos = (pos[0], pos[1] + dist)
        if pos[1] < self.speed and map.IsEmpty((pos[0], pos[1] - pos[1])):
            map.SetObjectPosition(self.GetColorName(), (pos[0],self.speed), self.pos)
            self.pos = newPos

    def Right(self, dist):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        dist = self.CapDist(dist)
        newPos = (pos[0] + dist, pos[1])
        if pos[1] < self.speed and map.IsEmpty((pos[0], pos[1] - pos[1])):
            map.SetObjectPosition(self.GetColorName(), (self.speed, pos[1]),self.pos)
            self.pos = newPos

    def Left(self, dist):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        dist = self.CapDist(dist)
        newPos = (pos[0] - dist, pos[1])
        if map.IsEmpty((pos[0], pos[1] - pos[1])):
            map.SetObjectPosition(self.GetColorName(), (pos[0] - pos[0], pos[1]), self.pos)
            self.pos = newPos


    def Attack(self):

            localMap = map.GetMap()
            attackPosList = []
            attackPosList.append((self.pos[0]+self.range,self.pos[1]))
            attackPosList.append((self.pos[0]-self.range,self.pos[1]))
            attackPosList.append((self.pos[0],self.pos[1]-self.range))
            attackPosList.append((self.pos[0],self.pos[1]+self.range))

            for i in attackPosList:
                if i in localMap and not map.IsEmpty(i):
                    piece = localMap[i]
                    objPiece = game.GetObjectByColorName(piece)
                    objPiece.Damage(self.strenght)
                    print("qui c qu'il attack", piece)

            localMap = map.GetMap()
            attackPosList = []
            attackPosList.append((self.pos[0]+self.range,self.pos[1]))
            attackPosList.append((self.pos[0]-self.range,self.pos[1]))
            attackPosList.append((self.pos[0],self.pos[1]-self.range))
            attackPosList.append((self.pos[0],self.pos[1]+self.range))

            for i in attackPosList:
                if i in localMap and not map.IsEmpty(i):
                    piece = localMap[i]
                    objPiece = game.GetObjectByColorName(piece)
                    objPiece.Damage(self.strenght)
                    print("qui c qu'il attack", piece)
                    if objPiece.GetHp() <= 0:
                        objPiece.SetKill()

class Billy(Piece):
    def __init__(self, color, hp, strenght, pos):
        self.name = "Billy"
        self.speed = 3
        super().__init__(self.name, color, hp, strenght, 1,pos)
        self.moveDir = {0: self.Up, 1: self.Down, 2: self.Right, 3: self.Left}

    def Up(self, dist=None): # déplacement en Y vers le haut
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0], pos[1] - pos[1])
        if map.IsEmpty(newPos):
                map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
                self.pos = newPos
        else:
            self.Attack(newPos)

    def Down(self, dist=None):# déplacement en Y vers le bas
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0], self.speed)
        if pos[1] < self.speed and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos
        else:
            self.Attack(newPos)

    def Right(self, dist=None):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (self.speed, pos[1])
        if pos[1] < self.speed and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos
        else:
            self.Attack(newPos)

    def Left(self, dist=None):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] - pos[0], pos[1])
        if map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos
        else:
            self.Attack((pos[0] - pos[0], pos[1]))

    def Attack(self, attackPos:tuple):
        localMap = map.GetMap()
        other = game.GetObjectByColorName(localMap[attackPos])
        if other.GetColor() != self.GetColor():
            print("attack", attackPos)
        else:
            print("nothing to attack")

class Sponge(Piece):
    def __init__(self, color: str, hp: int, strenght: int, pos:tuple):
        self.name = "Sponge"
        self.speed = 1
        self.range = 1
        super().__init__(self.name, color, hp, strenght, range, pos)

    def Up(self, dist=None): # déplacement en Y vers le haut
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0], pos[1] - self.speed)
        if newPos in localMap.keys() and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos,self.pos)
            self.pos = newPos

    def Down(self, dist=None):# déplacement en Y vers le bas
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos =  (pos[0], pos[1] + self.speed)
        if newPos in localMap.keys() and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def Right(self, dist=None):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] + self.speed, pos[1])
        if newPos in localMap.keys() and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def Left(self, dist=None):# déplacement en X
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] - self.speed, pos[1])
        if newPos in localMap.keys() and map.IsEmpty(newPos):
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def Attack(self):
        localMap = map.GetMap()
        attackPos= [(x,self.pos[1]) for x in range(-self.range,self.range+1)]
        print(self.pos)


        for i in attackPos:

            if i in localMap.keys() and not map.IsEmpty(i) and not i==self.pos:
                piece = localMap[i]
                objPiece = game.GetObjectByColorName(piece)
                objPiece.Damage(self.strenght)
                print("qui c qu'il attack", piece)
                if objPiece.GetHp() <= 0:
                    objPiece.SetKill()

class DejaVu(Piece):
    def __init__(self, color: str, hp: int, strenght: int, pos: tuple):
        self.name = "Deja-Vu"
        self.range = 1
        super().__init__(self.name, color, hp, strenght, self.range, pos)

    def CapDist(self, dist):
        if dist < 1:
            return 1
        if dist > 4:
            return 4
        return dist

    def UpRight(self,dist): # déplacement en vers le haut droit
        localMap = map.GetMap()
        pos = list(self.pos)
        dist = self.CapDist(dist)
        newPos = (pos[0] + dist , pos[1] - dist)
        if newPos in localMap.keys() and map.IsEmpty(newPos) :
            map.SetObjectPosition(self.GetColorName(), newPos,self.pos)
            self.pos = newPos

    def DownRight(self,dist): # déplacement bas droit
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] - dist , pos[1] - dist)
        if newPos in localMap.keys() and map.IsEmpty(newPos) :
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def UpLeft(self, dist):# déplacement en haut gauche
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] - dist, pos[1]-dist)
        if newPos in localMap.keys() and map.IsEmpty(newPos) :
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def DownLeft(self, dist):# déplacement en bas gauche
        localMap = map.GetMap()
        pos = list(self.pos)
        newPos = (pos[0] - dist, pos[1]+dist)
        if newPos in localMap.keys() and map.IsEmpty(newPos) :
            map.SetObjectPosition(self.GetColorName(), newPos, self.pos)
            self.pos = newPos

    def Attack(self):
        attackPos = []
        localMap = map.GetMap()
        for x,y in zip(range(-self.range+self.pos[0], self.range+1+self.pos[0]), range(-self.range+self.pos[1], self.pos[1]+self.range+1)):
            attackPos.append((x,y))
        for x,y in zip(range(self.pos[0]-self.range, self.pos[0]+self.range+1), range(self.pos[1]+self.range, self.pos[1]-self.range-1, -1)):
            attackPos.append((x,y))

        for i in attackPos:
            if i in localMap.keys() and not map.IsEmpty(i) and not i==self.pos:
                piece = localMap[i]
                objPiece = game.GetObjectByColorName(piece)
                objPiece.Damage(self.strenght)
                print("qui c qu'il attack", piece)
                if objPiece.GetHp() <= 0:
                    objPiece.SetKill()



class Game():
    def __init__(self):
        self.dictPiece = dict()

    def GetObjectByColorName(self, colorName:str):
        if colorName in self.dictPiece:
            return self.dictPiece[colorName]
        print("not found")

    def AddToPieceDict(self, obj:dict):
        for keys,values in obj.items():
            self.dictPiece[keys] = values
    def GetDictPiece(self):
        return self.dictPiece


    def update(self):
        _epongeBlanche = self.dictPiece["WhiteSponge"]
        _epongeNoire = self.dictPiece["BlackSponge"]
        _patateBlanche = self.dictPiece["WhitePatate"]
        _patateNoire = self.dictPiece["BlackPatate"]
        _billyBlanc = self.dictPiece["WhiteBilly"]
        _billyNoire = self.dictPiece["BlackBilly"]
        _dejavuBlanc = self.dictPiece["WhiteDeja-Vu"]
        _dejavuNoire = self.dictPiece["BlackDeja-Vu"]

map = Map()
game = Game()

epongeBlanche = Sponge("White", 10, 10, (1,0))
epongeNoire = Sponge("Black", 10, 10, (2,3))
patateBlanche = Patate("White", 10, 10,(0,0))
patateNoire = Patate("Black", 10, 10,(3,3))
billyBlanc = Billy("White", 10, 10, (3,0))
billyNoire = Billy("Black", 10, 10, (0,3))
dejaVuBlanc = DejaVu("White",10,10,(2,0))
dejaVuNoire = DejaVu("Black",10,10,(1,3))

game.AddToPieceDict(
    {epongeBlanche.GetColorName():epongeBlanche, 
     epongeNoire.GetColorName():epongeNoire, 
     patateBlanche.GetColorName():patateBlanche, 
     patateNoire.GetColorName():patateNoire, 
     billyBlanc.GetColorName():billyBlanc,
     billyNoire.GetColorName():billyNoire, 
     dejaVuBlanc.GetColorName():dejaVuBlanc, 
     dejaVuNoire.GetColorName():dejaVuNoire})

