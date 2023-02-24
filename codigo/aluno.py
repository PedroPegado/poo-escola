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

    def emitirBoletim(self):
        with open("disciplinas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        print("\nNome do(a) aluno(a):")
        print(self.nome)
        print("Matricula do(a) aluno(a):")
        print(self.matricula)
        print("Disciplina(s):")
        print("(Nome, N1, N2, N3, N4, MF)")
        for index, disciplina in enumerate(self.disciplinas):
            n1, n2, n3, n4 = [float(x) for x in self.notas[index]]
            media_final = ((n1 * 2) + (n2 * 2) + (n3 * 3) + (n4 * 3)) / 10
            for linha in linhas:
                if (disciplina in linha):
                    nome_disciplina = linha.split(":")[1]
                    break

            print(f"{nome_disciplina}, {n1:.1f}, {n2:.1f}, {n3:.1f}, {n4:.1f}, {media_final:.1f}")

    def adicionarDisciplina(self, codigoDisciplina):

        if (f"#{codigoDisciplina}" in self.disciplinas):
            return False

        with open("alunos.txt", "r+") as arquivo:
            linhas = arquivo.readlines()
            dados = f"{self.matricula}:{self.nome}:"

            if (self.disciplinas != []):
                for index, disciplina in enumerate(self.disciplinas):
                    n1, n2, n3, n4 = [int(x) for x in self.notas[index]]
                    dados += f"{disciplina},{n1},{n2},{n3},{n4}:"

            indice_aluno = linhas.index(dados+"\n")
            dados += f"#{codigoDisciplina},0,0,0,0:\n"
            linhas[indice_aluno] = dados
            arquivo.seek(0)
            arquivo.writelines(linhas)

        self.disciplinas.append(f"#{codigoDisciplina}")
        self.notas.append(["0","0","0","0"])
        return True


