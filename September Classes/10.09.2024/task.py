class Computer:
    
    def __init__(self):
        self.__amount = 20000
    
    def getprice(self):
        return self.__amount

ob = Computer()
ob.__amount = 50000
print(ob.getprice())