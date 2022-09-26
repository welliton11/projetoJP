class Pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def mostrarDados(self):
        print(self.nome, self.idade, self.peso, self.altura)
    def envelhecer(self):
        self.idade += 1
        
    def engordar(self, novoPeso):
        self.peso += novoPeso
    def emagrecer(self, novoPeso):
        self.peso -= novoPeso
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
        else:
            print('Você está velho demais para crescer.')

'''p1 = Pessoa('bruna', 17, 42, 1.57)
p2 = Pessoa('giovana', 20, 70, 1.65)
p3 = Pessoa('matheus', 20, 65, 1.80)
p4 = Pessoa('roberto', 50, 82, 1.70)

p1.envelhecer()
p2.crescer()
p1.mostrarDados()
p2.mostrarDados()'''