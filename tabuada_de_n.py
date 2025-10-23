# Mostre a tabuada de um número informado.
import os
os.system('clear')

num = int(input('Insira um número para obter sua tabuada: '))

for i in range(10):
    print(f'{num} x {i + 1} = {num * (i + 1)}')