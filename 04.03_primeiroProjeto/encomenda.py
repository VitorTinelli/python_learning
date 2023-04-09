import sqlite3
from random import randint

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

class Encomendas():
    def __init__(self):
        pass
    def envio(self):
        pass

class Cartas(Encomendas):
    def __init__(self):
        super().__init__()
    def envio(self):
        nome = input("Digite seu nome: ")
        dest = input("Digite o nome do destinatário: ")
        end = input("Digite o endereço da entrega: ")
        peso = float(input("Digite o peso da carta (em gramas): "))

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
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{:.2f}','{}', '{}', {} )".format(nome, dest, end, codigoRast, frete, "CARTA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {:.2f}\nCusto de Envio: {}\nCódigo de Rastreio: {}".format(dest, end, frete, codigoRast))
        print("")

class Caixas(Encomendas):
    def __init__(self):
        super().__init__()
    def envio(self):
        nome = input("Digite seu nome: ")
        dest = input("Digite o nome do destinatário: ")
        end = input("Digite o endereço da entrega: ")
        comprimento = float(input("Digite o comprimento da caixa (cm): "))
        altura = float(input("Digite a altura da caixa(cm): "))
        largura = float(input("Digite a largura da caixa(cm): "))
        frete = (comprimento * largura * altura / 6000) * 100 
        codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
        while (cursor.fetchall() != []):
            codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{:.2f}','{}', '{}', {} )".format(nome, dest, end, codigoRast, frete, "CAIXA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {:.2f}\nCusto de Envio: {}\nCódigo de Rastreio: {}".format(dest, end, frete, codigoRast))
        print("")
