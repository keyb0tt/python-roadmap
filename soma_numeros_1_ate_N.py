# Some os números de 1 até N.
import os
os.system('clear')

num = int(input('Insira o número alvo: '))

sum = 0
for i in range(1, num + 1):
    sum += i


print(f'Soma de 1 até {num} = {sum}')

