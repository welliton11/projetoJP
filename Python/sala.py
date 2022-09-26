'''def saudacao(s='Bom dia', nome='Bruno.'):
    print(s, nome)
saudacao()'''
#===============================================================/
'''a= int(input('Digite um número: '))
b= int(input('Digite outro número: '))
c= int(input('Digite mais um número: '))

def numbers(a):
    multiplica = a*b*c
    print(multiplica)
numbers(a)'''
#===============================================================/
'''def num(resultado):
    return    
a= int(input('Digite um número: '))
b= int(input('Digite a porcentagem: '))

porcentagem = a * (b/100)
resultado = a + porcentagem
print(resultado)'''
#===============================================================/
n1 = int(input('Digite um número: '))

def exercicio(n):
    div_3 = n1 % 3
    div_5 = n1 % 5

    if div_3 == 0 and div_5 == 0:
        print('FizzBuzz')
    elif div_3 == 0:
        print("Fizz")
    elif div_5 == 0:
        print('Buzz')
    else:
        print(n1)
exercicio(n1)