import sqlite3
import random

conexao = sqlite3.connect('assinatura_de_produto.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS assinantes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'meses INTEGER'
')')

# lista = ['Renata','Bruno','Patricia','Carol','Evilin','João','Leticia','Erica','Marcio','Maria','Giovanna','Rafael','Fátima','Cleber','Henrique']
# for j in range(0, 100):
#     pp = random.choice(lista)
#     cc = random.randint(0, 24)
#     cursor.execute(f'INSERT INTO assinantes (nome, meses) VALUES("{pp}",{cc}) ')
#     conexao.commit()

# cursor.execute('INSERT INTO assinantes (nome, meses) VALUES("Henrique", 1) ')
cursor.execute('SELECT * FROM assinantes')
# cursor.execute('DELETE FROM assinantes WHERE meses >=12')
conexao.commit()

for l in cursor.fetchall():
    identi, nome,meses = l
    print(f'\n\033[33m{identi}. Nome: {nome} \n    Meses: {meses}\033[m')

cursor.close()
conexao.close()