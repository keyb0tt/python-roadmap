import os
import numpy as np
os.system('clear')

primeira_matriz = np.array([[1, 2],
                            [3, 4],])

segunda_matriz = np.array([ [5, 6],
                            [7, 8],])

matriz_soma = np.sum(primeira_matriz + segunda_matriz) 

print(primeira_matriz, '\n')
print(segunda_matriz, '\n')
print(f'Soma das matrizes: {matriz_soma}')