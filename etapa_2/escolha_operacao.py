# Peça dois números e permita escolher a operação (soma, subtração, etc.).
import os
os.system('clear')

print('~ Escolha o tipo de operação ~\n'
      '1. Soma\n'
      '2. Subtração\n'
      '3. Multiplicação\n'
      '4. Divisão\n')

operacao = int(input(''))
os.system('clear')

n1 = int(input('Insira o 1° número: '))
os.system('clear')
n2 = int(input('Insira o 2° número: '))
os.system('clear')

if operacao == 1:
    print('~ Operação de Soma ~')
    print(f'{n1} + {n2} = {n1 + n2}')
elif operacao == 2:
    print('~ Operação de Subtração ~')
    print(f'{n1} - {n2} = {n1 - n2}')
elif operacao == 3:
    print('~ Operação de Multiplicação ~')
    print(f'{n1} x {n2} = {n1 * n2}')
elif operacao == 4:
    print('~ Operação de Divisão ~')
    print(f'{n1} / {n2} = {n1 / n2}')
else:
    print('Operação Inexistente')