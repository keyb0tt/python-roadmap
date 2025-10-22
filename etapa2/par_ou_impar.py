# Determine se um número é par ou ímpar.
import os
os.system('clear')

num = int(input('Insira o número para iniciar a verificação: '))

if num % 2 == 0:
    print('O Número é par')
else:
    print('O Número é ímpar')