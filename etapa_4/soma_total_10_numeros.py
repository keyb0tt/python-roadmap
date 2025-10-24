# Leia 10 números e mostre a soma total.
import os
os.system('clear')

array_numeros = []
soma_numeros = 0
qnt_numeros = int(input('Insira a quantidade de números a serem somados: ')) 
os.system('clear')

for i in range(qnt_numeros):
    array_numeros.append(int(input(f'Insira o {i+1}° número: ')))
    os.system('clear')

for numero in array_numeros:
    soma_numeros += numero

print(f'{array_numeros=}\n')
print(f'{soma_numeros=}')