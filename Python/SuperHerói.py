class Humano:
    def __init__(self, Nome, Idade) -> None:
        self.__nome = Nome
        self.__idade = Idade
    @property
    def Nome(self):
        return self.__nome
    @property
    def Idade(self):
        return self.__idade
    def StatusH(self):
        print(f'{self.__nome}, você é Humano e tem {self.__idade} anos.')
#
class Inseto:
    def __init__(self, Nome, Venenoso = False, Alado = False) -> None:
        self.__nome = Nome
        self.__venenoso = Venenoso
        self.__alado = Alado
        match Venenoso:
            case True:
                self.__venenoso = 'é venenoso'
            case False:
                self.__venenoso = 'não é venenoso'
        match Alado:
            case True:
                self.__alado = 'é alado'
            case False:
                self.__alado = 'não é alado'
    @property
    def Nome(self):
        return self.__nome
    @property
    def Venenoso(self):
        return self.__venenoso
    @Venenoso.setter
    def Venenoso(self):
        return self.__venenoso
    @property
    def Alado(self):
        return self.__alado
    @Alado.setter
    def Alado(self):
        return self.__alado
    def StatusI(self):
        print(f'Seu nome é {self.__nome}, você é um inseto, {self.__venenoso} e {self.__alado}.', end=' ')
#
class SuperHeroi(Inseto, Humano):
    def __init__(self, Codinome, Poderes, Venenoso=False, Alado=False) -> None:
        self.__codinome = Codinome
        self.__poderes = Poderes
    @property
    def Codinome(self):
        return self.__codinome
    @property
    def Poderes(self):
        return self.__poderes
    def info(self):
        print(f'Seu poder é {self.__poderes} e seu codinome é: {self.__codinome}.')
    # super().__init__()
    # Humano.__init__(self)
h = Humano('Marcos', 37)
i = Inseto('Louva-a-Deus')
s = SuperHeroi('Capa branca', 'jogar raio')
i.StatusI()
s.info()