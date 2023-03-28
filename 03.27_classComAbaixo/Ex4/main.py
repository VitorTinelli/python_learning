from aluno import Aluno

nome = input("Digite o nome do aluno: ")
curso = input("Digite o curso do aluno: ")
tempoSemDormir = float(input("Digite quanto tempo sem dormir: "))
tempoEstudo = float(input("Digite as horas de estudo: "))
tempoSono = float(input("Digite as horas de sono: "))



rotina = Aluno(nome, curso, tempoSemDormir)
#rotina.curso = "Pedro"
rotina.estudar(tempoEstudo)
rotina.dormir(tempoSono)