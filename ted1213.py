from time import sleep
glossário={'Algotitmo':' pode ser definido como uma sequência de passos que visam a atingir um objetivo bem definido – FORBELLONE, 2005',
            'Teste de mesa':' Trata-se de um processo manual para análise e verificação do comportamento de uma algoritmo —BATISTA, MESSIAS',
            'Dado':' são símbolos ou signos não estruturados,sem significado, como valores em uma tabela.',
            'Variável':'um dado é classificado como variavel quando tem a possibilidade de ser alterado em algum instante no decorrer do tempo.',
            'Contante':'quando um dado não sofre nenhuma variação no decorrer do tempo.'}
for i in glossário:
    sleep(1)
    print('\n************************************************************************************')
    print(f'{i} :{glossário[i]}')