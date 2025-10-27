# Multiplique uma matriz por um escalar.
import os
import numpy as np
os.system('clear')

matriz = np.array([ [1, 2],
                    [3, 4]])

escalar = 2
matriz_resultado = np.multiply(matriz, escalar) 

print(matriz_resultado)