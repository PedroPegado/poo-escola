from aluno import Aluno
from disciplina import Disciplina
from pessoa import Pessoa
from professor import Professor


def checa_existe(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados_arquivo = arquivo.readlines()
            return dados_arquivo
    except: 
        with open(nomeArquivo, 'w') as arquivo:
            pass

def estrutura_disciplina(dicionario):
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - CADASTRAR DISCIPLINA
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

            print('\n====================\nDisciplina cadastrada\n====================')
            return dicionario
        else:
            print('\n====================\nCódigo já cadastrado\n====================')
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

def estrutura_professor(dicionario):
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - CADASTRAR PROFESSOR
    2 - EMITIR RELATÓRIO
    3 - ALTERAR DISCIPLINAS''')
    acao_user = int(input("> "))

    if acao_user == 1:
        print('Matricula do professor:')
        matricula_professor = input('> ')

        if dicionario.get(f'{matricula_professor}') == None:
            print('Nome do professor: ')
            nome_professor = input('> ')
            print('Gostaria de cadastrar as disciplinas deste professor agora?')
            acao_user = int(input('(1)Sim (0)Não\n> '))
            disciplinas_prof = ""

            if acao_user == 1:
                while True:
                    print('Digite o código da disciplina(0 para finalizar)')
                    codigo_disciplina = input('> #')
                    if codigo_disciplina == '0':
                        disciplinas_prof = disciplinas_prof[0:len(disciplinas_prof) - 1]
                        break
                    else:
                        disciplinas_prof += f'#{codigo_disciplina},'

                professor = Professor(matricula_professor)
                professor.codigosDisciplinas = disciplinas_prof.split(",")
                linha = f"{matricula_professor}:{nome_professor}:{disciplinas_prof}:\n"
      
                with open('professores.txt', 'a') as arquivo:
                    arquivo.write(linha)
                    
            elif acao_user == 0:
                professor = Professor(matricula_professor)
                linha = f"{matricula_professor}:{nome_professor}:{None}:\n"

                with open('professores.txt', 'a') as arquivo:
                    arquivo.write(linha)

            dicionario[matricula_professor] = [nome_professor,disciplinas_prof]

            print('\n====================\nProfessore cadastrade\n====================')
            return dicionario
        else:
            print('\n====================\nProfessore já cadastrade\n====================')
def estrutura_aluno(dicionario):
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - CADASTRAR ALUNO
    2 - EMITIR RELATÓRIO
    3 - ALTERAR NOTAS
    4 - ALTERAR DISCIPLINAS''')
    acao_user = int(input("> "))

    if (acao_user == 1):
        print("Matricula do aluno:")
        matricula_aluno = input("> ")
        if (dicionario.get(matricula_aluno) == None):
            print("Nome do aluno:")
            nome_aluno = input("> ")
            print("Gostaria de cadastrar as disciplinas deste aluno agora?")
            acao_user = input("(1)Sim (0)Não\n> ")

