from funcoes import validar_arquivo, validar_acao_usuario, menu_disciplina
from cores import Cores
from disciplina import Disciplina
nomes_arquivos = ["disciplinas.txt", "codigos_disciplinas.txt", "professores.txt", "alunos.txt"]
cores = Cores()

for nome in nomes_arquivos:
    validar_arquivo(nome)

while True:
    print("\n(1)Disciplinas\n(2)Alunos\n(3)Professores\n(0)Encerrar o programa\n")
    acao_usuario = validar_acao_usuario("> ")

    if (acao_usuario == 0):
        print(cores.verde + "\nAté breve!")
        print("=)" + cores.fim)
        break
    elif (acao_usuario == ""):
        continue
    elif (acao_usuario == 1):
        retorno = False
        while (not retorno):
            retorno = menu_disciplina()
