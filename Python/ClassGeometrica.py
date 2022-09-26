from abc import ABC, abstractmethod
import math

class Geometrica(ABC):
    @abstractmethod
    def perimetro():
        pass
    def area():
        pass
class Quadrado(Geometrica):
    def __init__(self, number_1, number_2, number_3, number_4):
        self.n1 = number_1
        self.n2 = number_2
        self.n3 = number_3
        self.n4 = number_4
    def perimetro(self):
        print(f'Perimetro: {self.n1+self.n2+self.n3+self.n4}')
    def area(self):
        print(f'Area: {self.n1*self.n2}')

class Triangulo(Geometrica):
    def __init__(self, number_1, number_2, number_3):
        self.n1 = number_1
        self.n2 = number_2
        self.n3 = number_3
    def perimetro(self):
        self.total_p = self.n1+self.n2+self.n3
        print(f'Perimetro: {self.total_p}')
    def area(self):
        alt = self.total_p / 2
        base = math.sqrt(alt*(alt-self.n1)*(alt-self.n2)*(alt-self.n3))
        print(f'Area: {(base*alt)/2}')

class Circulo:
    def __init__(self, raio_do_circulo):
        self.n1 = raio_do_circulo
    def perimetro(self):
        self.total_p = 2*3.14*self.n1
        print(f'Perimetro: {self.total_p}')
    def area(self):
        self.a = 3.14*(self.n1**2)
        print(f'Area: {self.a}')

class Pentagono:
    def __init__(self, number_1, number_2, number_3, number_4, number_5):
        self.n1 = number_1
        self.n2 = number_2
        self.n3 = number_3
        self.n4 = number_4
        self.n5 = number_5
    def perimetro(self):
        print(f'Perimetro: {self.n1+self.n2+self.n3+self.n4+self.n5}')
    def area(self):
        print(f'Area: {(self.n1*3)/2}')

q = Quadrado(5,5,5,5)
t = Triangulo(7,9,3)
c = Circulo(10)
p = Pentagono(7,7,7,7,7)

q.perimetro()
q.area()
t.perimetro()
t.area()
c.perimetro()
c.area()
p.perimetro()
p.area()