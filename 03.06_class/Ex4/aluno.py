class Aluno:

    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar (self, tempoEstudo):
        self.tempoSemDormir += tempoEstudo

    def dormir (self, tempoSono):
        print ("Tempo sem dormir: {}h".format(self.tempoSemDormir - tempoSono)) 
