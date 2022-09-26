class Pessoa:
    def __init__(self, Nome = None) -> None:
        self.__nome = Nome
        self.__vida = 50
        self.__energia = 50
        self.__mana = 50
        self.__fome = 50
    @property
    def nome(self):
        return self.__nome
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, valor):
        self.__vida = valor
    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self, valor):
        self.__energia = valor
    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self, valor):
        self.__mana = valor
    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self, valor):
        self.__fome = valor

    def Comer(self):
        self.__fome = self.__fome + 50
        self.__vida = self.__vida + 10
        self.__energia = self.__energia + 5
        self.__mana = self.__mana + 5

    def Correr(self):
        self.__energia = self.__energia - 50
        self.__fome = self.__fome - 40
        self.__vida = self.__vida + 20

    def Dormir(self):
        self.__fome = self.__fome - 35
        self.__vida = self.__vida + 30
        self.__energia = self.__energia + 50
        self.__mana = self.__mana + 50

    def Lutar(self):
        if self.__mana >= 80:
            self.__fome = self.__fome - 25
            self.__vida = self.__vida - 20
            self.__energia = self.__energia - 35
            self.__mana = self.__mana - 75
        elif self.__mana >= 40 and self.__mana < 80:
            self.__fome = self.__fome - 30
            self.__vida = self.__vida - 50
            self.__energia = self.__energia - 40
            self.__mana = self.__mana - 60
        elif self.__mana < 40:
            self.__fome = self.__fome - 35
            self.__vida = self.__vida - 75
            self.__energia = self.__energia - 45
            self.__mana = self.__mana - 30

    def VerificarStatus(self):
        if self.vida > 100:
            self.vida = 100
        if self.energia > 100:
            self.energia = 100
        if self.mana > 100:
            self.mana = 100
        if self.fome > 100:
            self.fome = 100
        print(f'Nome: {self.__nome} \nVida: {self.__vida} \nEnergia: {self.__energia} \nMana: {self.__mana} \nFome: {self.__fome}\n ')
        if self.__vida <= 0 or self.__fome <= 0:
            print('Você morreu!!')
            del self.__nome


a = Pessoa('joaquim')
a.Lutar()
a.Lutar()
a.VerificarStatus()