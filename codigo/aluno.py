from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.notas = []

    def cadastrarAluno(self, nome, codigosDisciplinas):
        pass

    def emitirBoletim(self):
        pass

    def alterarNotas(self, codigoDisciplina, notas):
        pass