from users import User
from encomenda import Cartas, Encomendas
import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()


controladorEtapas = 0
user = User()
cartas = Cartas()

while True:
    match controladorEtapas:
        case 0:
            #SISTEMA DE LOGIN/REGISTRAR
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
            #SELETOR DO TIPO DA CONTA (ADM OU NÃO)
            cursor.execute("SELECT status FROM user WHERE cpf = {}".format(user.cpf))
            if (cursor.fetchall() == [(1,)]):
                controladorEtapas = 2
            else:
                controladorEtapas = 3
                    

        case 2:
            #CONTA SEM DIREITOS DE ADMINISTRADOR
            envioAcompanhamento = int(input("Digite 1 para enviar encomenda, e 2 para acompanhar uma encomenda: "))
            if envioAcompanhamento == 1:
                tipoEnvio = int(input("Digite 1 para cartas, e 2 para caixas: ")) 
                if tipoEnvio == 1:
                    cartas.envio()
                elif tipoEnvio == 2:
                    pass
                else: 
                    print("Código Incorreto!")

            elif envioAcompanhamento == 2: #Acompanhar Encomenda
                codigoRast = input("Digite o código de rastreio: ")
                cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
                if (cursor.fetchall() == []):
                    print("Não localizamos nenhuma encomenda!")

            else:
                print("Código incorreto.")
                print("")
                
        case 3:
            print ("ADM")
            break
