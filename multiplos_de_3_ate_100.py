# Mostre os múltiplos de 3 até 100.
import os
os.system('clear')

for i in range (1, 101):
    if i % 3 == 0:
        print(f'{i} ', end = '')