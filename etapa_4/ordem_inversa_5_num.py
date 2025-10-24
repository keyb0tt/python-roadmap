import os
os.system('clear')

array_size = int(input('Insira o tamanho da array: '))
array_root = []

for i in range(array_size):
    array_root.append(int(input(f'Insira o {i + 1}° elemento da array: ')))

for array_size in range(0):
    print(array_root[array_size])
