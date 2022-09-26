while True:
    print('\nOPERAÇÕES: \n Soma:(+)  Subtração:(-)  Divisão:(/)  Multiplicação:(*) \n')
    n1= float(input('Digite um número: '))
    forma= input('Digite agora a operação desejada:')
    n2= float(input('Digite o segundo número: '))


    if forma == '+':
        print(n1+n2)
        loop= input('Deseja usar novamente? S ou N. ').lower()
        if loop == 'n':
            break

    elif forma == '-':
        print(n1-n2)
        loop= input('Deseja usar novamente? S ou N. ').lower()
        if loop == 'n':
            break

    elif forma == '/':
        print(n1/n2)
        loop= input('Deseja usar novamente? S ou N. ').lower()
        if loop == 'n':
            break

    elif forma == '*':
        print(n1*n2)
        loop= input('Deseja usar novamente? S ou N. ').lower()
        if loop == 'n':
            break

    else:
        print('Valor inválido')

#eval(f' {n1}{expressao}{n2}')
#print(f'O resultado de {n1}{expressao}{n2} é igual a {resultado}')