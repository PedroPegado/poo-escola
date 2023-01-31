from aluno import Aluno
from disciplina import Disciplina
from funcoes import checa_existe, estrutura_disciplina
from professor import Professor

for nome in ['alunos.txt', 'professores.txt', 'disciplinas.txt']:
    dados_disciplina = checa_existe(nome)

disciplinas_dic = {}
professores_dic = {}
alunos_dic = {}

try:
    for linha in dados_disciplina:
        dados = linha.split(':')
        codigo_disciplina = dados[0]
        disciplinas_dic[codigo_disciplina] = dados[1:3]
except TypeError as error:
    pass

while True:
    print('''\nDIGITE A OPÇÃO DESEJADA:
    1 - DISCIPLINA
    2 - PROFESSOR
    3 - ALUNO
    0 - SAIR''')

    try:
        acao_usuario = int(input('> '))
    except:
        print("Ação inválida.")
    else:
        if acao_usuario == 1:
            retorno = estrutura_disciplina(disciplinas_dic)
            if (retorno == None):
                pass
            else:
                disciplinas_dic = retorno

        elif acao_usuario == 2:
            retorno = estrutura_professor(professores_dic)

        elif acao_usuario == 3:
            retorno = estrutura_aluno(alunos_dic)
            
        elif acao_usuario == 0:
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

FORMATAÇÃO DOS ARQUIVOS
---Alunos---
matricula:nome:codigoDisciplina, notas:\n
---Professores---
matricula:nome:codigoDisciplinas:\n
---Disciplinas---
codigoDisciplina:nome:cargaHoraria:\n

FORMATAÇÃO DOS DICIONÁRIOs
---Alunos---
---Professores---
{'matricula': ['Nome']}
---Disciplinas---
{'#001': ['PEOO', 120]}
"""