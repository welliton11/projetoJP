n1= int(input('Digite um número: '))
n2= int(input('Digite um outro número: '))
n3= int(input('Digite um o último número: '))

if n1 > n2 and n1 > n3:
    print('O', n1, ('é o maior número.'))

if n2 > n1 and n2 > n3:
    print('O', n2, ('é o maior número.'))

if n3 > n2 and n3 > n1:
    print('O', n3, ('é o maior número.'))