class Aluno:
    def __init__(self, matricula):
        self.matricula = matricula
        self.notas = []
        self.disciplinas = []

        with open("matriculas_alunos.txt", "r+") as arquivo:
            linhas = arquivo.readlines()

            if (f"{self.matricula}:\n" not in linhas):
                print("Esse(a) aluno(a) não existe. Informe os seguintes dados para cadastra-lo(a) no sistema.\n")
                print("Nome do(a) aluno(a):")
                self.nome = input("> ")
                arquivo.write(f"{self.matricula}:\n")

                with open("alunos.txt", "a") as arquivo:
                    arquivo.write(f"{self.matricula}:{self.nome}:\n")

                return None

        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        possui_disciplinas = False
        for linha in linhas:
            dados = linha.split(":")
            if (self.matricula in dados):
                self.nome = dados[1]
                disciplinas = dados[2:len(dados) - 1]
                possui_disciplinas = True
                break

        if (possui_disciplinas):
            for disciplina in disciplinas:
                dados = disciplina.split(",")
                self.disciplinas.append(dados[0])
                self.notas.append(dados[1:])

