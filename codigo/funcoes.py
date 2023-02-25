from cores import Cores
from aluno import Aluno
from disciplina import Disciplina
cores = Cores()

def validar_arquivo(nome):
    try:
        arquivo = open(nome, "r")
    except:
        arquivo = open(nome, "x")
    finally:
        arquivo.close()

def validar_acao_usuario(mensagem):
    try:
        acao_usuario = int(input(mensagem))
    except:
        print(cores.pisca + "!!!!!!!!!!!!!" + cores.fim)
        print(cores.vermelho + "Ação inválida" + cores.fim)
        print(cores.pisca + "!!!!!!!!!!!!!" + cores.fim)
        return ""
    else:
        return acao_usuario

def validar_codigo_disciplina(codigo_disciplina):
    if (len(codigo_disciplina) != 3):
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        print(cores.vermelho + "O código da disciplina deve ter 3 digitos" + cores.fim)
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        return False

    return True

def validar_disciplina_existe(codigo_disciplina)
    with open("codigos_disciplinas.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    if (f"#{codigo_disciplina}:\n" not in linhas):
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        print(cores.vermelho + "Essa disciplina não existe" + cores.fim)
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        return False

    return True


def menu_disciplina():
    print("\nInforme o codigo de disciplina")
    codigo_disciplina = input("> #")

    retorno = validar_codigo_disciplina(codigo_disciplina)
    if (not retorno):
        return False
    disciplina = Disciplina(codigo_disciplina)

    while True:
        print("\n(1)Emitir Relatório da disciplina\n(2)Trocar de disciplina\n(0)Sair")
        acao_usuario = validar_acao_usuario("> ")
        if (acao_usuario == 0):
            return True
        elif (acao_usuario == 2):
            return False
        elif (acao_usuario == 1):
            disciplina.emitirRelatorio()

def menu_aluno():
    print("\nInforme a matricula do(a) aluno(a)")
    matricula = input("> ")

    if (len(matricula) != 14):
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        print(cores.vermelho + "A matricula deve ter 14 digitos" + cores.fim)
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        return False
    aluno = Aluno(matricula)

    while True:
        print("\n(1)Adicionar Disciplina\n(2)Remover Disciplina\n(3)Emitir Boletim\n(4)Trocar de aluno\n(0)Sair")

        acao_usuario = validar_acao_usuario("> ")
        if (acao_usuario == 0):
            return True
        elif (acao_usuario == 4):
            return False
        elif (acao_usuario == 3):
            aluno.emitirBoletim()
        elif (acao_usuario == 1 or acao_usuario == 2):
            codigo_disciplina = input("> #")
            if (len(codigo_disciplina) != 3):
                print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                print(cores.vermelho + "O código da disciplina deve ter 3 digitos" + cores.fim)
                print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                continue

            with open("codigos_disciplinas.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            if (f"#{codigo_disciplina}:\n" not in linhas):
                print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                print(cores.vermelho + "Essa disciplina não existe" + cores.fim)
                print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                continue

            if (acao_usuario == 1):
                retorno = aluno.adicionarDisciplina(codigo_disciplina)
                if (not retorno):
                    print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                    print(cores.vermelho + "Essa disciplina já foi cadastrada para este(a) aluno(a)" + cores.fim)
                    print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                    continue
            elif (acao_usuario == 2):
                retorno = aluno.removerDisciplina(codigo_disciplina)
                if (not retorno):
                    print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                    print(cores.vermelho + "Essa disciplina não existe neste(a) aluno(a)" + cores.fim)
                    print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
                    continue

