# Calcule o fatorial de um número.
import os
os.system('clear')

num = int(input('Escolha um número para obter seu fatorial: '))
fatorialResult = num

os.system('clear')

for i in range(1, num):
    fatorialResult *= (num - i)

print(f'Fatorial de {num} = {fatorialResult}')