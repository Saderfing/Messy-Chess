class Constant():
    def __init__(self):
        self.__constant = dict()
    
    def SetConstante(self, key, value):
        if self.KeyExist(key):
            raise IndexError("This key already exist")
        else:
            self.__constant[key] = value
        
    def KeyExist(self, key):
        return True if key in self.__constant.keys() else False
    
    def GetConstant(self, key):
        if self.KeyExist(key):
            return self.__constant[key]
        else:
            raise IndexError(f"There is no key : {key}")
    
    