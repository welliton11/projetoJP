n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = ((n1+n2)/2)

if m == 10:
    print('Aprovado com distinção.')
elif m >= 7:
    print('Aprovado.')
elif m < 7:
    print('Reprovado.')