from aluno import Aluno
from disciplina import Disciplina
from professor import Professor


def checaExiste(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            pass
    except: 
        with open(nomeArquivo, 'w') as arquivo:
            pass

for c in ['alunos.txt', 'professores.txt', 'disciplinas.txt']:
    checaExiste(c)

with open('disciplinas.txt', 'r') as arquivo:
    bancoDados = arquivo.readlines()

dicio = {}

for linha in bancoDados:
    dados = linha.split(':')
    coddis = dados[0]
    nomedisc = dados [1]
    dicio[coddis] = nomedisc

print(dicio)

while True:
    print('''DIGITE A OPÇÃO DESEJADA:
    1 - CRIAR DISCIPLINA
    2 - EMITIR RELATÓRIO DE DISCIPLINA''')
    opc = int(input('> '))
    if opc == 1:
        ch = int(input('Carga horaria > '))
        nome = str(input('Nome > '))
        codDisci = input('#')
        Disciplina(ch, nome, codDisci)
    elif opc == 2:
        opc2 = input('Digite o código da disciplina > ')
        Disciplina.emitirRelatorio(dicio[opc2]) 