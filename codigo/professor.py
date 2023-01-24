from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, matricula):
        super().__init__(matricula)
    
    def emitirRelatorio(self):
        with open('profesores.txt', 'r') as arquivoProfessor:
            linhasProf = arquivoProfessor.readlines()
            for linha in linhasProf:
                professor = linha.split(':')
                if (professor[0] == self.matricula):
                    print()
                    break

        with open('disciplinas.txt', 'r') as arquivoDisciplina:
            linhasDisc = arquivoDisciplina.readlines()
            for linha in linhasDisc:
                disciplina = linha.split(':')

    def cadastrarProfessor(self, nome, codigosDisciplinas):
        pass



        