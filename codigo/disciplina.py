class Disciplina:
    def __init__(self, cargaHoraria, nome, codigoDisciplina):
        self.cargaHoraria = cargaHoraria
        self.nome = nome
        self.professor = ""
        self.codigoDisciplina = codigoDisciplina
        
    
    def emitirRelatorio(self):
        print("Nome da disciplina:", self.nome)
        print("Carga Horária da disciplina:", self.cargaHoraria)
        print("Código da disciplina:", self.codigoDisciplina)
        if (self.professor == ""):
            print("Professor: Indeterminado")
        else:
            print("Professor:", self.professor)
