import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS contatos('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'endereço TEXT,'
'numero INTEGER'
')')

class Contatos:
    def __init__(self):
        pass
    def inserirContatos(self,nome,endereço,numero):
        nome = input("Digite numero")
        cursor.execute('INSERT INTO contatos (nome,endereço,numero) VALUES (?,?,?)', (nome,endereço,numero))
        conexao.commit()
    def alterarContatos(self):
        cursor.execute('UPDATE contatos SET nome = ? WHERE numero = 3456',('robson',) )
        cursor.commit()
    def deletarContatos(self):
        cursor.execute('DELETE FROM contatos WHERE numero = 179')
        conexao.commit()
    def visualizadorContatos(self):
        cursor.execute('SELECT nome FROM contatos WHERE nome = "robson"')
        for i in cursor.fetchall():
            print(i)

contato = Contatos()
contato.inserirContatos("robson", 'rua margarida', 111)
contato.visualizadorContatos()
cursor.close()
conexao.close()