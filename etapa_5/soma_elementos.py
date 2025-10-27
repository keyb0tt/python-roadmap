# Calcule a soma de todos os elementos.
import os
os.system('clear')

matriz = []
soma_elementos = 0

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        matriz[linha].append(int(input(f'Insira o {coluna+1}° elemento da {linha+1}ª linha e {coluna+1}ª coluna: ')))
        os.system('clear')

for linha in range(3):
    for coluna in range(3):
        soma_elementos += matriz[linha][coluna]

print(f'{matriz=}')
print(f'{soma_elementos=}')