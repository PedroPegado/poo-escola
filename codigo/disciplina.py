class Disciplina:
    def __init__(self, codigoDisciplina, nome, cargaHoraria):
        self.cargaHoraria = cargaHoraria
        self.nome = nome
        self.professor = None
        self.codigoDisciplina = codigoDisciplina

        with open("professores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")
            disciplinas_professor = dados[2]
            if (f"#{codigoDisciplina}" in disciplinas_professor):
                self.professor = dados[1]
                break
        
    
    def emitirRelatorio(self):
        print("\n---###---")
        print("Nome da disciplina:", self.nome)
        print("Carga Horária da disciplina:", self.cargaHoraria)
        print(f"Código da disciplina: #{self.codigoDisciplina}")
        if (self.professor == None):
            print("Professor: Indeterminado")
        else:
            print("Professor:", self.professor)
        print("---###---")
