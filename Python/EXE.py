from operator import truediv


x = True
while x == True:

    idade = int(input('Qual sua idade?'))

    if idade < 18:
        print('Usuário não pode tirar a carteira.')
    else:
        print('Já pode tirar a carteira, meus parabéns.')
        x = False