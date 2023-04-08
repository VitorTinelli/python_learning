import sqlite3
from random import randint

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

# cursor.execute("DELETE FROM user WHERE senha = 'user1' ")
# banco.commit()

# cursor.execute("SELECT cpf FROM user WHERE senha = 'soyadmin'")
# print(cursor.fetchall())

# cursor.execute("CREATE TABLE encomendas (remetente text, destinatario text, endereco text, codRastreio text, frete float, statusT text, statusI integer)")
# cursor.execute("INSERT INTO encomendas VALUES('Pedro Morona', 'José Tinelli', 'Rua Walter Palmeirinhas, 98 - Jardim Angélica - Criciuma/SC', 'BR1045BR', '2.50' ,'RECEBIDO NA AGÊNCIA DOS CORREIOS', 0  )")
# banco.commit() 

# cursor.execute("DROP TABLE encomendasNacional")
# banco.commit() 

