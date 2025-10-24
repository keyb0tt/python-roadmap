# Leia 5 números e mostre-os na ordem inversa.
import os
os.system('clear')

array_size = int(input('Insira o tamanho da array: '))
array_root = []

for i in range(array_size):
    array_root.append(int(input(f'Insira o {i + 1}° elemento da array: ')))

# Método convencional (mais parecido com C)
# for i in range(array_size, 0, -1): 
#     print(array_root[i - 1])

# Método mais típico do python
for element in reversed(array_root):
    print(element)
