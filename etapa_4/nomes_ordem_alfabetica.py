import os
os.system('clear')

nomes = []
NOMES_SIZE = 5

for i in range(NOMES_SIZE):
    nomes.append(str(input(f'Insira o {i+1}° nome: ')))
    os.system('clear')

print(f'Array original: {nomes=}')

nomes.sort()

print(f'Array em ordem alfabética: {nomes=}')