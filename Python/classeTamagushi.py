import random

class Tamagushi:
    def __init__(self, Nome, Idade) -> None:
        self.nome = Nome
        self.fome = 70
        self.saude = 70
        self.idade = Idade
    def status(self):
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'idade: {self.idade}\n')
    def alterarNome(self, novoNome):
        self.nome = novoNome
        self.fome = self.fome-40
        self.saude = self.saude-35
        print('Ele não gosta de trocar seu nome.\n')
        print('Nome: ', self.nome)
        print('Fome: ', self.fome)
        print('Saúde: ', self.saude)
        print('idade: ', self.idade, '\n')
        if (self.fome+self.saude)>=180:
            print('Humor: ᕙ(`▿´)ᕗ\n')
        elif (self.fome+self.saude)>=140 and (self.fome+self.saude)<=180:
            print('Humor: (◠▿◠)\n')
        elif (self.fome+self.saude)>=80 and (self.fome+self.saude)<=140:
            print('Humor: (ㆆ_ㆆ)\n ')
        elif (self.fome+self.saude)>=50 and (self.fome+self.saude)<=80:
            print('Humor: /╯﹏╰\ \n')
        elif (self.fome+self.saude)>=20 and (self.fome+self.saude)<=50:
            print('Humor: (╥_╥)\n')
        elif (self.fome+self.saude)>=2 and (self.fome+self.saude)<=20:
            print('Humor: (x︵x)\n')
        elif (self.fome+self.saude)<2 or self.fome==0 or self.saude==0:
            print(f'Você deixou {self.nome} morrer.\n')
            del self.nome
            del self.fome
            del self.saude
            del self.idade
    def alterarFome(self, novaFome):
        if novaFome <= 0:
            novaFome = 0
            print('Você só pode dar comida a ele.\n')
        self.fome = novaFome
        if self.fome>100:
            self.fome = 100
            print(self.nome, 'comeu demais, não dê mais comida a ele.\n')
        print('Nome: ', self.nome)
        print('Fome: ', self.fome)
        print('Saúde: ', self.saude)
        print('idade: ', self.idade, '\n')
        if (self.fome+self.saude)>=180:
            print('Humor: ᕙ(`▿´)ᕗ\n')
        elif (self.fome+self.saude)>=140 and (self.fome+self.saude)<=180:
            print('Humor: (◠▿◠)\n')
        elif (self.fome+self.saude)>=80 and (self.fome+self.saude)<=140:
            print('Humor: (ㆆ_ㆆ)\n ')
        elif (self.fome+self.saude)>=50 and (self.fome+self.saude)<=80:
            print('Humor: /╯﹏╰\ \n')
        elif (self.fome+self.saude)>=20 and (self.fome+self.saude)<=50:
            print('Humor: (╥_╥)\n')
        elif (self.fome+self.saude)>=2 and (self.fome+self.saude)<=20:
            print('Humor: (x︵x)\n')
        elif (self.fome+self.saude)<2 or self.fome==0 or self.saude==0:
            print(f'Você deixou {self.nome} morrer.\n')
            del self.nome
            del self.fome
            del self.saude
            del self.idade
    def brincar(self):
        lista = ['boliche', 'caça ao tesouro', 'vôlei', 'futebol', 'skate', 'pega-pega', 'basquete', 'pipa', 'esconde-esconde']
        al = random.choice(lista)
        self.fome = self.fome+20
        self.saude = self.saude+40
        if self.fome>100:
            self.fome = 100
        if self.saude>100:
            self.saude = 100
        print(f'O {self.nome} adorou brincar de {al}.\n')
        print('Nome: ', self.nome)
        print('Fome: ', self.fome)
        print('Saúde: ', self.saude)
        print('idade: ', self.idade,'\n')
        if (self.fome+self.saude)>=180:
            print('Humor: ᕙ(`▿´)ᕗ\n')
        elif (self.fome+self.saude)>=140 and (self.fome+self.saude)<=180:
            print('Humor: (◠▿◠)\n')
        elif (self.fome+self.saude)>=80 and (self.fome+self.saude)<=140:
            print('Humor: (ㆆ_ㆆ)\n ')
        elif (self.fome+self.saude)>=50 and (self.fome+self.saude)<=80:
            print('Humor: /╯﹏╰\ \n')
        elif (self.fome+self.saude)>=20 and (self.fome+self.saude)<=50:
            print('Humor: (╥_╥)\n')
        elif (self.fome+self.saude)>=2 and (self.fome+self.saude)<=20:
            print('Humor: (x︵x)\n')
        elif (self.fome+self.saude)<2 or self.fome==0 or self.saude==0:
            print(f'Você deixou {self.nome} morrer.\n')
            del self.nome
            del self.fome
            del self.saude
            del self.idade
    def alterarSaude(self, novaSaude):
        if novaSaude <= 0:
            novaSaude = 0
            print('Você não pode tirar a saúde dele dessa forma.\n')
        self.saude = novaSaude
        self.fome = self.fome-10
        if self.saude>100:
            self.saude = 100
            print(self.nome, 'está com a saúde no máximo.\n')
        print('Nome: ', self.nome)
        print('Fome: ', self.fome)
        print('Saúde: ', self.saude)
        print('idade: ', self.idade,'\n')

        if (self.fome+self.saude)>=180:
            print('Humor: ᕙ(`▿´)ᕗ\n')
        elif (self.fome+self.saude)>=140 and (self.fome+self.saude)<=180:
            print('Humor: (◠▿◠)\n')
        elif (self.fome+self.saude)>=80 and (self.fome+self.saude)<=140:
            print('Humor: (ㆆ_ㆆ)\n ')
        elif (self.fome+self.saude)>=50 and (self.fome+self.saude)<=80:
            print('Humor: /╯﹏╰\ \n')
        elif (self.fome+self.saude)>=20 and (self.fome+self.saude)<=50:
            print('Humor: (╥_╥)\n')
        elif (self.fome+self.saude)>=2 and (self.fome+self.saude)<=20:
            print('Humor: (x︵x)\n')
        elif (self.fome+self.saude)<2 or self.fome==0 or self.saude==0:
            print(f'Você deixou {self.nome} morrer.\n')
            del self.nome
            del self.fome
            del self.saude
            del self.idade
    def alterarIdade(self, novaIdade):
        self.idade = novaIdade
        self.fome = self.fome-35
        self.saude = self.saude-25
        print('Ele não gosta de ficar mais velho.\n')
        print('Nome: ', self.nome)
        print('Fome: ', self.fome)
        print('Saúde: ', self.saude)
        print('idade: ', self.idade,'\n')
        if (self.fome+self.saude)>=180:
            print('Humor: ᕙ(`▿´)ᕗ\n')
        elif (self.fome+self.saude)>=140 and (self.fome+self.saude)<=180:
            print('Humor: (◠▿◠)\n')
        elif (self.fome+self.saude)>=80 and (self.fome+self.saude)<=140:
            print('Humor: (ㆆ_ㆆ)\n ')
        elif (self.fome+self.saude)>=50 and (self.fome+self.saude)<=80:
            print('Humor: /╯﹏╰\ \n')
        elif (self.fome+self.saude)>=20 and (self.fome+self.saude)<=50:
            print('Humor: (╥_╥)\n')
        elif (self.fome+self.saude)>=2 and (self.fome+self.saude)<=20:
            print('Humor: (x︵x)\n')
        elif (self.fome+self.saude)<2 or self.fome==0 or self.saude==0:
            print(f'{self.nome} morreu.\n')
            del self.nome
            del self.fome
            del self.saude
            del self.idade

a = Tamagushi('Pou', 1)
a.status()
a.alterarNome('pikachu')
a.alterarSaude(2)
a.brincar()
a.alterarFome(2)
a.alterarNome('pedro')
a.status()