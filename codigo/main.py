from funcoes import validar_arquivo, validar_acao_usuario, menu_disciplina, menu_aluno, menu_professor
from cores import Cores

nomes_arquivos = ["disciplinas.txt", "codigos_disciplinas.txt", "professores.txt", "matriculas_professores.txt", "alunos.txt", "matriculas_alunos.txt"]
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
    elif (acao_usuario == 2):
        retorno = False
        while (not retorno):
            retorno = menu_aluno()
    elif (acao_usuario == 3):
        retorno = False
        while (not retorno):
            retorno = menu_professor()
