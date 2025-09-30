class Calculator:
    def __init__(self, batteryMax: int):
        self.battery: int=0
        self.batteryMax: int = batteryMax
        self.display: float = 0
    
    def __str__(self)-> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def recarregar(self, increment: int):
        self.battery+= increment
        if self.battery >= self.batteryMax:
            self.battery=self.batteryMax

    def somar(self, a : int , b: int):
        if self.battery==0:
            print("fail: bateria insuficiente")
        else :
            self.display= a+b
            self.battery-=1
    
    def divisao(self, num: float, den:float):
        if self.battery==0:
            print("fail: bateria insuficiente")
        elif den==0:
            print("fail: divisao por zero")
            self.battery -=1
        else:
            self.display = num/den
            self.battery -=1
def main():
    calculator= Calculator(0)
    while True :
        line= input()
        print(f"${line}")
        args= line.split()
        if args[0]=="end":
            break
        elif args[0]=="init":
            increment=int(args[1])
            calculator=Calculator(increment)
        elif args[0]=="show":
            print(calculator)
        elif args[0]=="charge":
            increment=int(args[1])
            calculator.recarregar(increment)
        elif args[0]=="sum":
            a=int(args[1])
            b=int(args[2])
            calculator.somar(a,b)
        elif args[0]=="div":
            a=float(args[1])
            b= float(args[2])
            calculator.divisao(a,b)


main()