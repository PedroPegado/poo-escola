class Pessoa:
    def __init__(self, matricula):
        self.matricula = matricula
        self.codigosDisciplinas = []
    
    def alterarDisciplina(self, codigoDisciplina, dicionarioDisciplinas, dicionarioPessoa):
        dados_disciplina = dicionarioDisciplinas.get(f"#{codigoDisciplina}")

        if (dados_disciplina == None):
            print("Disciplina inexistente.")
            return False
        
        dados_pessoa = dicionarioPessoa.get(f"{self.matricula}")
        disciplinas_pessoa = dados_pessoa[1]

        print("1 - ADICIONAR\n2 - EXCLUIR")
        acao_user = int(input("> "))

        if (disciplinas_pessoa[0] == "None"):
            novas_disciplinas = []
            if (acao_user == 2):
                print("Essa pessoa não possui disciplinas.")
                return False
        
        novas_disciplinas = disciplinas_pessoa

        if (acao_user == 1):
            novas_disciplinas.append(f"#{codigoDisciplina}:")
            self.codigosDisciplinas.append(f"#{codigoDisciplina}")
        elif (acao_user == 2):
            indice = 0
            for disciplina in disciplinas_pessoa:
                if (f"#{codigoDisciplina}" == disciplina[0:3]):
                    novas_disciplinas.pop(indice)
                    break
                indice = indice + 1
        
        dicionarioPessoa[f"{self.matricula}"] = [dados_pessoa[0], novas_disciplinas]

        return dicionarioPessoa
