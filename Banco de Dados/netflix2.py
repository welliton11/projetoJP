import sqlite3

conexao = sqlite3.connect('netflixBD2.db')
cursor = conexao.cursor()
b = True
while True:
    try:
        interface = int(input('\033[31m\nNETFLIX:\033[m \n\033[;1m1.Crie sua conta \n2.Acesse sua conta \n3.Fechar programa \n\nDigite a opção desejada:\033[m '))
        a = True
        match interface:
            case 1:
                nome = input('\nNome: ')
                email = input('Email: ')
                senha = input('Senha: ')
                if not nome or not email or not senha:
                    print('Você não pode deixar nenhum dos campos em branco!')
                    continue
                
                email2 = input('Confirme seu email para ter acesso ao menu netflix: ')
                while email2 != email:
                    print('\033[1;31mEmail incorreto.\033[m')
                    email2 = input('Confirme seu email para criar um perfil: ')
                cursor.execute(f'INSERT INTO conta (nome, email, senha) VALUES("{nome}", "{email}", "{senha}") ')
                cursor.execute('SELECT * FROM conta')
                conexao.commit()
                print('\033[32mConta criada!\033[m\n\n')
            case 2:
                email = input('\nEmail: ')
                senha = input('Senha: ')
                cursor.execute('SELECT * FROM conta')
                for linha in cursor.fetchall():
                    if linha[1] == email and linha[2] == senha:
                        print('\033[32mConectado\033[m')
                        email2 = input('Confirme seu email para ter acesso ao menu netflix: ')
                        while email2 != email:
                            print('\033[1;31mEmail incorreto.\033[m')
                            email2 = input('Confirme seu email para criar um perfil.')
                        a = False
                    else:
                        continue
                if a == True:
                    print('\033[1;31m\nEmail incorreto, tente novamente.\033[m')
                    continue
            case 3:
                break
    except:
        print('\n\033[1;31mVocê só pode digitar números do 1 ao 3.\033[m')
        continue
    while b == True:
        try:
            inicio = int(input('\n\033[33mINÍCIO:\033[m \n1.Alterar senha \n2.Criar perfil \n3.Alterar nome do perfil \n4.Vizualizar perfis existentes \n5.Acessar perfil \n6.Excluir perfil \n7.Excluir conta \n8.Sair da conta \n\nDigite a opção desejada: \n'))
        except:
            print('\n\033[1;31mVocê só pode digitar números do 1 ao 8.\033[m')
            continue
        match inicio:
            case 1:
                nova_senha = input('Digite a nova senha: ')
                cursor.execute(f'UPDATE conta SET senha = ? WHERE email = "{email}"', (nova_senha,))
                conexao.commit()
                print('\033[32mSenha alterada com sucesso!!\033[m')
            case 2:
                contador = 0
                cursor.execute('SELECT * FROM perfis')
                for linha in cursor.fetchall():
                    contador += 1
                if contador >= 4:
                    print('\033[1;31mVocê não pode ter mais de 4 perfis!\033[m')
                elif contador < 4:
                    perfil = input('\nNome do perfil: ').capitalize()
                    print('\033[32mPerfil criado com sucesso!!\033[m')
                    cursor.execute(f'INSERT INTO perfis (email2, perfil) VALUES("{email}", "{perfil}") ')
                    cursor.execute('SELECT * FROM perfis')
                    conexao.commit()
            case 3:
                contador = 0
                cursor.execute('SELECT * FROM perfis')
                for linha in cursor.fetchall():
                    contador += 1
                if contador == 0:
                    print('\033[1;31mVocê não tem nenhum perfil!\033[m')
                elif contador > 0:
                    cursor.execute('SELECT * FROM perfis')
                    nome_perfil = input('\nDigite o nome do perfil que deseja alterar: ').capitalize()
                    zz = False
                    for linha in cursor.fetchall():
                        if linha[1] == nome_perfil:
                            novo_nome_perfil = input('Digite o novo nome do perfil: ').capitalize()
                            cursor.execute(f'SELECT * FROM perfis WHERE email2 ="{email2}"')
                            cursor.execute(f'UPDATE perfis SET perfil = ? WHERE perfil ="{nome_perfil}" ', (novo_nome_perfil,))
                            print('\033[32mPerfil alterado!\033[m')
                            conexao.commit()
                            zz == True
                    if zz == False:
                        print('\033[1;31mNome de perfil incorreto!\033[m')
            case 4:
                contador = 0
                cursor.execute('SELECT * FROM perfis')
                for linha in cursor.fetchall():
                    contador += 1
                cursor.execute(f'SELECT * FROM perfis WHERE email2 ="{email2}"')
                lista = []
                for linha in cursor.fetchall():
                    if contador == 0:
                        print('\033[1;31mVocê não tem nenhum perfil!\033[m')
                        break
                    lista.append(linha[1])
                if contador == 1:
                    print(f'\nPerfil 1: {lista[0]}')
                if contador == 2:
                    print(f'\nPerfil 1: {lista[0]} \nPerfil 2: {lista[1]}')
                if contador == 3:
                    print(f'\nPerfil 1: {lista[0]} \nPerfil 2: {lista[1]} \nPerfil 3: {lista[2]}')
                if contador == 4:
                    print(f'\nPerfil 1: {lista[0]} \nPerfil 2: {lista[1]} \nPerfil 3: {lista[2]} \nPerfil 4: {lista[3]}')
            case 5:
                perfil2 = input('Digite o nome do perfil que deseja acessar: ').capitalize()
                cursor.execute('SELECT * FROM perfis')
                xxx = False
                for linha in cursor.fetchall():
                    if perfil2 == linha[1]:
                        xxx = True
                if xxx == False:
                    print('O perfil digitado esta incorreto ou não existe!')
                    continue
                while b == True:
                    print(f'\n\033[33mOlá, {perfil2}\033[m')
                    inicio2 = int(input('1.Adicionar filmes aos favoritos \n2.Ver lista de favoritos \n3.Sair do perfil \n\nO que você deseja?\n    '))
                    match inicio2:
                        case 1:
                            filme = input('\nDigite o nome do filme que deseja adicionar aos favoritos: ').capitalize()
                            cursor.execute(f'INSERT INTO filmes (email3, perfil2, filme) VALUES("{email}", "{perfil2}", "{filme}") ')
                            cursor.execute('SELECT * FROM filmes')
                            conexao.commit()
                            print('\n\033[32mFilme Adicionado!\033[m')
                        case 2:
                            contador = 0
                            cursor.execute('SELECT * FROM filmes')
                            for linha in cursor.fetchall():
                                contador += 1
                            if contador == 0:
                                print('Sua lista favoritos está vazia!')
                            elif contador > 0:
                                cursor.execute('SELECT * FROM filmes')
                                favoritos = []
                                for linha in cursor.fetchal():
                                    favoritos.append(linha[2])
                                print(favoritos)
                        case 3:
                            sair_perfil = input('Você tem certeza que deseja sair do perfil? ("s" ou "n"): ').lower()
                            if sair_perfil == 's':
                                break
                            if sair_perfil == 'n':
                                continue
                            else:
                                print('Você só pode digitar "s" ou "n"')
                                continue
            case 6:
                contador = 0
                cursor.execute('SELECT * FROM perfis')
                for linha in cursor.fetchall():
                    contador += 1
                if contador == 0:
                    print('\033[1;31mVocê não tem nenhum perfil para excluir!\033[m')
                    break
                if contador > 0:
                    apagar_perfil = input('Digite o número do perfil que você deseja apagar: ')
                    cursor.execute(f'SELECT * FROM perfis WHERE email2 ="{email2}"')
                    match apagar_perfil:
                        case 1:
                            cursor.execute('DELETE FROM perfis WHERE perfil = ?', (apagar_perfil,))
                        case 2:
                            cursor.execute('DELETE FROM perfis WHERE perfil = ?', (apagar_perfil,))
                        case 3:
                            cursor.execute('DELETE FROM perfis WHERE perfil = ?', (apagar_perfil,))
                        case 4:
                            cursor.execute('DELETE FROM perfis WHERE perfil = ?', (apagar_perfil,))
                    conexao.commit()
                    print('\033[32mPerfil excluído!!\033[m')
            case 7:
                ap = input('Você tem certeza que deseja apagar a conta? (S ou N): ').lower()
                if ap == 's':
                    cursor.execute('DELETE FROM conta WHERE email = ?', (email2,))
                    cursor.execute('DELETE FROM perfis WHERE email2 = ?', (email2,))
                    cursor.execute('DELETE FROM filmes WHERE email3 = ?', (email2,))
                    conexao.commit()
                    print('\033[32mConta excluída!\033[m')
                    break
                if ap == 'n':
                    break
                else:
                    print('\033[1;31mVocê só pode digitar "S" ou "N"!\033[m')
                    continue
            case 8:
                sair_conta = input('Você tem certeza que deseja sair da conta? ("s" ou "n"): ').lower()
                if sair_conta == 's':
                    break
                if sair_conta == 'n':
                    continue
                else:
                    print('Você só pode digitar "s" ou "n"')
                    continue
            case _:
                print('Você digitou errado, você só pode digitar números do 1 ao 8.')