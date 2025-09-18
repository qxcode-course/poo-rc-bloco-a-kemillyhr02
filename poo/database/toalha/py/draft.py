class Towel:
    def __init__(self,color:str, size:str):
        self.color= color
        self.size= size
        self.wetness= 0

    def dry(self, amout:int):
        if self.wetness==self.getMaxWetness():
            print("umidade ja esta no maximo")
            return
        
        self.wetness+=amout
        if self.wetness>=self.getMaxWetness():
            self.wetness=self.getMaxWetness()
            print("umidade chegou no maximo")
        

    def wringOut(self):
        self.wetness=0

    def getMaxWetness(self):
        if self.size=="P":
            return 10
        elif self.size=="M":
            return 20 
        else :
            return 30
    
    def isDry(self):
        if self.wetness==0:
            return True 
        else:
            return False 

    def __str__(self):
        return f"cor:{self.color}, tamanho:{self.size}, umidade:{self.wetness}"


cor = input()
tamanho = input()
towel = Towel(cor, tamanho)
print(towel)