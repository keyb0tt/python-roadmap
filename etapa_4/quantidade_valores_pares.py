import os
os.system('clear')

array_valores = []
ARRAY_SIZE, cont_pares = (5, 0)

for i in range(ARRAY_SIZE):
    array_valores.append(int(input(f'Insira o {i+1}° valor: ')))
    os.system('clear')

for valor in array_valores:
    if valor % 2 == 0:
        cont_pares += 1

print(f'{cont_pares=}')