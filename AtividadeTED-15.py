# Desenvolva um programa utilizando os recursos que já vimos: if, elif, else, while, for, listas, dicionários.
# Não precisa utilizar todos, apenas os que julgar necessários.

# Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
# 1 - Cadastrar um funcionário
# 2 - Alterar um funcionário
# 3 - Listar (imprimir) todos os funcionários
# 4 - Excluir um funcionário
# 5 - Adicionar um aumento de salário

# Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, E-mail, Data de Admissão e Salário.


import random


controle = 1
cadastros = []

while controle != 0:
    #Painel principal
    print('='*100)
    print('1 - Cadastrar um funcionário')
    print('2 - Alterar um funcionario')
    print('3 - Listar todos os funcionários')
    print('4 - Excluir um funcionário')
    print('5 - Adicionar um aumento de salário')
    print('0 - encessar a sessão')
    print('\n')
    controle = int(input('Digite a opção: '))
    print('='*100)
    print('\n')
    
    if controle == 1:
        #Cadastrando um funcionario
        print('='*100)

        funcionario = {'Codigo': None, 'Nome': None, 'E-mail': None, 'Admissão': None, 'Salário': None}

        funcionario['Codigo'] = random.randint(1, 1000)
        gerando = 1
        codigos_gerados = []
        for c in range(0, len(cadastros)):
            cg = cadastros[c]
            codigos_gerados.append(cg['Codigo'])
        
        while gerando == 1:
            if cadastros == []:
                gerando = 0
            else:
                corrigindo = 1
                while corrigindo == 1:
                    codigo = random.randint(1, 1000)
                    if codigo not in codigos_gerados:
                        funcionario['Codigo'] = codigo
                        corrigindo = 0
                        gerando = 0

        funcionario['Nome'] = input('Digite o nome do funcionario: ')

        funcionario['E-mail'] = input('Digite o E-mail do funcionario: ')

        funcionario['Admissão'] = input('Digite a data de adimissão do funcionario: ')

        funcionario['Salário'] = float(input('Digite o salário(apenas numeros) do funcionario: '))

        cadastros.append(funcionario)

        print(f'Casdastro de funcionario concluido, codigo de cadastro é {funcionario["Codigo"]} , voltando ao painel principal.')
        print('='*100)
        print('\n')
        
    elif controle == 2:
        #Alterando informações de um funcionario
        
        codigo = int(input('Digite o codigo do funcionario que deseja realizar a alteração: '))
 
        for i in range(0, len(cadastros)):
            fc = cadastros[i]
            
            if (codigo == fc['Codigo']):
                opcoes = 1
                print(cadastros[i])
                while opcoes != 0:
    
                    print('1 - Alterar o Codigo')
                    print('2 - Alterar o nome')
                    print('3 - Alterar o E-mail')
                    print('4 - Alterar a data de admissão')
                    print('5 - Alterar o salario')
                    print('0 - encerrar a alteração')
                    print('\n')
                    opcoes = int(input('Digite a opção: '))

                    if opcoes == 1:
                        repetir = -1
                        while repetir == -1:
                            codigos_utilizados = []
                            NovoCodigo = int(input('Digite um novo codigo: '))
                            for f in cadastros:
                                codigos_utilizados.append(f['Codigo'])
                            if NovoCodigo in codigos_utilizados:
                                print('Tente Novamente')
                            else:
                                repetir = 0
                                fc['Codigo'] = NovoCodigo
                                print('\n')
                                print('Alteração concluida!')

                                
                    elif opcoes == 2:

                        fc['Nome'] = (input('Digite o novo Nome: '))
                        print('\n')
                        print('Alteração concluida!')
                    
                    elif opcoes == 3:

                        fc['E-mail'] = (input('Digite o novo E-mail: '))
                        print('\n')
                        print('Alteração concluida!')
                    
                    elif opcoes == 4:

                        fc['Admissão'] = (input('Digite a nova data de Admissão: '))
                        print('\n')
                        print('Alteração concluida!')
                    
                    elif opcoes == 5:

                        fc['Salário'] = float(input('Digite o novo salario(apenas numeros): '))
                        print('\n')
                        print('Alteração concluida!')
        print('='*100)
        print('\n')

    elif controle == 3:
        #Listando a lista de funcionario 

        print('='*100)    
        if cadastros == []:
            print('Sem cadastro')
        
        else:
            for f in cadastros:
                print(f)
                
            
        print('='*100)
        print('\n')
        

    elif controle == 4:
        #Excluindo um funcionario
        print('='*100)
        print('\n')
        codigo = int(input('Digite o codigo do funcionario que deseja excluir: '))
        fu_ex = 0
        for i in range(0, len(cadastros)):
            fc = cadastros[i]
                
            if (codigo == fc['Codigo']):
                print(fc)
                
                print('Deseja excluir esse funcionario?')
                print('0 - Não')
                print('1 - Sim')
                opcoes = input('Digte a opcão: ')

                if opcoes == '1':
                    fu_ex = fc
        if fu_ex == 0:
            pass
        else:
            cadastros.remove(fu_ex)
                    
        print('='*100)
        print('\n')
    elif controle == 5:
        #adicionando um salario de valor fixo a um funcionario
        print('='*100)
        codigo = int(input('Digite o codigo do funcionario que deseja dar um aumento: '))
            
        for i in range(0, len(cadastros)):
            fc = cadastros[i]
                
            if (codigo == fc['Codigo']):
                print(cadastros[i])
                
                Aumento = float(input('Digite quanto você quer adicionar de aumento (valor fixo) ao funcionario: '))
                fc['Salário'] = Aumento + fc['Salário']
        print('='*100)
        print('\n')

                    
    
    elif controle == 0:
        #finalizando do programa
        
        print("Sessão finalizada!")
