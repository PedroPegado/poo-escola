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

        if (dados_pessoa[1] == ""):
            disciplinas_pessoa = []
        else:
            disciplinas_pessoa = dados_pessoa[1]

        print("1 - ADICIONAR\n2 - EXCLUIR")
        acao_user = int(input("> "))

        try:
            if (disciplinas_pessoa[0] == "None"):
                pass
        except:
            if (acao_user == 2):
                print("Essa pessoa não possui disciplinas.")
                return False
        
        if (acao_user == 1):
            if (disciplinas_pessoa[0] == "None"):
                disciplinas_pessoa[0] = f"#{codigoDisciplina}"
            else:
                if (len(str(self.matricula)) == 14):
                    disciplinas_pessoa.append(f"#{codigoDisciplina},0,0,0,0")
                else:
                    disciplinas_pessoa.append(f"#{codigoDisciplina}")
            self.codigosDisciplinas.append(f"#{codigoDisciplina}")
        elif (acao_user == 2):
            indice = disciplinas_pessoa.index(f"#{codigoDisciplina}")
            disciplinas_pessoa.pop(indice)
            disciplinas_pessoa.insert(indice, "None")
            self.codigosDisciplinas.remove(f"#{codigoDisciplina}")
        
        dicionarioPessoa[f"{self.matricula}"] = [dados_pessoa[0], disciplinas_pessoa]

        return dicionarioPessoa
