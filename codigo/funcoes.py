from cores import Cores
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

def menu_disciplina():
    print("\nInforme o codigo de disciplina")
    codigo_disciplina = input("> #")

    if (len(codigo_disciplina) != 3):
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
        print(cores.vermelho + "O código da disciplina deve ter 3 digitos" + cores.fim)
        print(cores.pisca + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + cores.fim)
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

