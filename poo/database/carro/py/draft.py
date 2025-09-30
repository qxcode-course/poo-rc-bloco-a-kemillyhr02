class Carro:
    def __init__(self):
        self.psg: int=0
        self.km: int=0
        self.gas: int=0
   
    def __str__(self)->str:
        return f"pass: {self.psg}, gas: {self.gas}, km: {self.km}"
    
    def enter(self):
        if self.psg>=2:
            print(f"fail: limite de pessoas atingido")
        else :
            self.psg+=1
    
    def leave(self):
        if self.psg==0:
            print(f"fail: nao ha ninguem no carro")
        else :
            self.psg-=1
    
    def fuel(self, increment: int):
        self.gas+=increment
        if self.gas>=100:
            self.gas=100
        
    def drive(self, distance: int):
        if self.psg==0:
            print(f"fail: nao ha ninguem no carro")
        elif self.gas==0:
            print(f"fail: tanque vazio")
        elif self.gas<distance:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km+=self.gas
            self.gas=0
        else :
            self.km+=distance
            self.gas-=distance

def main():
    carro=Carro()
    while True:
        line= input()
        print(f"${line}")
        args= line.split()
        if args[0]=="end":
            break
        elif args[0]=="enter":
            carro.enter()
        elif args[0]=="show":
            print(carro)
        elif args[0]=="leave":
            carro.leave()
        elif args[0]=="fuel":
            increment = int(args[1])
            carro.fuel(increment)
        elif args[0]=="drive":
            increment= int(args[1])
            carro.drive(increment)
main()

