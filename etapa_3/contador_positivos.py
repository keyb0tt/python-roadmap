# Conte quantos números positivos foram digitados.
import os
os.system('clear')

num, qnt_par = (0, 0)

for i in range(5):
    num = int(input(f'({i+ 1}/5)Insira o {i + 1}° número: '))

    if num % 2 == 0:
        qnt_par += 1

    os.system('clear')

print(f'Foram inseridos {qnt_par} números pares')