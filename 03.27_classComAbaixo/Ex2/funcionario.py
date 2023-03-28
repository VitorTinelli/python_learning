class Pessoa():
    def __init__(self, nome) -> None:
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, salario) -> None:
        super().__init__(nome)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
        
    @salario.setter
    def salario(self, a):
        raise ValueError("Não é possivel alterar o valor")


    def aumentarsalario(self, aumento):
        self.aumento = aumento
        novosal = self.salario+(self.__salario*self.aumento/100)
        print("O novo salário de {} é de: BRL {}".format(self.nome, novosal))

