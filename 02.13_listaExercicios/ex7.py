print ("-_-_- Calculadora de médias do Omega -_-_-")
print ()
n1 = float(input("Digite a nota da primeira avaliação: "))
n2 = float(input("Digite a nota da segunda avaliação: "))
media = (n1+n2)/2

if media <6:
    print ("Status: Reprovado!")
    print ("Média: {}".format (media))
else:
    print ("Status: Aprovado!")
    print ("Média: {}".format (media))
print()
print()
