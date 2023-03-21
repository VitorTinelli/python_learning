print ("-_-_- Contador de negativos do Omega -_-_-")
print ()
contn = 0
for i in range (1,11):
    n = float(input("Digite um número: "))
    if n < 0:
        contn = contn+1
print()
print("Total de números negativos: {}".format(contn))
print()
print()