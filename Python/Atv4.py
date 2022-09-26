s = float(input('Qual seu salário mensal? '))

if s < 280:
    print('Com o reajuste seu salário agora é:', (s*20/100+s))
if s >= 280 and s < 700:
    print('Com o reajuste seu salário agora é:', (s*15/100+s))
if s >= 700 and s < 1500:
    print('Com o reajuste seu salário agora é:', (s*10/100+s))
if s >= 1500:
    print('Com o reajuste seu salário agora é:', (s*5/100+s))

print('Salário antes do reajuste era: ', (s))

if s < 280:
    print('O percentual de aumento aplicado foi 20%.\n Seu novo salario é:', (s*20/100+s))
if s >= 280 and s < 700:
    print('O percentual de aumento aplicado foi 15%.\n Seu novo salario é:', (s*15/100+s))
if s >= 700 and s < 1500:
    print('O percentual de aumento aplicado foi 10%.\n Seu novo salario é:', (s*10/100+s))
if s >= 1500:
    print('O percentual de aumento aplicado foi 5%.\n Seu novo salario é:', (s*5/100+s))