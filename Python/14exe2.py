nota1= float(input('Digite sua primeira nota: '))
nota2= float(input('Digite sua segunda nota: '))

media= (nota1+nota2) /2

if media <= 10 and media >= 9:
    conceito = 'A'
    aa = 'APROVADO'

if media < 9 and media >= 7.5:
    conceito = 'B'
    aa = 'APROVADO'

if media < 7.5 and media >= 6:
    conceito = 'C'
    aa = 'APROVADO'

if media < 6 and media >= 4:
    conceito = 'D'
    aa = 'REPROVADO'

if media < 4 and media >= 0:
    conceito = 'E'
    aa = 'REPROVADO'

print(f'NOTAS: {nota1} e {nota2}' )
print('MÉDIA: ', media)
print('CONCEITO: ', conceito)
print(aa)