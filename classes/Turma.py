import os
import json
from .Registrador import Registrador

class Turma:

    'Classe para registro de turmas dos alunos'
    alunos = []
    turmas = {}

    def __init__(self, turmas = {}, alunos = []):
        self.turmas = turmas
        self.alunos = alunos

    def cadastrar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno: ")
        if aluno in self.turmas:
            print("Aluno já possui turma cadastrada.")
        elif aluno in self.alunos:
            turma = input("Digite a turma do aluno:")
            self.turmas[aluno] = [turma]

            Registrador.registrarTurmas(Registrador, self.turmas)
        else:
            print("Aluno não encontrado")

    def editar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno que deseja editar a turma: ")
        if aluno in self.alunos:
            novaTurma = input("Por favor digite a nova turma para o aluno escolhido: ")
            self.turmas[aluno] = [novaTurma]
            Registrador.registrarTurmas(Registrador, self.turmas)
        else:
            print("Aluno não encontrado")
            
    def apagar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno que deseja apagar a turma: ")

        if aluno in self.alunos:
            del(self.turmas[aluno])
            Registrador.registrarTurmas(Registrador, self.turmas)
        else:
            print("Aluno não encontrado")
    
    def verTurmas(self):
        os.system(['clear','cls'][os.name == 'nt'])
        print("Estes sãos as turmas dos alunos cadastrados no sistema:")
        print(self.turmas)