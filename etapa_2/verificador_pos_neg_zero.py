# Verifique se um número é positivo, negativo ou zero.
import os
os.system('clear')

num = int(input('Insira o número para iniciar a verificação: '))

if num > 0:
    print(f'O Número {num} tem a propriedade positiva')
elif num < 0:
    print(f'O Número {num} tem a propriedade negativa')
elif num == 0:
    print(f'O Número {num} é igual a zero')
