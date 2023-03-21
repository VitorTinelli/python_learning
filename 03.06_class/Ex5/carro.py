class Carro:
    def __init__(self, consumo, qtdaComb, distancia):
        self.consumo = consumo
        self.qtdaComb = qtdaComb
        self.distancia = distancia
    
    def adicionar_Gasolina(self):
        self.qtdaComb = int(input("Digite a quantidade de gasosa: "))
    
    def andar(self, qtdaComb, consumo, distancia):
        self.resto = qtdaComb - (consumo*distancia)
    
    def get_Gasolina(self):
        print("O restante de combustivel é:", self.resto,"L")
        