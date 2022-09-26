class Quadrado:
    def __init__(self, tamanhoLado) -> None:
        self.tamanho = tamanhoLado
    def mudarTamanho(self, novoTamanho):
        self.tamanho = novoTamanho
    def retornaTamanho(self):
        print(self.tamanho)
    def calcularArea(self):
        print(self.tamanho**2)

'''quadrado1 = Quadrado(8)

quadrado1.retornaTamanho()
quadrado1.calcularArea()
quadrado1.mudarTamanho(20)
quadrado1.retornaTamanho()
quadrado1.calcularArea()'''