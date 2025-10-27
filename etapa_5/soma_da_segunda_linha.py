# Mostre a soma da segunda linha.
import os
import numpy as np
os.system('clear')

matriz = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

segunda_linha = matriz[1]

print(f'{matriz=}')
print(f'{segunda_linha=}')