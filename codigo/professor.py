from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, matricula):
        super().__init__(matricula)

        with open("professores.txt", 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.split(":")
                if (f"{self.matricula}" == dados[0]):
                    self.codigosDisciplinas = dados[2:len(dados) - 1]
                    break
                
    
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
        with open("disciplinas.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
        
        for linha in linhas:
            dados = linha.split(":")
            codigo_disciplina = dados[0]
            if (codigo_disciplina in self.codigosDisciplinas):
                print(dados[1])
                continue
