from carro import Carro
qtdaComb = 0

consumo = int(input("Digite o consumo do carro (km/L): "))
distancia = int(input("Digite a distância a percorrer: "))

car = Carro(consumo, qtdaComb, distancia)

car.adicionar_Gasolina()
car.resto = 1000
car.andar(consumo, qtdaComb, distancia)
car.get_Gasolina()

