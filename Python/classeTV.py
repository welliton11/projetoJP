class Tv:
    def __init__(self) -> None:
        self.canal = 12
        self.volume = 10
    
    def statusDaTv(self):
        print(f'Canal {self.canal} \nVolume {self.volume}\n')

    def mudarCanais(self, novoCanal):
        if novoCanal==4 or novoCanal==7 or novoCanal==9 or novoCanal==12 or novoCanal==41 or novoCanal==45:
            self.canal = novoCanal
        else:
            print('Canal indisponível\n')
    def aumentarVolume(self, novoVolume):
        if (self.volume+novoVolume) > 30:
            print('Volume máximo\n')
            self.volume = 30
        else:    
            self.volume += novoVolume
    def diminuirVolume(self, novoVolume):
        if (self.volume+novoVolume) < 0:
            print('Mudo\n')
            self.volume = 0
        else:    
            self.volume -= novoVolume

'''x1 = Tv()

x1.statusDaTv()
x1.aumentarVolume(15)
x1.mudarCanais(4)
x1.statusDaTv()
x1.aumentarVolume(30)
x1.mudarCanais(5)
x1.statusDaTv()'''