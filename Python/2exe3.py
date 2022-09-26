nome = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')


while nome == senha:
    print('Seu nome de usuário não pode ser igual a senha.')
    nome = input('Digite um nome de usuário: ')
    senha = input('Digite uma senha: ')