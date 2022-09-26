a = 0
soma = 0
while a < 10:
    n1 = int(input('Digite um número: '))
    
    if n1 < 0:
        soma += n1
    a += 1

print(soma)