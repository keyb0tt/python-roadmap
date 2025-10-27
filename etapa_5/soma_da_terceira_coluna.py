# Calcule a soma da terceira coluna.
import os
import numpy as np
os.system('clear')

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

soma_colunas = np.sum(matriz, axis=0)
soma_terceira_coluna = soma_colunas[2]

print(f'{soma_terceira_coluna=}')