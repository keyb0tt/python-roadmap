# Calcule o maior entre três números.
import os
os.system('clear')

n1 = int(input('Insira o 1° número: '))
os.system('clear')
n2 = int(input('Insira o 2° número: '))
os.system('clear')
n3 = int(input('Insira o 3° número: '))
os.system('clear')

if n1 > n2:
    maior = n1
elif n3 > n2:
    maior = n3
else:
    maior = n2

print(f'O Maior número inserido foi {maior}')