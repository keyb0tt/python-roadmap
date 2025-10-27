# Leia uma matriz 3x3 e mostre seus elementos.
import os
os.system('clear')

matriz = []

for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f'Insira o {j+1}° elemento da coluna {i} e linha {j}: ')))

print(f'{matriz=}')

