from random import randint

class Map():
    def __init__(self):
        self.empty = "               "
        self.map = {(0,0):self.empty, (0,1):self.empty, (0,2):self.empty, (0,3):self.empty,
                    (1,0):self.empty, (1,1):self.empty, (1,2):self.empty, (1,3):self.empty,
                    (2,0):self.empty, (2,1):self.empty, (2,2):self.empty, (2,3):self.empty,
                    (3,0):self.empty, (3,1):self.empty, (3,2):self.empty, (3,3):self.empty}

    def __str__(self):
        return f"""
                     |                 |                 |
     {self.map[0,0]} | {self.map[0,1]} | {self.map[0,2]} | {self.map[0,3]}
                     |                 |                 |
    -------------------
                     |                 |                 |
     {self.map[1,3]} | {self.map[1,1]} | {self.map[1,2]} | {self.map[1,3]}
                     |                 |                 |
    -------------------
                     |                 |                 |
     {self.map[2,0]} | {self.map[2,1]} | {self.map[2,2]} | {self.map[2,3]}
                     |                 |                 |
    -------------------
                     |                 |                 |
     {self.map[3,0]} | {self.map[3,1]} | {self.map[3,2]} | {self.map[3,3]}
                     |                 |                 |
    """


    def GetMap(self):
        return self.map

    def SetObjectPosition(self, objName:str, pos=tuple):
        if pos in self.map:
            self.map[pos] = objName
        else:
            print("invalid position")



class Piece():
    def __init__(self, name:str, hp:int, strenght:int, speed:int, range:int):
        self.name = name
        self.hp = hp
        self.df = None # ajout de la défence ?
        self.strenght = strenght
        self.speed = speed
        self.range = range

    def Move(self):
        pass

    def Damage(self, strenght):
        self.HP -= randint(1,2)*strenght




class Sponge(Piece):
    def __init__(self, name:str, hp:int, strenght:int, speed:int, range:int):
        super().__init__(self, name, hp, strenght, speed, range)

    def Move(self):
        super().Move()

    def Damage(self, strenght):
        super().Damage(strenght)
