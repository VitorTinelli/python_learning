class Veiculo:
    def __init__(self, consumo) -> None:
        self.consumo = consumo
    def adicionar_Gasolina(self):
        pass
    def andar(self):
        pass
    def get_Gasolina(self):
        pass


class Carro(Veiculo):
    def __init__(self, consumo, qtdaComb, distancia) -> None:
        super().__init__(consumo)
        self.qtdaComb = qtdaComb
        self.distancia = distancia
    
    def adicionar_Gasolina(self):
        self.qtdaComb = int(input("Digite a quantidade de gasosa: "))
    
    def andar(self, qtdaComb, consumo, distancia):
        self.__resto = qtdaComb - (consumo*distancia)
        
        @property
        def resto(self):
            return self.__resto
        
        @resto.setter
        def resto(self, b):
            raise ValueError("Você não pode alterar o resto sozinho")

    def get_Gasolina(self):
        print("O restante de combustivel é:", self.__resto,"L")
        