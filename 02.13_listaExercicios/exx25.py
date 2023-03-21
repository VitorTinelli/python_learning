print ("-_-_- Calculadora idades ? do Omega -_-_-")
print ()
homens = []
mulheres = []

homens.append(int(input("Digite a idade do primeiro homem: ")))
homens.append(int(input("Digite a idade do segundo homem: ")))
print()
mulheres.append(int(input("Digite a idade da primeira mulher: ")))
mulheres.append(int(input("Digite a idade da segunda mulher: ")))
print()
mulheres.sort()
homens.sort()
print("A soma da idade do homem mais velho com a mulher mais nova: {}".format(homens[1]+mulheres[0]))
print("O produto da idade do homem mais novo com a mulher mais nova: {}".format(homens[0]*mulheres[1]))
print()
print()
