from random import randint


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
            print(lastPos)
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
    def __init__(self, color:str, hp:int, strenght:int, pos:tuple):
        self.name = "Patate"
        self.range = 1
        super().__init__(self.name,color,hp,strenght,self.range,pos)

    def Movement(self, newPos:tuple):
        localMap = map.GetMap()
        if newPos[0] == self.pos[0] and newPos[1] != self.pos[1] and map.IsEmpty(newPos):
            
            map.SetObjectPosition(self.GetColorName(),newPos,self.pos)
        elif newPos[0] != self.pos[0] and newPos[1] == self.pos[1] and map.IsEmpty(newPos):
            
            map.SetObjectPosition(self.GetColorName(),newPos,self.pos)
        else:
            print("pas possible")

    def Attack(self):
        localMap = map.GetMap()
        attackPosList = []
        attackPosList.append((self.pos[0]+self.range,self.pos[1]))
        attackPosList.append((self.pos[0]-self.range,self.pos[1]))
        attackPosList.append((self.pos[0],self.pos[1]-self.range))
        attackPosList.append((self.pos[0],self.pos[1]+self.range))

        for i in attackPosList:
            if i in localMap and not map.IsEmpty(i):
                print("attack in ", i)
                




class Sponge(Piece):
    def __init__(self, name:str, color: str, hp: int, strenght: int, range: int, pos:tuple):
        self.name = name
        super().__init__(self.name, color, hp, strenght, range, pos)




map = Map()
eponge = Sponge("sponge", "White", 10, 10, 1, (0,0))
patateBlanche = Patate("White",10,10,(3,1))
patateNoire = Patate("Black", 10, 10,(2,1))

print(map)
patateNoire.Attack()
print(map)
