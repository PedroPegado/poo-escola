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
    bancoDados = checaExiste(nome)

dicio = {}

try:
    for linha in bancoDados:
        dados = linha.split(':')
        coddis = dados[0]
        nomedisc = dados [1]
        dicio[coddis] = nomedisc
    
    print(dicio)
except TypeError as error:
    pass

while True:
    print('''DIGITE A OPÇÃO DESEJADA:
    1 - CRIAR DISCIPLINA
    2 - EMITIR RELATÓRIO DE DISCIPLINA
    3 - ENCERRAR O PROGRAMA''')

    try:
        acao = int(input('> '))
    except:
        print("Ação inválida.")
    else:
        if (acao == 1):
            print("Carga horaria:")
            ch = int(input("> "))
            print("Nome da disciplina:")
            nome = str(input("> "))
            print("Código da disciplina:")
            codDisci = input("> #")
            Disciplina(ch, nome, codDisci)
        elif (acao == 2):
            print("Digite o código da disciplina:")
            opc2 = input('#')
            Disciplina.emitirRelatorio()
        elif (acao == 3):
            print("Até breve...")
            break
