from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.notas = []
        
        with open('alunos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                dados = linha.split(':')
                if f'{self.matricula}' == dados[0]:
                    self.codigosDisciplinas = dados[2].split(':')
                    break
                
    def emitirBoletim(self):
        pass

    def alterarNotas(self, codigoDisciplina, notas):
        pass