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
        self.__frete = 0
        
        if peso <= 20:
            self.frete = 2.50
        elif peso <= 100:
            self.__frete = 5.00
        elif peso <= 200:
            self.__frete = 8
        elif peso <= 400:
            self.__frete = 12.50
        else:
            self.__frete = peso*0.04
        self.__codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(self.__codigoRast))
        while (cursor.fetchall() != []):
            self.__codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{}','{}', '{}', {} )".format(self.nome, self.dest, self.end, self.__codigoRast, self.__frete, "CARTA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {}\nCusto de Envio: {:.2f}\nCódigo de Rastreio: {}".format(self.dest, self.end, self.__frete, self.__codigoRast))
        print("")

    @property
    def frete(self):
        return self.__frete
        
    @frete.setter
    def frete(self, a):
        raise ValueError("Impossivel alterar o frete manualmente!")
    
    @property
    def codigoRast(self):
        return self.__codigoRast
        
    @codigoRast.setter
    def codigoRast(self, a):
        raise ValueError("Impossivel alterar o codigoRast manualmente!")

class Caixas(Encomendas):
    def __init__(self, nome, dest, end):
        super().__init__(nome, dest, end)
    def envio(self):
        comprimento = float(input("Digite o comprimento da caixa (cm): "))
        altura = float(input("Digite a altura da caixa(cm): "))
        largura = float(input("Digite a largura da caixa(cm): "))
        self.__frete = (comprimento * largura * altura / 6000) * 100
         
        self.__codigoRast = "NL" + str(randint(1000, 9999)) + "BR"

        cursor.execute("SELECT codRastreio from encomendas where codRastreio = '{}'".format(self.__codigoRast))
        while (cursor.fetchall() != []):
            self.__codigoRast = "NL" + str(randint(1000, 9999)) + "BR"
        cursor.execute("INSERT INTO encomendas VALUES('{}', '{}', '{}', '{}','{}','{}', '{}', {} )".format(self.nome, self.dest, self.end, self.__codigoRast, self.__frete, "CAIXA" ,"RECEBIDO NA AGÊNCIA DOS CORREIOS", 0))
        banco.commit()
        print("Encomenda enviada com sucesso!\nDestinatário: {}\nEndereço: {}\nCusto de Envio: {:.2f}\nCódigo de Rastreio: {}".format(self.dest, self.end, self.__frete, self.__codigoRast))
        print("")

    @property
    def frete(self):
        return self.__frete
        
    @frete.setter
    def frete(self, a):
        raise ValueError("Impossivel alterar o frete manualmente!")
    
    @property
    def codigoRast(self):
        return self.__codigoRast
        
    @codigoRast.setter
    def codigoRast(self, a):
        raise ValueError("Impossivel alterar o codigoRast manualmente!")

