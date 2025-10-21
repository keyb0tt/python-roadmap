# Leia três números e calcule a média.
import os
os.system('clear')

print('Insira o primeiro número: ')
n1 = int(input())

print('\nInsira o segundo número: ')
n2 = int(input())

print('\nInsira o terceiro número: ')
n3 = int(input())

media = (n1 + n2 + n3) / 3

print(f'A Média dos números é igual a {media}')