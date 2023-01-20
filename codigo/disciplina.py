class Disciplina:
    def __init__(self, cargaHoraria, nome, codigoDisciplina):
        self.cargaHoraria = cargaHoraria
        self.nome = nome
        self.professor = ""
        self.codigoDisciplina = codigoDisciplina

        linha = f"#{self.codigoDisciplina}:{self.nome}:{self.cargaHoraria}:\n"

        with open("disciplinas.txt", 'a') as arquivo:
            arquivo.write(linha)
                
    
    def emitirRelatorio(self):
        print(f"Nome da disciplina:", self.nome)
        print(f"Carga Horária da disciplina:", self.cargaHoraria)
        print(f"Código da disciplina:", self.codigoDisciplina)
        if (self.professor == ""):
            print(f"Professor: Indeterminado")
        else:
            print(f"Professor:", self.professor)
