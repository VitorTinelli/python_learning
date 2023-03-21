class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentarsalario(self, aumento):
        self.aumento = aumento
        novosal = self.salario+(self.salario*self.aumento/100)
        print("O novo salário de {} é de: BRL {}".format(self.nome, novosal))

