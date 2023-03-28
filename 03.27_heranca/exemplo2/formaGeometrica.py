class FormaGeometrica():
    pi = 3.14

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcArea(self):
        area = FormaGeometrica.pi * (self.raio ** 2) # ** = elevado
        print(area)
