import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE encomendasNacional (remetente text, destinatario text, endereco text, codRastreio text, statusT text, statusI integer)")
cursor.execute("INSERT INTO user VALUES('Pedro Morona', 'José Tinelli', 'Rua Walter Palmeirinhas, 98 - Jardim Angélica - Criciuma/SC', 'BR1045BR', 'RECEBIDO NA AGÊNCIA DOS CORREIOS', 0  )")

banco.commit()