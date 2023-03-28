class Funcionario():
    def __init__(self, nome, cargo, valorHoraTrabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valorHoraTrabalhada = valorHoraTrabalhada
        self.__salario = 0
        self.__horasTrabalhadas = 34

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario (self, a):
        raise ValueError("Impossivel alterar o salário manualmente!")
        

    def registraHoraTrabalhada(self):
        self.horasTrabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horasTrabalhadas * self.valorHoraTrabalhada
        print("Salário de {}: R$ {}".format(self.nome, self.__salario) )

    