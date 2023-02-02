from aluno import Aluno
from disciplina import Disciplina
from professor import Professor


def checa_arquivo_existe(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            dados_arquivo = arquivo.readlines()
            return dados_arquivo
    except: 
        with open(nomeArquivo, 'w') as arquivo:
            pass

def estrutura_disciplina(dicionario):
    while True:
        print('''\nDIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR DISCIPLINA
        2 - EMITIR RELATÓRIO
        0 - VOLTAR''')
        acao_user = int(input("> "))

        if (acao_user == 1):
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
        elif (acao_user == 2):
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
        elif (acao_user == 0):
            return None

def estrutura_professor(dicionario_professores, dicionario_disciplinas):
    while True:
        print('''\nDIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR PROFESSOR
        2 - EMITIR RELATÓRIO
        3 - ALTERAR DISCIPLINAS
        0 - VOLTAR''')
        acao_user = int(input("> "))

        if acao_user == 1:
            print('Matricula do professor:')
            matricula_professor = input('> ')
            if dicionario_professores.get(f'{matricula_professor}') == None:
                print('Nome do professor: ')
                nome_professor = input('> ')
                print('Gostaria de cadastrar as disciplinas deste professor agora?')
                acao_user = int(input('(1)Sim (0)Não\n> '))
                disciplinas_professor = ""

                if acao_user == 1:
                    while True:
                        print('Digite o código da disciplina(0 para finalizar)')
                        codigo_disciplina = input('> #')
                        if (dicionario_disciplinas.get(f"#{codigo_disciplina}") == None and codigo_disciplina != "0"):
                            print("Essa disciplina não existe.")
                            continue
                        elif (codigo_disciplina == '0'):
                            disciplinas_professor = disciplinas_professor[0:len(disciplinas_professor) - 1]
                            break
                        else:
                            if (f"#{codigo_disciplina}" in disciplinas_professor):
                                print("Essa disciplina já foi cadastrada para esse professor.")
                            else:
                                disciplinas_professor += f'#{codigo_disciplina},'

                    professor = Professor(matricula_professor)
                    linha = f"{matricula_professor}:{nome_professor}:{disciplinas_professor}:\n"
        
                    with open('professores.txt', 'a') as arquivo:
                        arquivo.write(linha)
                        
                elif acao_user == 0:
                    professor = Professor(matricula_professor)
                    linha = f"{matricula_professor}:{nome_professor}:{None}:\n"

                    with open('professores.txt', 'a') as arquivo:
                        arquivo.write(linha)

                dicionario_professores[matricula_professor] = [nome_professor,disciplinas_professor]

                print('\n====================\nProfessore cadastrade\n====================')
                return dicionario_professores
            else:
                print('\n====================\nProfessore já cadastrade\n====================')
        elif (acao_user == 2):
            print("Digite a matrícula do professor:")
            matricula_professor = int(input())
            dados_prof = dicionario_professores.get(f"{matricula_professor}")
            if (dados_prof == None):
                print("Professor inexistente.")
            else:
                professor = Professor(matricula_professor)
                professor.emitirRelatorio()
        elif (acao_user == 0):
            return None



def estrutura_aluno(dicionario_alunos, dicionario_disciplinas):
    while True:
        print('''\nDIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR ALUNO
        2 - EMITIR RELATÓRIO
        3 - ALTERAR NOTAS
        4 - ALTERAR DISCIPLINAS
        0 - VOLTAR''')
        acao_user = int(input("> "))

        if (acao_user == 1):
            print("Matricula do aluno:")
            matricula_aluno = input("> ")
            if (dicionario_alunos.get(matricula_aluno) == None):
                print("Nome do aluno:")
                nome_aluno = input("> ")
                print("Gostaria de cadastrar as disciplinas deste aluno agora?")
                acao_user = int(input("(1)Sim (0)Não\n> "))
                disciplinas_alunos = ""
                
                if acao_user == 1:
                    while True:
                        print('Digite o código da disciplina(0 para finalizar)')
                        codigo_disciplina = input('> #')
                        if (dicionario_disciplinas.get(f"#{codigo_disciplina}") == None and codigo_disciplina != "0"):
                            print("Essa disciplina não existe.")
                            continue
                        elif codigo_disciplina == '0':
                            disciplinas_alunos = disciplinas_alunos[0:len(disciplinas_alunos) - 1]
                            break
                        else:
                            if f'#{codigo_disciplina}' in disciplinas_alunos:
                                print('Essa disciplina já foi cadastrada para esse aluno.')
                            else:
                                disciplinas_alunos += f'#{codigo_disciplina},0,0,0,0:'
                    
                    aluno = Aluno(matricula_aluno)
                    linha = f'{matricula_aluno}:{nome_aluno}:{disciplinas_alunos}:\n'
                    
                    with open('alunos.txt', 'a') as arquivo:
                        arquivo.write(linha)
                elif acao_user == 0:
                    aluno = Aluno(matricula_aluno)
                    linha = f'{matricula_aluno}:{nome_aluno}::\n'
                    
                    with open('alunos.txt', 'a') as arquivo:
                        arquivo.write(linha)
                
                dicionario_alunos[matricula_aluno] = [nome_aluno,disciplinas_alunos]
                print('\n====================\nAlune cadastrade\n====================')
                return dicionario_alunos
            else:
                print('\n====================\nAlune já cadastrade\n====================')
        elif acao_user == 2:
            print("Digite a matrícula do aluno:")
            matricula_aluno = int(input())
            dados_aluno = dicionario_alunos.get(f"{matricula_aluno}")
            if (dados_aluno == None):
                print("Aluno inexistente")
            else:
                aluno = Aluno(matricula_aluno)
                aluno.emitirBoletim()
        elif (acao_user == 0):
            return None    
