from veiculos import Veiculo, Motocicleta

v = Veiculo("Carro", "gwu364", "bmw", "m4a1", "2022")
m = Motocicleta("Motivo", "gj35", "bmw", "f700", "2022", "798")

print(isinstance(v, Veiculo), isinstance(v, Motocicleta))
print(isinstance(m, Veiculo), isinstance(m, Motocicleta))