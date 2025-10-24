# Peça 5 números e mostre o maior.
import os
os.system('clear')

maior_num = 0

for i in range(5):
    num = int(input(f'Insira o {i + 1}° número: '))
    if num > maior_num:
        maior_num = num

print(f'O maior número inserido foi: {maior_num}')

