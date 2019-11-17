import json
import os

class Registrador():

    'Classe para registrar dados inseridos em arquivos txt'
    diretorio = os.path.dirname(os.path.abspath(__file__))
    
    def carregarCursos(self):
        with open(os.path.join(self.diretorio + '/cursos/cursos.json'), 'r') as arquivo:
            cursos = json.load(arquivo)

        return cursos

    def carregarTurmas(self):
        with open(os.path.join(self.diretorio + '/turmas/turmas.json'), 'r') as arquivo:
            turmas = json.load(arquivo)

        return turmas

    def carregarAlunos(self):
        with open(os.path.join(self.diretorio + '/alunos/alunos.json'), 'r') as arquivo:
            alunos = json.load(arquivo)

        return alunos

    def registrarAlunos(self, alunos = []):
        with open(os.path.join(self.diretorio + '/alunos/alunos.json'), 'w') as arquivo:
            json.dump(alunos, arquivo)

    def registrarCursos(self, cursos = {}):
        with open(os.path.join(self.diretorio + '/cursos/cursos.json'), 'w') as arquivo:
            json.dump(cursos, arquivo)

    def registrarTurmas(self, turmas = {}):
        with open(os.path.join(self.diretorio + '/turmas/turmas.json'), 'w') as arquivo:
            json.dump(turmas, arquivo)