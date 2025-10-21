# Peça um número e mostre o dobro, triplo e raiz quadrada.
import os
os.system('clear')

n1 = int(input('Insira o número desejado: '))

dobro = n1 * 2
triplo = n1 * 3
raiz_quadrada = n1 ** 0.5

print(f'{n1} x 2 = {dobro}')
print(f'{n1} x 3 = {triplo}')
print(f'Raiz² de {n1} = {raiz_quadrada}')