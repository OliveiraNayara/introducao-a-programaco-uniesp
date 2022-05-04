#Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.



import random

VET = []

for x in range(50):
    
    VET.append(random.randint(0, 100))


print(f'O vetor gerado foi: {VET}')


for i in range(0, len(VET)):
    
    print(f'VALOR TESTADO: {VET[i]} | ÍNDICE TESTADO: {i}')
    
    for j in range(0, len(VET)):
        
        if VET[i] == VET[j] and i != j:
            print(f'Índice: {j} | Valor: {VET[j]}')