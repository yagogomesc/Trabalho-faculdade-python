import os
import json
from .Registrador import Registrador

class Curso:

    'Classe para registro de cursos dos alunos'

    cursos = {}
    alunos = []

    def __init__(self, cursos = {}, alunos= []):
        self.cursos = cursos
        self.alunos = alunos

    def cadastrar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno: ")
        if aluno in self.cursos:
            print("Aluno já possui curso cadastrado.")
        elif aluno in self.alunos:
            curso = input("Digite o curso do aluno: ")
            self.cursos[aluno] = [curso]
            
            Registrador.registrarCursos(Registrador, self.cursos)
        else:
            print("Aluno não encontrado")

    def editar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno que deseja editar o Curso: ")
        if aluno in self.cursos:
            novoCurso = input("Por favor digite o novo curso para o aluno escolhido: ")
            self.cursos[aluno] = [novoCurso]
            Registrador.registrarCursos(Registrador, self.cursos)
        else:
            print("Aluno não encontrado")


    def apagar(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno que deseja apagar o curso: ")

        if aluno in self.cursos:
            print("Curso apagado.")
            del(self.cursos[aluno])
            Registrador.registrarCursos(Registrador, self.cursos)
        else:
            print("Aluno não encontrado")
    
    def verCursos(self):
        os.system(['clear','cls'][os.name == 'nt'])
        print("Estes sãos os cursos dos alunos cadastrados no sistema:")
        print(self.cursos)