from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, matricula):
        super().__init__(matricula)
    
    def emitirRelatorio(self):
        print("\n---###---")
        print("Matricula do professor:", self.matricula)
        with open("professores.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.split(":")
                if (self.matricula == int(dados[0])):
                    print("Nome do professor:", dados[1])
                    break
        print("Disciplinas do professor:")
        print(self.codigosDisciplinas)