from random import randint

class Map():
    def __init__(self):
        self.map = [
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
                        ]


class Piece():
    def __init__(self, HP, strenght, speed, range):
        
        self.HP = HP
        self.DF = None # ajout de la défence ?
        self.strenght = strenght
        self.speed = speed
        self.range = range
        
    def Move(self):
        pass
        
    def Damage(self, strenght):
        self.HP -= randint(1,2)*strenght
        
    


class Sponge(Piece):
    def __init__(self, HP, streght, speed, range):
        super().__init__( HP, streght, speed, range)
    
    def Move(self):
        super().Move()
    
    def Damage(self, strenght):
        super().Damage(strenght)