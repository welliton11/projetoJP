n1= int(input('Digite o número que deseja ver a tabuada: '))
inicio= int(input('Começar a tabuada em qual número? '))
fim= int(input('Terminar a tabuada em qual número? '))

if inicio > fim:
    print('A tabuada não pode começar com um número menor que o fim dela.')

for i in range(inicio,fim+1):
    print(i*n1)