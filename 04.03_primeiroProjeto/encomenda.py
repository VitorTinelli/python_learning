import sqlite3
from random import randint

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE encomendasNacional (remetente text, destinatario text, endereco text, codRastreio text, frete float, statusT text, statusI integer)")
#cursor.execute("INSERT INTO encomendasNacional VALUES('Pedro Morona', 'José Tinelli', 'Rua Walter Palmeirinhas, 98 - Jardim Angélica - Criciuma/SC', 'BR1045BR', 'RECEBIDO NA AGÊNCIA DOS CORREIOS', 0  )")
#banco.commit() 
class Encomendas():
    def __init__(self):
        frete = 0
    def envio(self):
        pass

class Cartas(Encomendas):
    def __init__(self):
        super().__init__()
    def envio(self):
        nome = input("Digite seu nome: ")
        dest = input("Digite o nome do destinatário: ")
        end = input("Digite o endereço da entrega: ")
        peso = float(input("Digite o peso da carta: "))

        if peso <= 20:
            frete = 2.50
        elif peso <= 100:
            frete = 5.00
        elif peso <= 200:
            frete = 8
        elif peso <= 400:
            frete = 12.50
        else:
            frete = peso*0.04

        codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
        while (cursor.fetchall() != []):
            codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{}', '{}', {} )".format(nome, dest, end, codigoRast, frete, "RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {}\nCusto de Envio: {}\nCódigo de Rastreio: {}".format(dest, end, frete, codigoRast))