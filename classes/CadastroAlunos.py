import os
import json
from .Registrador import Registrador
from .Turma import Turma
from .Curso import Curso

class CadastroAlunos:

    'Classe para realizar cadastro, alteração e exclusão de alunos'
    alunos = []
    cursosAluno = Curso()
    turmasAluno = Turma()

    def __init__(self):
        
        self.alunos = Registrador.carregarAlunos(Registrador)
        self.cursosAluno = Curso(Registrador.carregarCursos(Registrador), self.alunos)
        self.turmasAluno = Turma(Registrador.carregarTurmas(Registrador), self.alunos)
        self.menu()
        
    def cadastrarAluno(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do novo aluno: ")
        if aluno in self.alunos:
            print("Aluno já cadastrado no sistema.")
        else:
            self.alunos.append(aluno)
            Registrador.registrarAlunos(Registrador, self.alunos)
        
        self.menu()

    def apagarAluno(self):
        os.system(['clear','cls'][os.name == 'nt'])
        aluno = input("Digite o nome do aluno que deseja apagar: ")

        if aluno in self.alunos:
            self.alunos.remove(aluno)
            if aluno in self.cursosAluno.cursos:    
                del(self.cursosAluno.cursos[aluno])
            if aluno in self.turmasAluno.turmas:
                del(self.turmasAluno.turmas[aluno])
            Registrador.registrarAlunos(Registrador, self.alunos)
            Registrador.registrarCursos(Registrador, self.cursosAluno.cursos)
            Registrador.registrarTurmas(Registrador, self.turmasAluno.turmas)
        else:
            print("Aluno não encontrado")

        self.menu()

    def verAlunos(self):
        os.system(['clear','cls'][os.name == 'nt'])
        print("Estes são os alunos cadastrados no sistema: ")
        print(self.alunos)
        self.menu()

    def menu(self):
        print("****Cadastro de Alunos****")
        print("1 - Cadastrar aluno")
        print("2 - Registrar curso")
        print("3 - Registrar turma")
        print("4 - Editar curso")
        print("5 - Editar turma")
        print("6 - Excluir aluno")
        print("7 - Excluir curso")
        print("8 - Excluir turma")
        print("9 - Ver alunos")
        print("10 - Ver cursos")
        print("11 - Ver turmas")
        print("12 - Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao not in(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
            self.menu()
        elif opcao == 1:
            self.cadastrarAluno()
        elif opcao == 2:
            self.cursosAluno.cadastrar()
            self.menu()
        elif opcao == 3:
            self.turmasAluno.cadastrar()
            self.menu()
        elif opcao == 4:
            self.cursosAluno.editar()
            self.menu()
        elif opcao == 5:
            self.turmasAluno.editar()
            self.menu()
        elif opcao == 6:
            self.apagarAluno()
        elif opcao == 7:
            self.cursosAluno.apagar()
            self.menu()
        elif opcao == 8:
            self.turmasAluno.apagar()
            self.menu()
        elif opcao == 9:
            self.verAlunos()
        elif opcao == 10:
            self.cursosAluno.verCursos()
            self.menu()
        elif opcao == 11:
            self.turmasAluno.verTurmas()
            self.menu()
        elif opcao == 12:
            exit()

main = CadastroAlunos()