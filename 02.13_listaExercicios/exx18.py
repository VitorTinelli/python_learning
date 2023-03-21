print ("-_-_- Calculadora de médias do Omega -_-_-")
print ()
sus = "S"
conf = ""
while sus == "S":
    n1 = float(input("Digite a nota da primeira avaliação: "))
    n2 = float(input("Digite a nota da segunda avaliação: "))

    while n1 >10 or n1 <0:
        print("Nota 1 Inválida!")
        n1 = float(input("Digite a nota da primeira avaliação: "))

    while n2 > 10 or n2<0:
        print("Nota 2 Inválida!")
        n2 = float(input("Digite a nota da segunda avaliação: "))

    media = (n1+n2)/2
    print("Média do aluno: {:.2f}".format(media))

    while conf != "S" and conf != "N":
        conf = input("Deseja repetir? (S/N): ").upper()
        if conf == "S":
            sus = "S"
        elif conf == "N":
            sus = "N"
print()
print()
