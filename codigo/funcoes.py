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

def validar_acao(mensagem):
    try:
        acao_user = int(input(mensagem))
    except:
        print("\nAção inválida.\n")
        return ""
    else:
        return acao_user

def validar_matricula(matricula, pessoa):
    matricula = str(matricula)
    tamanho_matricula = len(matricula)
    if (pessoa == "aluno"):
        if (tamanho_matricula == 14):
            return True
        print("\nA matricula deve ter 14 digitos\n")
        return False
    else:
        if (tamanho_matricula == 6):
            return True
        print("\nA matricula deve ter 6 digitos\n")
        return False

def validar_codigo(codigo):
    codigo = str(codigo)
    tamanho_codigo = len(codigo)
    if tamanho_codigo == 3:
        return True
    print('O código deve ter 3 digitos')
    return False

def estrutura_disciplina(dicionario):
    while True:
        print('''
        DIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR DISCIPLINA
        2 - EMITIR RELATÓRIO
        0 - VOLTAR''')
        acao_user = validar_acao("> ")

        if (acao_user == ""):
            continue
        
        elif (acao_user == 1):
            print("Código da disciplina:")
            codigo_disciplina = input("> #")
            
            if validar_codigo(codigo_disciplina) == False:
                continue
            
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

            print('\n====================\nCódigo já cadastrado\n====================')
        elif (acao_user == 2):
            print("Digite o código da disciplina:")
            codigo_disciplina = input('> #')
            materia = dicionario.get(f'#{codigo_disciplina}')

            if (materia == None):
                print('Disciplina inexistente')
                continue

            nome_disciplina = materia[0]
            carga_horaria = materia[1]
            disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)
            disciplina.emitirRelatorio()
        elif (acao_user == 0):
            return None

def estrutura_professor(dicionario_professores, dicionario_disciplinas):
    while True:
        print('''
        DIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR PROFESSOR(A)
        2 - EMITIR RELATÓRIO
        3 - ALTERAR DISCIPLINAS
        0 - VOLTAR''')
        acao_user = validar_acao("> ")

        if (acao_user == ""):
            continue
        elif (acao_user == 1):
            print('Matricula do(a) professor(a):')
            matricula_professor = validar_acao("> ")
            if (validar_matricula(matricula_professor, "professor") == False):
                continue

            if dicionario_professores.get(f'{matricula_professor}') == None:
                print('Nome do(a) professor(a): ')
                nome_professor = input('> ')
                print('Gostaria de cadastrar as disciplinas deste(a) professor(a) agora?')
                acao_user = validar_acao('(1)Sim (0)Não\n> ')
                disciplinas_professor = ""

                if acao_user == 1:
                    while True:
                        print('Digite o código da disciplina(0 para finalizar)')
                        codigo_disciplina = input('> #')
                        if (dicionario_disciplinas.get(f"#{codigo_disciplina}") == None and codigo_disciplina != "0"):
                            print("Essa disciplina não existe.")
                            continue
                        elif (codigo_disciplina == '0'):
                            if (disciplinas_professor == ""):
                                disciplinas_professor == "None"
                            else:
                                disciplinas_professor = disciplinas_professor[0:len(disciplinas_professor) - 1]
                            break

                        if (f"#{codigo_disciplina}" in disciplinas_professor):
                            print("Essa disciplina já foi cadastrada para esse(a) professor(a).")
                            continue
                        disciplinas_professor += f'#{codigo_disciplina}:'

                    professor = Professor(matricula_professor)
                    linha = f"{matricula_professor}:{nome_professor}:{disciplinas_professor}:\n"
        
                    with open('professores.txt', 'a') as arquivo:
                        arquivo.write(linha)
                        
                elif acao_user == 0:
                    professor = Professor(matricula_professor)
                    linha = f"{matricula_professor}:{nome_professor}:\n"

                    with open('professores.txt', 'a') as arquivo:
                        arquivo.write(linha)

                dicionario_professores[matricula_professor] = [nome_professor,disciplinas_professor]

                print('\n====================\nProfessor(a) cadastrado(a)\n====================')
                return dicionario_professores

            print('\n====================\nProfessore já cadastrade\n====================')

        elif (acao_user == 2):
            print("Digite a matrícula do(a) professor(a):")
            matricula_professor = validar_acao("> ")
            if (validar_matricula(matricula_professor, "professor") == False):
                continue

            dados_prof = dicionario_professores.get(f"{matricula_professor}")

            if (dados_prof == None):
                print("Professor(a) inexistente.")
                continue

            professor = Professor(matricula_professor)
            professor.emitirRelatorio()

        elif (acao_user == 3):
            print('Digite a matrícula do(a) professor(a):')
            matricula_professor = validar_acao("> ")
            if (validar_matricula(matricula_professor, "professor") == False):
                continue
            
            dados_prof = dicionario_professores.get(f'{matricula_professor}')
            
            if dados_prof == None:
                print('Professor(a) inexistente.')
                continue
            
            print('Digite o código da disciplina:')
            codigo_disciplina = input('> #')
            
            dados_disciplina = dicionario_disciplinas.get(f'#{codigo_disciplina}')
            
            if dados_disciplina == None:
                print('Disciplina inexistente.')
                continue
                
            professor = Professor(matricula_professor)
            professor.alterarDisciplina(codigo_disciplina, 'professores.txt')
            
        elif (acao_user == 0):
            return None



def estrutura_aluno(dicionario_alunos, dicionario_disciplinas):
    while True:
        print('''
        DIGITE A OPÇÃO DESEJADA:
        1 - CADASTRAR ALUNO(A)
        2 - EMITIR BOLETIM
        3 - ALTERAR DISCIPLINAS
        4 - ALTERAR NOTAS
        0 - VOLTAR''')
        acao_user = validar_acao("> ")

        if (acao_user == ""):
            continue
        
        elif (acao_user == 1):
            print("Matricula do(a) aluno(a):")
            matricula_aluno = validar_acao("> ")
            if (validar_matricula(matricula_aluno, "aluno") == False):
                continue
            
            if (dicionario_alunos.get(f"{matricula_aluno}") == None):
                print("Nome do(a) aluno(a):")
                nome_aluno = input("> ")
                print("Gostaria de cadastrar as disciplinas do(a) aluno(a) agora?")
                acao_user = validar_acao("(1)Sim (0)Não\n> ")
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
                                print('Essa disciplina já foi cadastrada para o(a) aluno(a).')
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
                print('\n====================\nAluno(a) cadastrado(a)\n====================')
                return dicionario_alunos
            
            qprint('\n====================\nAluno(a) já cadastrado(a)\n====================')
                
        elif acao_user == 2:
            print("Digite a matrícula do(a) aluno(a):")
            matricula_aluno = validar_acao("> ")
            if (validar_matricula(matricula_aluno, "aluno") == False):
                continue
            dados_aluno = dicionario_alunos.get(f"{matricula_aluno}")

            if (dados_aluno == None):
                print("Aluno(a) inexistente")
                continue

            aluno = Aluno(matricula_aluno)
            aluno.emitirBoletim()
        
        elif acao_user == 3:
            print('Digite a matrícula do(a) aluno(a):')
            matricula_aluno = validar_acao("> ")
            if (validar_matricula(matricula_aluno, "aluno") == False):
                continue
            
            dados_aluno = dicionario_alunos.get(f'{matricula_aluno}')
            
            if dados_aluno == None:
                print('Aluno(a) inexisteste.')
                continue
            
            print('Digite o código da disciplina:')
            codigo_disciplina = input('> #')
            
            dados_disciplina = dicionario_disciplinas.get(f'#{codigo_disciplina}')
            
            if dados_disciplina == None:
                print('Disciplina inexistente.')
                continue
            
            aluno = Aluno(matricula_aluno)
            aluno.alterarDisciplina(codigo_disciplina, 'alunos.txt')
            
        elif acao_user == 4:
            print('Digite a matrícula do(a) aluno(a):')
            matricula_aluno = validar_acao("> ")
            if (validar_matricula(matricula_aluno, "aluno") == False):
                continue
            dados_aluno = dicionario_alunos.get(f'{matricula_aluno}')
            
            if dados_aluno == None:
                print('Aluno(a) inexistente')
                continue
            
            print('Digite o código da disciplina:')
            codigo_disciplina = input('> #')
            
            dados_disciplina = dicionario_disciplinas.get(f'#{codigo_disciplina}')
        
            if dados_disciplina == None:
                print('Disciplina inexistente')
                continue
             
            aluno = Aluno(matricula_aluno)
            aluno.alterarNotas(codigo_disciplina)

        elif (acao_user == 0):
            return None    
