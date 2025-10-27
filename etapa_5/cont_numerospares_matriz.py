# Conte quantos números pares há na matriz.
import numpy as np
import os
os.system('clear')

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],])

qnt_pares = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] % 2 == 0:
            qnt_pares += 1

print(matriz)
print(f'\n{qnt_pares=}')