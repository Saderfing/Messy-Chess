from random import randint


class Map():
    def __init__(self):
        self.EMPTY = "               "
        self.map = {(0,0):self.EMPTY, (0,1):self.EMPTY, (0,2):self.EMPTY, (0,3):self.EMPTY,
                    (1,0):self.EMPTY, (1,1):self.EMPTY, (1,2):self.EMPTY, (1,3):self.EMPTY,
                    (2,0):self.EMPTY, (2,1):self.EMPTY, (2,2):self.EMPTY, (2,3):self.EMPTY,
                    (3,0):self.EMPTY, (3,1):self.EMPTY, (3,2):self.EMPTY, (3,3):self.EMPTY}

    def __str__(self):
        return f"""
                     |                 |                 |
     {self.map[0,0]} | {self.map[0,1]} | {self.map[0,2]} | {self.map[0,3]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[1,3]} | {self.map[1,1]} | {self.map[1,2]} | {self.map[1,3]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[2,0]} | {self.map[2,1]} | {self.map[2,2]} | {self.map[2,3]}
                     |                 |                 |
    -----------------------------------------------------------------------
                     |                 |                 |
     {self.map[3,0]} | {self.map[3,1]} | {self.map[3,2]} | {self.map[3,3]}
                     |                 |                 |
    """

    def GetMap(self):
        return self.map

    def SetObjectPosition(self, objName:str, newPos:tuple, lastPos=None):
        if lastPos != None:
            print(lastPos)
            print("a")
            self.map[lastPos] = self.EMPTY
        if newPos in self.map.keys():
            self.map[newPos] = objName
        else:
            print("invalid position")


    def IsEmpty(self, pos:tuple):
        if self.EMPTY == self.map[pos]:
            print("a")
            return True
        else:
            return False



class Piece():
    def __init__(self, name:str, color:str,hp:int, strenght:int, speed:int, range:int, pos:tuple):
        self.name = name
        self.color = color
        self.hp = hp
        self.df = None # ajout de la défence ?
        self.strenght = strenght
        self.speed = speed
        self.range = range
        self.pos = pos
        map.SetObjectPosition(self.name, self.pos)

    def GetName(self):
        return self.name

    def GetPos(self):
        return self.pos


    def Move(self, newPos:tuple):
        if map.IsEmpty(newPos):
            map.SetObjectPosition(self.name, newPos)
        else:
            print("already somthing")


    def Damage(self, strenght):
        self.HP -= randint(1, 2)*strenght

    def GetColorName(self):
        return self.color+self.name

class Patate(Piece):
    def __init__(self, color, hp, strenght, speed, range, pos):
        self.name = "Patate"
        super().__init__(self.name,color,hp,strenght,speed,range,pos)

    def Movement(self, newPos:tuple):
        if newPos[0] == self.pos[0] and newPos[1] != self.pos[1]:
            self.CheckAttack()
            map.SetObjectPosition(self.GetColorName(),newPos,self.pos)
        elif newPos[0] != self.pos[0] and newPos[1] == self.pos[1]:
            self.CheckAttack()
            map.SetObjectPosition(self.GetColorName(),newPos,self.pos)
        else:
            print("pas possible")

    def CheckAttack(self):
        localMap = map.GetMap()
        if self.GetPos() in localMap.keys() and not map.IsEmpty(self.GetPos()):
            print("attack", self.GetPos())

        else:
            print("nothing to attack")





class Sponge(Piece):
    def __init__(self, name: str, color: str, hp: int, strenght: int, speed: int, range: int, pos:tuple):
        super().__init__(name, color, hp, strenght, speed, range, pos)




map = Map()
eponge = Sponge("sponge", "White", 10, 10, 1, 1, (0,0))
print(map)
patateBlanche = Patate("white",10,10,1,2,(0,0))
patateNoire = Patate("black", 10, 10, 2, 2,(0,1))
map.SetObjectPosition(patateBlanche.GetColorName(), patateBlanche.GetPos())
map.SetObjectPosition(patateNoire.GetColorName(), patateNoire.GetPos())
print(map)
patateBlanche.Movement((0,1))
print(map)
