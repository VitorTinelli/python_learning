from users import User
from encomenda import Cartas, Caixas, Encomendas
import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()


controladorEtapas = 0
user = User()
cartas = Cartas()
caixas = Caixas()

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
                    caixas.envio()
                else: 
                    print("Código Incorreto!")

            elif envioAcompanhamento == 2: #Acompanhar Encomenda
                codigoRast = input("Digite o código de rastreio: ")
                cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
                if (cursor.fetchall() == []):
                    print("Não localizamos nenhuma encomenda!")
                else:
                    print("Encomenda localizada: ")

                    cursor.execute("SELECT endereco from encomendas where codRastreio = '{}'".format(codigoRast))
                    print("Endereço de envio: " + str(cursor.fetchone()))

                    cursor.execute("SELECT statusT from encomendas where codRastreio = '{}'".format(codigoRast))
                    print("Status: " + str(cursor.fetchone()))
                    print("")

            else:
                print("Código incorreto.")
                print("")
                
        case 3:
            envioAcompanhamento = int(input("Digite 1 para enviar encomenda, 2 para acompanhar uma encomenda, e 3 para alterar o status de uma encomenda: "))

            if envioAcompanhamento == 1: ##
                tipoEnvio = int(input("Digite 1 para cartas, e 2 para caixas: ")) 
                if tipoEnvio == 1:
                    cartas.envio()
                elif tipoEnvio == 2:
                    caixas.envio()
                else: 
                    print("Código Incorreto!")

            elif envioAcompanhamento == 2: #Acompanhar Encomenda
                codigoRast = input("Digite o código de rastreio: ")
                cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
                if (cursor.fetchall() == []):
                    print("Não localizamos nenhuma encomenda!")
                else:
                    print("Encomenda localizada: ")

                    cursor.execute("SELECT endereco from encomendas where codRastreio = '{}'".format(codigoRast))
                    print("Endereço de envio: " + str(cursor.fetchone()))

                    cursor.execute("SELECT statusT from encomendas where codRastreio = '{}'".format(codigoRast))
                    print("Status: " + str(cursor.fetchone()))
                    print("")

            elif envioAcompanhamento == 3:
                cursor.execute("SELECT codRastreio from encomendas")
                print(cursor.fetchall())

                codigoRast = input("Digite o código de rastreio da mercadoria: ")
                cursor.execute("SELECT statusI FROM encomendas WHERE codRastreio = '{}'".format(codigoRast))
                match cursor.fetchall():
                    case [(0,)]:
                        cursor.execute("UPDATE encomendas SET statusI = {}, statusT = '{}' where codRastreio = '{}'".format(1, "ENCOMENDA EM ROTA DE ENTREGA", codigoRast))
                        banco.commit()
                        print("ENCOMENDA ATUALIZADA: \nNovo status: ENCOMENDA EM ROTA DE ENTREGA")
                
                    case [(1,)]:
                        cursor.execute("UPDATE encomendas SET statusI = {}, statusT = '{}' where codRastreio = '{}'".format(2, "ENCOMENDA ENTREGUE", codigoRast))
                        banco.commit()
                        print("ENCOMENDA ATUALIZADA: \nNovo status: ENCOMENDA ENTREGUE")
                    
                    case [(2,)]:
                        print("MERCADORIA JÁ EM POSSE DO DESTINATÁRIO")
                    
            else:
                print("Código incorreto.")
                print("")
