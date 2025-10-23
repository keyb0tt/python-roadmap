# Conte quantos números pares há entre 1 e 50.
import os
os.system('clear')
count = 0

for i in range(1, 51):
    if i % 2 == 0:
        count += 1
        print(f'{i}')
        
print(f'Entre 1 e 50 existem {count} números pares')