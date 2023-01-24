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