class Disciplina:
    def __init__(self, codigoDisciplina):
        self.codigoDisciplina = f"#{codigoDisciplina}"
        self.professores = []
        with open("codigos_disciplinas.txt", "r+") as arquivo:
            linhas = arquivo.readlines()

            if (f"{self.codigoDisciplina}:\n" not in linhas):
                print("\nEssa disciplina não existe. Informe os seguintes dados para cadastra-la no sistema.\n")
                print("Nome da discilina:")
                self.nome = input("> ")
                print("Carga Horaria da disciplina:")
                self.cargaHoraria = int(input("> "))
                arquivo.write(f"{self.codigoDisciplina}:\n")
                with open("disciplinas.txt", "a") as arquivo:
                    arquivo.write(f"{self.codigoDisciplina}:{self.nome}:{self.cargaHoraria}:\n")
                return None

        with open("disciplinas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")
            if (self.codigoDisciplina == dados[0]):
                self.nome = dados[1]
                self.cargaHoraria = dados[2]
                break

        with open("professores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")

            if (self.codigoDisciplina in dados[2]):
                self.professores.append(dados[1])

    def emitirRelatorio(self):
        print("\nNome da disciplina:")
        print(self.nome)
        print("Código da disciplina:")
        print(self.codigoDisciplina)
        print("Carga Horaria:")
        print(self.cargaHoraria)
        print("Professor(es):")
        if (self.professores == []):
            print("Indeterminado")
        else:
            for professor in self.professores:
                print(professor)

        print("Aluno(s):")
        print("(Nome, N1, N2, N3, N4, MF)")

        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            disciplina_tem_alunos = False

        for linha in linhas:
            dados_aluno = linha.split(":")
            disciplinas_aluno = dados_aluno[2:]
            for disciplina in disciplinas_aluno:
                codigo_disciplina_aluno = disciplina[0:4]

                if (self.codigoDisciplina == codigo_disciplina_aluno):
                    disciplina_tem_alunos = True
                    dados_disciplina_aluno = disciplina.split(",")
                    notas_aluno = dados_disciplina_aluno[1:]
                    n1, n2, n3, n4 = [float(x) for x in notas_aluno]
                    media_final = ((n1 * 2) + (n2 * 2) + (n3 * 3) + (n4 * 3)) / 10
                    nome_aluno = dados_aluno[1]
                    print(f"{nome_aluno}, {n1:.1f}, {n2:.1f}, {n3:.1f}, {n4:.1f}, {media_final:.1f}")
                    break

        if (not disciplina_tem_alunos):
            print("Indeterminado.")
        print()


