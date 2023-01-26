from aluno import Aluno
from disciplina import Disciplina
from professor import Professor


def checaExiste(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            if (nomeArquivo == "disciplinas.txt"):
                dadosDisciplinas = arquivo.readlines()
                return dadosDisciplinas
    except: 
        with open(nomeArquivo, 'w') as arquivo:
            pass
    

for nome in ['alunos.txt', 'professores.txt', 'disciplinas.txt']:
    dados_disciplina = checaExiste(nome)

disciplinas_dic = {}

try:
    for linha in dados_disciplina:
        dados = linha.split(':')
        codigo_disciplina = dados[0]
        disciplinas_dic[codigo_disciplina] = dados[1:3]
except TypeError as error:
    pass

while True:
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - CRIAR DISCIPLINA
    2 - EMITIR RELATÓRIO DE DISCIPLINA
    3 - ENCERRAR O PROGRAMA''')

    try:
        acao_usuario = int(input('> '))
    except:
        print("Ação inválida.")
    else:
        if (acao_usuario == 1):
            print("Carga horaria:")
            carga_horaria = int(input("> "))
            print("Nome da disciplina:")
            nome_disciplina = input("> ")
            print("Código da disciplina:")
            codigo_disciplina = input("> #")

            disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)

            linha = f"#{codigo_disciplina}:{nome_disciplina}:{carga_horaria}:\n"

            with open("disciplinas.txt", 'a') as arquivo:
                arquivo.write(linha)
        elif (acao_usuario == 2):
            print("Digite o código da disciplina:")
            codigo_disciplina = input('#')
            materia = disciplinas_dic.get(f'#{codigo_disciplina}')
            if (materia == None):
                print('Matéria inexistente')
                continue
            else:
                nome_disciplina = materia[0]
                carga_horaria = materia[1]
                disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)
                disciplina.emitirRelatorio()
        elif (acao_usuario == 3):
            print("Até breve...")
            break

"""
TO-DOs
-o- Funções para o menu de disciplina, aluno e professor.
-o- Planejar diagrama de classes da interface gráfica (Kivy e KivyMD).
-o- Atualizar o README.md com instruções para utilizar a interface gráfica (Kivy e KivyMD).
-o- ...
-o- ...
-o- ...

ORGANIZAÇÃO DOS ARQUIVOS
---Alunos---
matricula:nome:codigoDisciplina, notas:\n
---Professores---
matricula:nome:codigoDisciplinas:\n
---Disciplinas---
codigoDisciplina:nome:cargaHoraria:\n
"""