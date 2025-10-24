# Leia 10 números e mostre a soma total.
import os
os.system('clear')

array_numeros = []
qnt_numeros = int(input('Insira a quantidade de números a serem somados: ')) 

for i in range(qnt_numeros):
    array_numeros.append(int(input(f'Insira o {i+1}° n')))