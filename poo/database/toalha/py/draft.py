#a: int = 5
#b: float = 6.4
#c: str = "jss"
#d: bool = True
class Towel:
    def __init__(self, color: str, size: str): #construtor
        self.color: str= color
        self.size: str= size
        self.wetness: int= 0
#referencias
print("Qual a cor da sua toalha e o tamanho?")
color = input() 
size = input()
towel: Towel= Towel(color, size) #objeto
print(f"Sua toalha é {towel}")