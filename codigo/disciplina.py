class Disciplina:
    def __init__(self, codigoDisciplina, nome, cargaHoraria):
        self.cargaHoraria = cargaHoraria
        self.nome = nome
        self.professor = ""
        self.codigoDisciplina = codigoDisciplina
        
    
    def emitirRelatorio(self):
        print("\n---###---")
        print("Nome da disciplina:", self.nome)
        print("Carga Horária da disciplina:", self.cargaHoraria)
        print(f"Código da disciplina: #{self.codigoDisciplina}")
        if (self.professor == ""):
            print("Professor: Indeterminado")
        else:
            print("Professor:", self.professor)
        print("---###---")
