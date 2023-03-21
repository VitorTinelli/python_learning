print ("-_-_- Calculadora de aproveitamento do Omega -_-_-")
print ()
n1 = float(input("Digite a nota da primeira avaliação: "))
n2 = float(input("Digite a nota da segunda avaliação: "))
n3 = float(input("Digite a nota da terceira avaliação: "))
mexer = float(input("Digite a média dos exercicios: "))
 
mapro = (n1 + n2*2 + n3*3 + mexer)/7

if mapro < 6:
    print("Conceito D")
elif mapro >= 6 and mapro < 7.5:
    print("Conceito C")
elif mapro >= 7.5 and mapro <9:
    print("Conceito B")
else:
    print("Conceito A")