# Peça números até digitar 0 e mostre a soma total.
import os
os.system('clear')
soma, cond = (0, 0)

while True:
    num = int(input('Insira um número para adicionar à soma ou 0 para encerrar: '))
    soma += num
    os.system('clear')

    if num == 0:
        break

print(f'A Soma total resulta em: {soma}')