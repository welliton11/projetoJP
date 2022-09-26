class Retangulo:
    def __init__(self, comprimento, largura) -> None:
        self.ladoA = comprimento
        self.ladoB = largura
    def mudarValor(self, comprimento, largura):
        self.ladoA = comprimento
        self.ladoB = largura
    def retornaValor(self):
        print(self.ladoA, 'e', self.ladoB)
    def calcularArea(self):
        print(self.ladoA*self.ladoB)
    def calcularPerimetro(self):
        print((self.ladoA*2)+(self.ladoB*2))
        return (self.ladoA*2)+(self.ladoB*2)

'''ret1 = Retangulo(7, 3)

ret1.retornaValor()
ret1.calcularArea()
ret1.calcularPerimetro()
ret1.mudarValor(8, 5)
ret1.retornaValor()
ret1.calcularArea()
ret1.calcularPerimetro()'''