import sqlite3
from random import randint

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

class Encomendas():
    def __init__(self, nome, dest, end):
        self.nome = nome
        self.dest = dest
        self.end = end
    def envio(self):
        pass

class Cartas(Encomendas):
    def __init__(self, nome, dest, end):
        super().__init__(nome, dest, end)
    
    def envio(self):

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
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{}','{}', '{}', {} )".format(self.nome, self.dest, self.end, codigoRast, frete, "CARTA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {}\nCusto de Envio: {:.2f}\nCódigo de Rastreio: {}".format(self.dest, self.end, frete, codigoRast))
        print("")

class Caixas(Encomendas):
    def __init__(self, nome, dest, end):
        super().__init__(nome, dest, end)
    def envio(self):
        comprimento = float(input("Digite o comprimento da caixa (cm): "))
        altura = float(input("Digite a altura da caixa(cm): "))
        largura = float(input("Digite a largura da caixa(cm): "))
        frete = (comprimento * largura * altura / 6000) * 100 
        codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(codigoRast))
        while (cursor.fetchall() != []):
            codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{}','{}', '{}', {} )".format(self.nome, self.dest, self.end, codigoRast, frete, "CAIXA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {}\nCusto de Envio: {:.2f}\nCódigo de Rastreio: {}".format(self.dest, self.end, self.frete, codigoRast))
        print("")
