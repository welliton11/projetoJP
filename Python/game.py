import random

pc= random.randint(1, 100)

chute= int(input('chute um número:'))
contador= 0


while True:
    if pc > chute:
        chute= int(input('o número digitado é menor, tente novamente:'))
        contador = contador+1
        if contador == 5:
            print('Você perdeu.')
            break

    elif pc < chute:
        chute= int(input('o número digitado é maior, tente novamente:'))
        contador = contador+1
        if contador == 5:
            print('Você perdeu.')
            break
    else:
        print('Parabéns, você ganhou!')
        break