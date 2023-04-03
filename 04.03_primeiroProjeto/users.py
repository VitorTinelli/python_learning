import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

# cursor.execute("CREATE TABLE user (cpf integer, senha text, status integer)")
#cursor.execute("INSERT INTO user VALUES(12118572980,'soyagiota',1)")
#cursor.execute("DELETE FROM user WHERE status = 1")

#banco.commit()

class User():
    def __init__(self):
        pass
    def login(self):
        self.cpf = int(input("Digite seu CPF: "))
        self.senha = input("Digite sua senha: ")
        cursor.execute("SELECT * FROM user WHERE cpf = {} and senha = '{}'".format(self.cpf, self.senha))
        print(cursor.fetchall())
    def registrar(self):
        self.cpf = int(input("Digite seu CPF: "))
        self.senha = input("Digite sua senha: ")
        cursor.execute("SELECT cpf FROM user WHERE cpf={}".format(self.cpf))
        if (cursor.fetchall() == []):
            cursor.execute("INSERT INTO user VALUES ({}, '{}', 1)".format(self.cpf, self.senha))
            banco.commit()
        else: 
            print("CPF JÁ REGISTRADO NO SISTEMA!")

        





