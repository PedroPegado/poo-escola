class Pessoa:
    def __init__(self, matricula):
        self.matricula = matricula
        self.codigosDisciplinas = []
    
    def alterarDisciplina(self, codigoDisciplina, arquivoPessoa):
        with open(arquivoPessoa, 'r') as arquivo:
            banco = arquivo.readlines()
        
        for linha in banco:
            ind_prof = linha.split(':')
            if ind_prof[0] == self.matricula:
                indice = banco.index(linha)
                break
        
        splitado = banco[indice].split(':')
        
        print('1 - ADICIONAR\n2 - EXCLUIR')
        opc_user = int(input('> '))
        
        if opc_user == 1:
            indice_add  = splitado.index('\n')
            
            if f'#{codigoDisciplina}' not in splitado:
                splitado.insert(indice_add, f'#{codigoDisciplina}')
            else:
                print('Disciplina já cadastrada nesse professor.')
            
            cont = 0
            novo_prof = ''
            
            for ind in splitado:
                if cont == len(splitado) - 1:
                    novo_prof += f'{ind}'
                else:
                    novo_prof += f'{ind}:'
                cont+=1
            
            banco[indice] = novo_prof
            
            with open('professores.txt', 'w') as arquivo:
                arquivo.writelines(banco)
            
        elif opc_user == 2:
            if f'#{codigoDisciplina}' not in splitado:
                print('Disciplina não cadastrada nesse professor.')
            else:
                for ind in splitado[2:]:
                    if ind[0:3] == f'#{codigoDisciplina}':
                        splitado.remove(ind)
            
                cont = 0
                novo_prof = ''
                
                for ind in splitado:
                    if cont == len(splitado) - 1:
                        novo_prof += f'{ind}'
                    else:
                        novo_prof += f'{ind}:'
                    cont+=1
                
                banco[indice] = novo_prof
                
                with open('professores.txt', 'w') as arquivo:
                    arquivo.writelines(banco)
        
        
        