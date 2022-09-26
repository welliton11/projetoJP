from operator import truediv


x = True

while x == True:

    usuario = input('Usuário:')
    senha = input('Senha:')

    if usuario == 'joaquim' and senha == '1234':
        print('Acesso autorizado.')
        x = False
    else:
        print('Acesso negado.')