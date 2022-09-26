"""
print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A PEDRINHO ELETRONICOS!\033[m \033[m")
print("")
print("VOCE DESEJA REALIZAR SEU CADASTRO OU ENTRAR EM UMA CONTA JÁ CRIADA?")
cad = int(input(1-CADASTRO
2-LOGIN
DIGITE SUA OPÇÃO:))
print("")
match cad:
    case 1:
        nome = str(input("DIGITE SEU NOME: "))
        sexo = str(input("DIGITE SUA ORIENTAÇÃO SEXUAL: "))
        idade = int(input("DIGITE SUA IDADE: "))
        email = input("DIGITE UM EMAIL: ")
        senha = input("DIGITE UMA SENHA: ")
    case 2:
        email = input("DIGITE SEU EMAIL: ")
        senha = input("DIGITE SUA SENHA: ")
print("")
print("SEJA MUITO BEM-VINDO A NOSSA LOJA E FIQUE A VONTADE!")
print("")
print("\033[1;31mCATEGORIAS DE PRODUTOS \033[m")

categorias = int(input(1-ELETRÔNICOS
2-PERIFERICOS
3-JOGOS
QUAL OPÇÃO VOCÊ DESEJA ACESSAR?: ))
print("")
match categorias:
    case 1:
        print("IPHONE 11 | VALOR: R$4000")
        print("IPHONE 12 PRO | VALOR: R$5690")
        print("IPHONE 13 PRO MAX | VALOR: R$7230")
        print("MACBOOK | VALOR: R$27000")
        print("TV SAMSUNG SMART 55 POLEGADAS | VALOR: R$6790")
        print("TV LG SMART 70 POLEGADAS | VALOR: R$9390")
"""


import sqlite3
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

class Login():
    def __init__(self) -> None:
        pass
    def inserirCadastramento(self):
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Login (nome,idade,email,senha) VALUES (?,?,?,?)",(nome,idade,email,senha))
        conexao.commit()
    def entrarLogin(self):
        email = input("Digite o seu email: ")
        senha = input("Digite o seu email: ")
        cursor.execute("INSERT INTO Login (email,senha) VALUES (?,?)",(email,senha))
        conexao.commit()


print("\033[1;0m \033[1;106mOLÁ SEJA BEM VINDO A PEDRINHO ELETRONICOS!\033[m \033[m")
print("")
print("VOCE DESEJA REALIZAR SEU CADASTRO OU ENTRAR EM UMA CONTA JÁ CRIADA?")
cad = int(input("""1-CADASTRO
2-LOGIN
DIGITE SUA OPÇÃO:"""))
print("")
login1 = Login()
match cad:
    case 1:
        login1.inserirCadastramento()
        print("CADASTRO FEITO COM SUCESSO, APROVEITE A NOSSA LOJA.")
    case 2:
        login1.entrarLogin()
print("")
print("CONTA LOGADA COM SUCESSO, BEM-VINDO A NOSSA LOJA.")
print("")
print("SEJA MUITO BEM-VINDO A NOSSA LOJA E FIQUE A VONTADE!")
print("")
print("\033[1;31mCATEGORIAS DE PRODUTOS \033[m")
class Login():
    def __init__(self) -> None:
        pass
    def inserirCadastramento(self):
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        email = input("Digite o seu email: ")
        senha = input("Digite o sua senha: ")
        cursor.execute("INSERT INTO Login (nome,idade,email,senha) VALUES (?,?,?,?)",(nome,idade,email,senha))
        conexao.commit()
    def entrarLogin(self):
        email = input("Digite o seu email: ")
        senha = input("Digite o seu email: ")
        cursor.execute("INSERT INTO Login (email,senha) VALUES (?,?)",(email,senha))
        conexao.commit()
categorias = int(input("""1-ELETRÔNICOS
2-PERIFERICOS
3-JOGOS
QUAL OPÇÃO VOCÊ DESEJA ACESSAR?: """))
print("")
cursor.close()
conexao.close()
