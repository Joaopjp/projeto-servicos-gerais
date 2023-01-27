import mysql.connector
from mysql.connector import errorcode
print("quero ir embora")
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
      CREATE TABLE `funcionarios` (
      `funcionario_id` int(11) NOT NULL AUTO_INCREMENT,
      `funcionario_nome` varchar(255) NOT NULL,
      `funcionario_cargo` varchar(255) NOT NULL,
      `funcionario_email` varchar(255) NOT NULL,
      `funcionario_login` varchar(255) NOT NULL,
      `funcionario_senha` varchar(255) NOT NULL,
      PRIMARY KEY (`funcionario_id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Servicos'] = ('''
      CREATE TABLE `servicos` (
      `servico_id` int(11) NOT NULL AUTO_INCREMENT,
      `servico_nome` varchar(300) NOT NULL,
      PRIMARY KEY (`servico_id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Setor'] = ('''
      CREATE TABLE `setor` (
      `setor_id` int(11) NOT NULL AUTO_INCREMENT,
      `setor_nome` varchar(255) NOT NULL,
      PRIMARY KEY (`setor_id`)
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
funcionarios_sql = 'INSERT INTO funcionarios (funcionario_nome, funcionario_cargo, funcionario_email, ' \
                        'funcionario_login, funcionario_senha) VALUES (%s, %s, %s, %s, %s)'
funcionarios = [
      ("Livia Bueno", "Compras", "livia.bueno@watchguard.com", "lbueno", "livia123"),
      ("João Pedro", "TI", "joaopedro.jesus@watchguard.com", "jjesus", "joao123"),
      ("Michele Fernandes", "Almoxarife", "michele.fernandes@watchguard.com", "mfernandes", "michele123")
]
cursor.executemany(funcionarios_sql, funcionarios)

cursor.execute('select * from servicosgerais.funcionarios')
print(' -------------  Funcionários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo serviços
servicos_sql = 'INSERT INTO servicos (servico_nome) VALUES (%s)'

servicos = [("Limpeza da Cozinha")]

cursor.execute(servicos_sql, servicos)

cursor.execute('select * from servicosgerais.servicos')


print(' -------------  Serviços:  -------------')
for servicos in cursor.fetchall():
    print(servicos[1])


# inserindo setores
setor_sql = 'INSERT INTO setor (setor_nome) VALUES (%s)'
setor = [("TI")]
cursor.execute(setor_sql, setor)

cursor.execute('select * from servicosgerais.setor')
print(' -------------  Setores:  -------------')
for setor in cursor.fetchall():
    print(setor[1])

# commitando se não nada tem efeito
conn.commit()
cursor.close()
conn.close()
