from triangulo import Triangulo

ladoA = int(input("Digite o valor do lado A: "))
ladoB = int(input("Digite o valor do lado B: "))
ladoC = int(input("Digite o valor do lado C: "))

triangulo_obj = Triangulo(ladoA, ladoB, ladoC)

triangulo_obj.calcular_perimetro()
triangulo_obj.get_maior_lado()