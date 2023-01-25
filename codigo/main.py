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
        codDisciplina = dados[0]
        nomeDisciplina = dados[1]
        dicio[codDisciplina] = nomeDisciplina
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
            nome = input("> ")
            print("Código da disciplina:")
            codDisci = input("> #")
            Disciplina(ch, nome, codDisci)
            linha = f"#{codDisci}:{nome}:{ch}:\n"

            with open("disciplinas.txt", 'a') as arquivo:
                arquivo.write(linha)
        elif (acao == 2):
            print("Digite o código da disciplina:")
            opc2 = input('#')
            disciplina = Disciplina(chDic, nomeDic, codDic)
            Disciplina.emitirRelatorio()
        elif (acao == 3):
            print("Até breve...")
            break

"""
Cadastrar disciplina vai fazer com que o usuario informe um codigo, um nome e a carga horaria da disciplina. Depois disso um objeto vai ser instanciado com os dados informados.
Caso um codigo de disciplina ja existir, avisar o user.

Emitir o relatorio de uma disciplina vai pegar os dados da disciplina no dicionario usando o codigo da disciplina informado pelo user.
"""