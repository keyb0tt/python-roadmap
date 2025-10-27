# Mostre a matriz transposta.
import numpy as np
import os
os.system('clear')

matriz_original = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],])

matriz_transposta = matriz_original.T

print(f'Original:\n{matriz_original}\n')
print(f'Transposta:\n{matriz_transposta}\n')