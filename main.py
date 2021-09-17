from random import randint

class Map():
    def __init__(self):
        self.map = 
        [
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[],[],[],[]],
                        ]


class Piece():
    def __init__(self, HP, streght, speed, range):
        self.HP = HP
        self.DF = None # ajout de la défence ?
        self.strenght = strenght
        self.speed = speed
        self.range = range
        
    def Move(self):
        pass
        
    def Damage(self):
        pass
    
    def Attack(self, other):
        other.HP -= randint(1,2)*strenght
        