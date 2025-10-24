# Calcule a média dos elementos de uma lista.
import os
os.system('clear')

numeros = [10, 5, 7]
soma_numeros = 0
media = 0

for numero in numeros:
    soma_numeros += numero

media = soma_numeros / len(numeros)

print(f'{media=:.1f}')