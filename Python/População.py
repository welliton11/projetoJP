anos = 0
a = int(input('Digite a população A: '))
b = int(input('Digite a população B: '))
por_a = float(input('Digite a porcentagem de crescimento da população A: '))
por_b = float(input('Digite a porcentagem de crescimento da população B: '))

while True:
    aporcentagem = a * (por_a/100)
    bporcentagem = b * (por_b/100)
    a+=aporcentagem
    b+=bporcentagem
    anos += 1
    if a >= b:
        print(f'A população A vai demorar {anos} anos para alcançar a população B.')
        break