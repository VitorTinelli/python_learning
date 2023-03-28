class FormaGeometrica:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

class Triangulo(FormaGeometrica):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)
        self.__x = [ladoA, ladoB, ladoC]

    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, l):
        raise ValueError("Você não pode trocar o valor manualmente")
               

    def calcular_perimetro(self):
        perimetro = sum(self.__x)
        print("Perimetro do triângulo:",perimetro)

    def get_maior_lado(self):
        self.__x.sort()
        print("Maior lado:",self.__x[2])