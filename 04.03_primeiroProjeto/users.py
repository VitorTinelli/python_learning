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
        controlerLogin = True
        while controlerLogin == True:
            self.cpf = int(input("Digite seu CPF: "))
            self.senha = input("Digite sua senha: ")
            cursor.execute("SELECT * FROM user WHERE cpf = {} and senha = '{}'".format(self.cpf, self.senha))
            if (cursor.fetchall() == []):
                print ("Usuário ou senha incorretos!")
                print ("")
                tenteNovamente = 10
                while (tenteNovamente != 1 or tenteNovamente != 0):
                        tenteNovamente = int(input("Códigos: \n1 - SIM \n2 - NÃO\nDeseja tentar novamente: "))
                        if tenteNovamente == 1:
                            break
                        elif tenteNovamente == 2:
                            return 0
                        else: 
                            print("Código Incorreto")
                            print("")
            else:
                print ("Logado com sucesso!")
                print("")

                cursor.execute("SELECT status FROM user WHERE cpf = {}".format(self.cpf))
                if (cursor.fetchall() == [(1,)]):
                    controlerLogin = False
                    return 1
                else: 
                    controlerLogin = False
                    return 2
                
        



    def registrar(self):
        controlerRegister = True
        while controlerRegister == True:
            self.cpf = int(input("Digite seu CPF: "))
            self.senha = input("Digite sua senha: ")
            cursor.execute("SELECT cpf FROM user WHERE cpf={}".format(self.cpf))
            if (cursor.fetchall() == []):
                cursor.execute("INSERT INTO user VALUES ({}, '{}', 1)".format(self.cpf, self.senha))
                banco.commit()
                print("Registrado com sucesso!")
                controlerRegister = False
            else: 
                print("CPF JÁ REGISTRADO NO SISTEMA!")
                print("")
                tenteNovamente = 0
                while (tenteNovamente != 1 and tenteNovamente != 2):
                    tenteNovamente = int(input("Códigos: \n1 - SIM \n2 - NÃO\nDeseja tentar novamente: "))
                    if tenteNovamente == 1:
                        break
                    elif tenteNovamente == 2:
                        return
                    else: 
                        print("Código Incorreto")
                        print("")