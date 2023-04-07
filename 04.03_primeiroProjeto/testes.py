import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

# cursor.execute("DELETE FROM user WHERE senha = 'user1' ")
# banco.commit()

cursor.execute("SELECT cpf FROM user WHERE senha = 'soyadmin'")
print(cursor.fetchall())
