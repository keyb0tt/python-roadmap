import os
import numpy as np
os.system('clear')

matriz = np.zeros((3, 3), dtype=int)
                  
np.fill_diagonal(matriz, 1)
print(matriz)
