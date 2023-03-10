class Disciplina:
    def __init__(self, codigoDisciplina, nome, cargaHoraria):
        self.cargaHoraria = cargaHoraria
        self.nome = nome
        self.professor = ""
        self.codigoDisciplina = codigoDisciplina

        with open("professores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")
            disciplinas_professor = dados[2:]
            if (f"#{self.codigoDisciplina}" in disciplinas_professor):
                self.professor += dados[1] + "\n"
                continue
        
    
    def emitirRelatorio(self):
        print("\n---###---")
        print("Nome da disciplina:", self.nome)
        print("Carga Horária da disciplina:", self.cargaHoraria)
        print(f"Código da disciplina: #{self.codigoDisciplina}")
        if (self.professor == None):
            print("Professor(a) indeterminado.")
        else:
            print(f"Professor(es):\n{self.professor}\n")

        print("Alunos da disciplina:")

        with open("alunos.txt", 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")
            disciplinas_aluno = dados[2:]
            for disciplina in disciplinas_aluno:
                if (f"#{self.codigoDisciplina}" == disciplina[0:4]):
                    print(dados[1])
                    break

        print("---###---")
