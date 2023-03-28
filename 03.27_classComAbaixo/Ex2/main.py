from funcionario import Funcionario

nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o aumento salarial: "))


func = Funcionario(nome, salario)
#func.salario = 1000 #Erro
func.aumentarsalario(aumento)

