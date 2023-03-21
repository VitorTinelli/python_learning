print ("-_-_- Calculadora de preço do combustivel do Omega -_-_-")
print()
ncomb = float(input("Digite quantos litros foram vendidos: "))
print("Digite 'A' para Álcool e 'G' para Gasolina.")
tcomb = input("Digite o tipo de combustivel vendido (A/G): ").lower()

if tcomb == "a":
    if ncomb > 20:
        print("Valor total: R${:.2f}".format((ncomb*2.9)*0.95))
    else: print("Valor total: R${:.2f}".format((ncomb*2.9)*0.97))
elif tcomb == "g":
    if ncomb > 20:
        print("Valor total: R${:.2f}".format((ncomb*3.3)*0.94))
    else: print("Valor total: R${:.2f}".format((ncomb*3.3)*0.96))
else: print("Tipo de combustivel inválido.")

print()
print()

