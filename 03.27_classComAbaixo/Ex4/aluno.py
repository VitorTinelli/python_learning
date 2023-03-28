class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

class Aluno(Pessoa):

    def __init__(self, nome, curso, tempoSemDormir) -> None:
        super().__init__(nome)
        self.nome = nome
        self.__curso = curso
        self.tempoSemDormir = tempoSemDormir
        
        @property
        def curso(self):
            return self.__curso
            
        @curso.setter
        def curso(self, a):
            raise ValueError("Você não pode alterar o curso manualmente")

    def estudar (self, tempoEstudo):
        self.tempoSemDormir += tempoEstudo

    def dormir (self, tempoSono):
        print ("Tempo sem dormir: {}h".format(self.tempoSemDormir - tempoSono)) 
