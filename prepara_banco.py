import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='123456jp'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `servicosgerais`;")

cursor.execute("CREATE DATABASE `servicosgerais`;")

cursor.execute("USE `servicosgerais`;")

# criando tabelas
TABLES = {}
TABLES['Funcionarios'] = ('''
      CREATE TABLE `Funcionarios` (
      `Funcionario_Id` NOT NULL AUTO_INCREMENT,
      `Funcionario_Nome` varchar(255) NOT NULL,
      `Funcionario_Cargo` varchar(40) NOT NULL,
      PRIMARY KEY (`Funcionario_Id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Servicos'] = ('''
      CREATE TABLE `Servicos` (
      `Servico_Id` NOT NULL AUTO_INCREMENT,
      `Servico_Nome` varchar(300) NOT NULL,
      PRIMARY KEY (`Servico_Id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
Funcionarios = 'INSERT INTO Funcionarios (Funcionario_Nome, Funcionario_Cargo) VALUES (%s, %s)'
Funcionarios = [
      ("Livia Bueno", "Livia Bueno", "livia123"),
      ("João Pedro", "JP", "joao123"),
      ("Michele Fernandes", "Michele Fernandes", "michele123")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
