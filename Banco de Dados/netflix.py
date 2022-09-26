import sqlite3

conexao = sqlite3.connect('netflixBD.db')
cursor = conexao.cursor()

email = input('Email: ')
senha = input('Senha: ')
cursor.execute(f'INSERT INTO conta (email, senha) VALUES("{email}", "{senha}") ')
cursor.execute('SELECT * FROM conta')
conexao.commit()
print('Conta criada! \nAgora faça seu perfil.\n')

email_conta = input('Confirme o email ao qual deseja criar o perfil. \nEmail: ')
while email_conta != email:
    print('Email errado!')
    email_conta = input('Confirme o email ao qual deseja criar o perfil. \nEmail: ')
if email_conta == email:
    nome = input('Nome: ')
    imagem = input('Imagem: ')
    cursor.execute(f'INSERT INTO perfis (nome, imagem, email_conta) VALUES("{nome}", "{imagem}", "{email_conta}") ')
    cursor.execute('SELECT * FROM perfis')
    conexao.commit()
    a = input('Perfil criado! \nDeseja criar outro perfil? (s ou n)\n').lower()
    if a == 's':
        nome2 = input('Nome: ')
        imagem2 = input('Imagem: ')
        cursor.execute(f'INSERT INTO perfis (nome, imagem, email_conta, nome2, imagem2) VALUES("{nome}", "{imagem}", "{email_conta}", "{nome2}", "{imagem2}") ')
        cursor.execute('SELECT * FROM perfis')
        conexao.commit()
b = True
while b:
    navegar = int(input('\033[31m\nNETFLIX:\033[m \n1.Informações da conta \n2.Atualizar senha \n3.Excluir conta \n4.Sair \n\nDigite o número da opção desejada: '))
    match navegar:
        case 1:
            if a == 's':
                for i in cursor.fetchall():
                    nome,imagem,email,nome2,imagem2 = i
                    print(f'\n\033[33mConta:\033[m \nEmail: {email} \nSenha: ****') 
                    print(f'\033[33mPerfis:\033[m \nNome: {nome}        │Nome: {nome2} \nImagem: {imagem}        │Imagem: {imagem2}\n')
            else:
                for i in cursor.fetchall():
                    nome,imagem,email = i
                    print(f'\n\033[33mConta:\033[m \nEmail: {email} \nSenha: ****') 
                    print(f'\033[33mPerfis:\033[m \nNome: {nome} \nImagem: {imagem}')
        case 2:
            nova_senha = input('Digite a nova senha: ')
            cursor.execute(f'UPDATE conta SET senha = ? WHERE email = "{email}"', (nova_senha,))
            conexao.commit()
        case 3:
            apagar = input('Digite o email da conta que você deseja apagar: ')
            cursor.execute('DELETE FROM conta WHERE email = ?', (apagar,))
            cursor.execute('DELETE FROM perfis WHERE email_conta = ?', (apagar,))
            conexao.commit()
            print('Conta excluída.')
            b = False
        case 4:
            b = False
cursor.close
conexao.close