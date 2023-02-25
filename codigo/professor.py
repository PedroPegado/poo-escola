class Professor:
    def __init__(self, matricula):
        self.matricula = matricula

        with open("matriculas_professores.txt", "r+") as arquivo:
            linhas = arquivo.readlines()

            if (f"{self.matricula}:\n" not in linhas):
                print("Esse(a) professor(a) não existe. Informe os seguintes dados para cadastra-lo(a) no sistema.\n")
                print("Nome do(a) professor(a):")
                self.nome = input("> ")
                arquivo.write(f"{self.matricula}:\n")

                with open("professores.txt","a") as arquivo:
                    arquivo.write(f"{self.matricula}:{self.nome}:\n")

                return None

        with open("professores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split(":")
            if (self.matricula in dados):
                self.nome = dados[1]
                break

