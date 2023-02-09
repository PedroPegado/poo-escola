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
                    
    def alterarNotas(self, matricula, codigoDisciplina):        
        notas = []
        
        for c in range(1, 5):
            print(f'Digite a nota do {c}° bimestre:')
            nota = input('> ')
            notas.append(nota)
        
        with open('alunos.txt', 'r') as arquivo:
            banco = arquivo.readlines()
            
        for linha in banco:
            ind_alunos = linha.split(':')
            if ind_alunos[0] == matricula:
                indice = banco.index(linha)
                break
        
        splitado = banco[indice].split(':')
        
        cont = 0 
        for ind in splitado:
            if codigoDisciplina in ind:
                splitado[cont] = f'#{codigoDisciplina},{notas[0]},{notas[1]},{notas[2]},{notas[3]}'
                break
            cont+=1
        
        cont = 0
        novo_aluno = ''
        
        for ind in splitado:
            if cont == len(splitado) - 1:
                novo_aluno += f'{ind}'
            else:
                novo_aluno += f'{ind}:'
            cont+=1
        
        banco[indice] = novo_aluno
        
        with open('alunos.txt', 'w') as arquivo:
            arquivo.writelines(banco)
            
        
        
            
            
        
        
        
        