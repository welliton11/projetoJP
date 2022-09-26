def sorte():
    import random

    num = random.randint(2, 12)
    print(num)

    if num == 7 or num == 11:
        print('Que sorte, você ganhou!!!')

    elif num == 2 or num == 3 or num == 12:
        print('Craps, você perdeu!')

    elif num==4 or num==5 or num==6 or num==8 or num==9 or num==10:
        print('Ponto')
#=======/========/=======/======/=======
        while True:
    
            import random

            num2 = random.randint(2, 12)
            print(num2)

            if num2 == 7:
                print('Craps, você perdeu!')
                break

            elif num == num2:
                print('Você ganhou!')
                break

sorte()