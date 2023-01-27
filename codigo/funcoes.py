def checa_existe(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            if (nomeArquivo == "disciplinas.txt"):
                dadosDisciplinas = arquivo.readlines()
                return dadosDisciplinas
    except: 
        with open(nomeArquivo, 'w') as arquivo:
            pass

def estrutura_disciplina(dicionario):
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - CRIAR DISCIPLINA
    2 - EMITIR RELATÓRIO''')
    acao_dois = int(input("> "))

    if (acao_dois == 1):
        print("Código da disciplina:")
        codigo_disciplina = input("> #")

        if dicionario.get(f'#{codigo_disciplina}') == None:
            print("Carga horaria:")
            carga_horaria = int(input("> "))
            print("Nome da disciplina:")
            nome_disciplina = input("> ")

            disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)
            linha = f"#{codigo_disciplina}:{nome_disciplina}:{carga_horaria}:\n"

            with open("disciplinas.txt", 'a') as arquivo:
                arquivo.write(linha)

            dicionario[f"#{codigo_disciplina}"] = [nome_disciplina, carga_horaria]
            return dicionario
        else:
            print('====================\nCódigo já cadastrado\n====================')
    elif (acao_dois == 2):
        print("Digite o código da disciplina:")
        codigo_disciplina = input('> #')
        materia = dicionario.get(f'#{codigo_disciplina}')
        if (materia == None):
            print('Disciplina inexistente')
        else:
            nome_disciplina = materia[0]
            carga_horaria = materia[1]
            disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)
            disciplina.emitirRelatorio()
