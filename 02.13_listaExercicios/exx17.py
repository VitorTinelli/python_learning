print ("-_-_- Calculadora de médias do Omega -_-_-")
print ()
n1 = float(input("Digite a nota da primeira avaliação: "))
n2 = float(input("Digite a nota da segunda avaliação: "))

while n1 >10 or n1 <0:
    print()
    print("Nota 1 Inválida!")
    n1 = float(input("Digite a nota da primeira avaliação: "))

while n2 > 10 or n2<0:
    print()
    print("Nota 2 Inválida!")
    n2 = float(input("Digite a nota da segunda avaliação: "))
    
print()
media = (n1+n2)/2

print("Média do aluno: {:.2f}".format(media))
print()
print()