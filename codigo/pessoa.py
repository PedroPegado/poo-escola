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
            
            if len(self.matricula) == 6:
                if f'#{codigoDisciplina}' not in splitado:
                    splitado.insert(indice_add, f'#{codigoDisciplina}')
                else:
                    print('Disciplina já cadastrada nesse professor.')
            
            
            elif len(self.matricula) == 14:
                
                check = 0
                
                for ind in splitado:
                    if f'#{codigoDisciplina}' == ind[0:4]: 
                        print('Disciplina já cadastrada nesse aluno.')
                        check += 1
                        break
                
                if check == 0:
                    splitado.insert(indice_add, f'#{codigoDisciplina},0,0,0,0')
                    
            cont = 0
            novo_pessoa = ''
            
            for ind in splitado:
                if cont == len(splitado) - 1:
                    novo_pessoa += f'{ind}'
                else:
                    novo_pessoa += f'{ind}:'
                cont+=1
            
            banco[indice] = novo_pessoa
            
            with open(arquivoPessoa, 'w') as arquivo:
                arquivo.writelines(banco)
                
        elif opc_user == 2:
            if len(self.matricula) == 6:
                if f'#{codigoDisciplina}' not in splitado:
                    print('Disciplina não cadastrada nesse professor.')
                else:
                    for ind in splitado[2:]:
                        if ind[0:3] == f'#{codigoDisciplina}':
                            splitado.remove(ind)
            
            elif len(self.matricula) == 14:
                check = 0
                
                for ind in splitado:
                    if f'#{codigoDisciplina}' != ind[0:4]:
                        check = 1
                    else:
                        check = 0
                        break

                
                if check == 1:
                    print('Disciplina não cadastrada nesse aluno.')
                elif check == 0:
                    for ind in splitado:
                        if f'#{codigoDisciplina}' in ind:
                            splitado.remove(ind)
                
                print(splitado)
                     
            cont = 0
            novo_pessoa = ''
            
            for ind in splitado:
                if cont == len(splitado) - 1:
                    novo_pessoa += f'{ind}'
                else:
                    novo_pessoa += f'{ind}:'
                cont+=1
            
            banco[indice] = novo_pessoa
            
            with open(arquivoPessoa, 'w') as arquivo:
                arquivo.writelines(banco)
            
        
        
        