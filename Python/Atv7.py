nome= str(input('Qual seu nome?'))
while len(nome) <= 3:
    print('O nome deve ter mais de 3 caracteres.')
    nome= str(input('Qual seu nome?'))

idade= int(input('Qual sua idade? '))
while idade <= 0 or idade > 70:
    print('Sua idade deve estar entre 0 e 70.')
    idade= int(input('Qual sua idade? '))

salario= float(input('Qual seu salário mensal? '))
while salario <= 0:
    print('O valor digitado deve ser maior que 0.')
    salario= float(input('Qual seu salário mensal? '))

sexo= input('Qual seu sexo? (f ou m) '.lower())
while sexo != "f" and sexo != 'm':
    print('Só pode ser usado f ou m, tente novamente')
    sexo= input('Qual seu sexo? (f ou m) '.lower())

estado_civil= input('Qual seu estado civil? (s, c, v ou d) '.lower())
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Só pode ser usado s; c; v ou d, tente novamente')
    estado_civil= input('Qual seu estado civil? (s, c, v ou d) '.lower())
 
print('Nome:', nome, '\n Idade:', idade, '\n Salário:', salario, '\n Sexo:', sexo, '\n Estado civil:', estado_civil)
