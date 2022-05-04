#Faça um algoritmo para ler 20 números e armazenar em um vetor. 
# Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa


import random


numeros = []

for linha in range(1 ,21):
    numero_gerado = random.randrange(1, 20)
    numeros.append(numero_gerado)
print(numeros)

numeros.reverse()

print(numeros)