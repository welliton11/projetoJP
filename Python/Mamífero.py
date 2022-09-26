class Mamifero():
    def __init__(self, Nome, Peso, Cor) -> None:
        self.nome = Nome
        self.peso = Peso
        self.cor = Cor
    def locomoção(self):
        print(f'O {self.nome} caminha.')
    def comunicação(self):
        print(f'O {self.nome} está se comunicando por latidos com o gato.')
    def alimentação(self):
        print(f'O {self.nome} come ração.')
    def habitat_Natural(self):
        print(f'O {self.nome} vive basicamente em centros urbanos com casas e apartamentos\n.')
class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    def comunicação(self):
        print(f'O {self.nome} está se comunicando por miados com a baleia.')
class Baleia(Mamifero):
    def locomoção(self):
        print(f'A {self.nome} nada.')
    def comunicação(self):
        print(f'a {self.nome} está se comunicando por bufos com o macaco.')
    def alimentação(self):
        print(f'A {self.nome} se alimenta de pequenos animais marinhos')
    def habitat_Natural(self):
        print(f'A {self.nome} vive no mar\n.')
class Macaco(Mamifero):
    def locomoção(self):
        print(f'O {self.nome} pula em galhos.')
    def comunicação(self):
        print(f'O {self.nome} está se comunicando por guinchos com o cachorro.')
    def alimentação(self):
        print(f'O {self.nome} come bananas.')
    def habitat_Natural(self):
        print(f'O {self.nome} vive na selva\n.')

dog = Cachorro('Snopp', '6kg', 'marrom')
cat = Gato('Garfield', '4kg', 'Amarelo')
baleia = Baleia('Free Willy', '500 toneladas', 'Azul')
monkey = Macaco('César', '8kg', 'Preto')
print(dog.__dict__)
dog.locomoção()
dog.comunicação()
dog.alimentação()
dog.habitat_Natural()
print(cat.__dict__)
cat.locomoção()
cat.comunicação()
cat.alimentação()
cat.habitat_Natural()
print(baleia.__dict__)
baleia.locomoção()
baleia.comunicação()
baleia.alimentação()
baleia.habitat_Natural()
print(monkey.__dict__)
monkey.locomoção()
monkey.comunicação()
monkey.alimentação()
monkey.habitat_Natural()

# from abc import ABC, abstractmethod

# class Mamifero(ABC):
#     def __init__(self, Nome, Peso, Cor) -> None:
#         self.nome = Nome
#         self.peso = Peso
#         self.cor = Cor
#     @abstractmethod
#     def locomoção(self):
#         print(f'O {self.nome} caminha.')
#     @abstractmethod
#     def comunicação(self):
#         print(f'O {self.nome} está se comunicando por latidos com o gato.')
#     @abstractmethod
#     def alimentação(self):
#         print(f'O {self.nome} come ração.')
#     @abstractmethod
#     def habitat_Natural(self):
#         print(f'O {self.nome} vive basicamente em centros urbanos com casas e apartamentos\n.')
# class Cachorro(Mamifero):
#     def locomoção(self):
#         return super().locomoção()
#     def comunicação(self):
#         return super().comunicação()
#     def alimentação(self):
#         return super().alimentação()
#     def habitat_Natural(self):
#         return super().habitat_Natural()
# class Gato(Mamifero):
#     def locomoção(self):
#         return super().locomoção()
#     def comunicação(self):
#         print(f'O {self.nome} está se comunicando por miados com a baleia.')
#     def alimentação(self):
#         return super().alimentação()
#     def habitat_Natural(self):
#         return super().habitat_Natural()
# class Baleia(Mamifero):
#     def locomoção(self):
#         print(f'A {self.nome} nada.')
#     def comunicação(self):
#         print(f'a {self.nome} está se comunicando por bufos com o macaco.')
#     def alimentação(self):
#         print(f'A {self.nome} se alimenta de pequenos animais marinhos')
#     def habitat_Natural(self):
#         print(f'A {self.nome} vive no mar\n.')
# class Macaco(Mamifero):
#     def locomoção(self):
#         print(f'O {self.nome} pula em galhos.')
#     def comunicação(self):
#         print(f'O {self.nome} está se comunicando por guinchos com o cachorro.')
#     def alimentação(self):
#         print(f'O {self.nome} come bananas.')
#     def habitat_Natural(self):
#         print(f'O {self.nome} vive na selva\n.')

# dog = Cachorro('Snopp', '6kg', 'marrom')
# cat = Gato('Garfield', '4kg', 'Amarelo')
# baleia = Baleia('Free Willy', '500 toneladas', 'Azul')
# monkey = Macaco('César', '8kg', 'Preto')
# print(dog.__dict__)
# dog.locomoção()
# dog.comunicação()
# dog.alimentação()
# dog.habitat_Natural()
# print(cat.__dict__)
# cat.locomoção()
# cat.comunicação()
# cat.alimentação()
# cat.habitat_Natural()
# print(baleia.__dict__)
# baleia.locomoção()
# baleia.comunicação()
# baleia.alimentação()
# baleia.habitat_Natural()
# print(monkey.__dict__)
# monkey.locomoção()
# monkey.comunicação()
# monkey.alimentação()
# monkey.habitat_Natural()