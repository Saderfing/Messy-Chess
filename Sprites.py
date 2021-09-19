from random import randint

class Map():
    def __init__(self):
        self.map = [
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]]
                        ]
        
    def GetMap(self):
        return self.map
    
    def __str__(self):
        return f"""
     {self.map[0][0][0]} | {self.map[0][0][1]} | {self.map[0][0][2]} | {self.map[0][0][3]}  
    -------------------
     {self.map[0][1][0]} | {self.map[0][1][1]} | {self.map[0][1][2]} | {self.map[0][1][3]} 
    -------------------
     {self.map[0][2][0]} | {self.map[0][2][1]} | {self.map[0][2][2]} | {self.map[0][2][3]} 
    -------------------
     {self.map[0][3][0]} | {self.map[0][3][1]} | {self.map[0][3][2]} | {self.map[0][3][3]} 
    """


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
        super().__init__(self, HP, streght, speed, range)
    
    def Move(self):
        super().Move()
    
    def Damage(self, strenght):
        super().Damage(strenght)