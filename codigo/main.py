from aluno import Aluno
from disciplina import Disciplina
from funcoes import checa_arquivo_existe, estrutura_disciplina, estrutura_professor, estrutura_aluno
from professor import Professor

for index,nome in enumerate(['alunos.txt', 'professores.txt', 'disciplinas.txt']):
    if (index == 0):
        dados_aluno = checa_arquivo_existe(nome)
    elif (index == 1):
        dados_professor = checa_arquivo_existe(nome)
    else:
        dados_disciplina = checa_arquivo_existe(nome)

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

try:
    for linhas in dados_professor:
        dados = linhas.split(':')
        matricula = dados[0]
        nome = dados[1]
        disciplinas_professor = dados[2:len(dados) - 1]
        try:
            professores_dic[matricula] = [nome, disciplinas_professor[0].split(',')]
        except:
            professores_dic[matricula] = [nome, "None"]
except TypeError as error:
    pass

try:
    for linha in dados_aluno:
        dados = linha.split(':')
        matricula = dados[0]
        disciplinas_aluno = dados[2:len(dados) - 1]
        alunos_dic[matricula] = [dados[1], disciplinas_aluno[0].split(':')]
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
            retorno = estrutura_professor(professores_dic, disciplinas_dic)
            if retorno == None:
                pass
            else:
                professores_dic = retorno

        elif acao_usuario == 3:
            retorno = estrutura_aluno(alunos_dic, disciplinas_dic)
            if retorno == None:
                pass
            else:
                alunos_dic = retorno
            
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
212:Gilbran Andrade:#001,#002:\n
---Disciplinas---
codigoDisciplina:nome:cargaHoraria:\n
#001:PEOO:160:\n

FORMATAÇÃO DOS DICIONÁRIOs
---Alunos---
{matricula: ['Nome', ["#001,100,20,40,80", "#002, 0, 50, 60, 100"]]}

---Professores---
{'212': ['Gilbran Andrade', ['#001', '#002']]}

---Disciplinas---
{'#001': ['PEOO', '120']}
"""
