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
                    self.codigosDisciplinas = dados[2:]
                    break
                
    def emitirBoletim(self):
        print('\n---###---')
        print('Matricula do aluno:', self.matricula)
        with open('alunos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.split(':')
                if self.matricula == int(dados[0]):
                    print('Nome do aluno:', dados[1])
                    break
        print('Disciplinas do aluno:')
        with open('disciplinas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(':')
            codigo_disciplina = dados[0]

            for disciplina in self.codigosDisciplinas:
                if codigo_disciplina in disciplina:
                    boletim = disciplina.split(',')
                    print(f'{dados[1]} - {boletim[1:]}')
                    
    def alterarNotas(self, codigoDisciplina, notas):
        