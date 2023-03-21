class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

        self.x = [ladoA, ladoB, ladoC]
    def calcular_perimetro(self):
        perimetro = sum(self.x)
        print("Perimetro do triângulo:",perimetro)

    def get_maior_lado(self):
        self.x.sort()
        print("Maior lado:",self.x[2])