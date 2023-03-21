print ("-_-_- Contador de range do Omega -_-_-")
print ()
contr = 0
contf = 0

for i in range (1,11):
    n = float(input("Digite um número: "))
    if n > 9 and n <21:
        contr = contr+1
    else: contf = contf+1
    
print()
print("Total de números no intervalo: {}".format(contr))
print("Total de números fora do intervalo: {}".format(contf))
print()
print()