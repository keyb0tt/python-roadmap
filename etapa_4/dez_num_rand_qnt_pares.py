# Gere 10 números aleatórios e mostre quantos são pares.
import os
import random
os.system('clear')

numeros = []
numeros_pares = []
contagem_pares = 0

for i in range(5):
    numeros.append(int(random.randint(1, 50)))
    if numeros[i] % 2 == 0:
        numeros_pares.append(int(numeros[i]))
        contagem_pares += 1

print(f'{numeros=}')
print(f'{numeros_pares=}')
print(f'{contagem_pares=}')