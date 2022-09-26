n1 = int(input('Digite um número: '))
lista = []

def exercicio(n):
    a= 1
    for i in range(n):
        lista.append(a)
        a += 1
        print(lista)
exercicio(n1)