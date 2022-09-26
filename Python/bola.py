class Bola:
    def __init__(self, cor, material, circunferencia) -> None:
        self.cor = cor
        self.material = material
        self.circun = circunferencia
    def trocaCor(self, corNova):
        self.cor = corNova
    def mostrarCor(self):
        print(self.cor)

'''
bola1 = Bola('vermelha', 'borracha', 35)
bola2 = Bola('amarela', 'couro', 20)

bola1.mostrarCor()
bola2.mostrarCor()
bola2.trocaCor('roxa')
bola1.trocaCor('azul')
bola1.mostrarCor()
bola2.mostrarCor()'''