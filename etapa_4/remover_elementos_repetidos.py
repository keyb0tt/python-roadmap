# Crie uma lista e remova elementos repetidos.
import os
os.system('clear')

numeros = [1, 1, 1, 2, 3, 4, 5, 5, 5]
numeros_norep = list(set(numeros))

print(f'{numeros=}')
print(f'{numeros_norep=}')