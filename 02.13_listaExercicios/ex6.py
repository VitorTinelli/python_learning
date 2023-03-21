print ("-_-_- Calculadora de maçã do Omega >.< -_-_-")
print()
novo =int(input("Digite a quantidade de maçãs comprados: "))
if novo >0 and novo<12:
    print("O valor total é de: R${:.2f}".format(novo*1.30))
elif novo >=12:
    print("O valor total é de: R${:.2f}".format(novo))
else : print("Valor inválido")
print()
print()