a= int(input('Digite o valor de a: '))

if a == 0:
    print('Não é uma equação do segundo grau.')

else:
    b= int(input('Digite o valor do b: '))
    c= int(input('Digite o valor do c: '))

    delta= ((b * b) - 4 * a * c)

    if delta < 0:
        print('A equação não possui raízes.')

    if delta == 0:
        print('A equação possui apenas uma raiz.')

    if delta > 0:
        print('A equação possui 2 raízes.')

    raiz1= (-b+delta**(1/2)) / (2*a)
    raiz2= (-b-delta**(1/2)) / (2*a)

    print(raiz1)
    print(raiz2)