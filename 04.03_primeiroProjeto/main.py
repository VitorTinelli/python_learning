from users import User
import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()


controladorEtapas = 0;
user = User()


while True:
    match controladorEtapas:
        case 0:
            logregister = int(input("Digite 1 para registrar-se, e 2 para logar: "))
            if logregister == 1:
                user.registrar()
            elif logregister == 2:
                if user.login() >= 1:
                    controladorEtapas = 1
                else:
                    print("")
            else:
                print("Código incorreto.")
                print("")
                
            

        case 1:
            cursor.execute("SELECT status FROM user WHERE cpf = {}".format(user.cpf))
            if (cursor.fetchall() == [(1,)]):
                controladorEtapas = 2
            else:
                controladorEtapas = 3
                    

        case 2:
            print("Não ADMIN")
            break
        case 3:
            print ("ADM")
            break
