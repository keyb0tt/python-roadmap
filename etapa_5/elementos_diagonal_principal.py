# Mostre os elementos da diagonal principal.
import os
import numpy as np
os.system('clear')

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal_principal = np.diag(matriz)

print(f'{matriz}')
print(f'{diagonal_principal}')