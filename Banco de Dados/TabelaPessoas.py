import sqlite3

conexao = sqlite3.connect('BaseDeDados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS people('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'idade INTEGER,'
'peso REAL,'
'sexo TEXT,'
'classe_social TEXT'
')')
# nome = input('Nome: ').lower().capitalize()
# idade = input('Idade: ')
# peso = input('Peso: ')
# sexo = input('Sexo: ').lower().capitalize()
# classe_social = input('Classe social: ').lower().capitalize()
# cursor.execute(f'INSERT INTO people (nome, idade, peso, sexo, classe_social) VALUES("{nome}", {idade}, {peso}, "{sexo}", "{classe_social}")')
cursor.execute('UPDATE people SET peso = ? WHERE id =7 or id =13', (60,))
cursor.execute('SELECT * FROM people')
#cursor.execute('SELECT * FROM people WHERE peso >60')
#cursor.execute('SELECT * FROM people WHERE sexo = "Feminino" ')
conexao.commit()
'''print('\033[33mPeople table\033[m')''' # 33m = Cor do texto
#cursor.execute('SELECT * FROM people WHERE peso >60 AND idade >=18 AND sexo = "Feminino" AND classe_social = "Alta" ')
for l in cursor.fetchall():
    # print(l)
    identi, nome,idade,peso,sexo,classe_social = l
    print(f'\n\033[33m{identi}. Nome: {nome}, Idade: {idade}, Peso: {peso}, Sexo: {sexo}, Classe social: {classe_social}\033[m')
cursor.close()
conexao.close()