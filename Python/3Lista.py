n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)
media = 0

print('Nota 1:', lista[0], '\nNota 2:', lista[1], '\nNota 3:', lista[2], '\nNota 4:', lista[3])
for i in lista:
    media += i
    
total = media / 4
print('Média igual á', float(total))