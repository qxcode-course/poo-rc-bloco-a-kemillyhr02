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
        if self.size=="M":
            return 20 
        if self.size=="G":
            return 30
        return 0
    
    def isDry(self):
        if self.wetness==0:
            return True 
        else:
            return False 

    def __str__(self):
        return f"cor:{self.color}, tamanho:{self.size}, umidade:{self.wetness}"
def main():
    towel: Towel=Towel(" ", " ")
    while True :
        line: str=input()
        args: list[str]= line.split(" ") 

        if args[0]=="end":
            break

        elif args[0]=="new":
            color:str= args[1]
            size: str= args[2]
        elif  args[0]== "dry":
            amount: int= int(args[1])
            towel.dry(amount)    
            towel=Towel(color, size)
        elif args[0] == "show":
            print(towel)
        else :
            print("fail: comando não encontrado")
main() #passo 1
