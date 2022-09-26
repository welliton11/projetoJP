while True:
    conta = float(input('Qual o valor da prestação?\n'))
    if conta < 0:
        print('Valor inválido.')
        continue

    elif conta == 0:
        break

    def pagamento(x):
        x = 'Valor a ser pago é igual a'
        multa = 3/100
        dias_atrasados = 0.1/100

        atraso = input(('Sua prestação está atrasada? (s ou n)\n')).upper()
        if atraso == 'S':
            dias = int(input('Quantos dias de atraso?\n'))
        
    
        if atraso == 'S':
            a = conta * multa
            b = conta * (dias * dias_atrasados)
            resultado = conta + a + b
            print(x, resultado)

        if atraso == 'N':
            print(x, conta)

    pagamento(conta)