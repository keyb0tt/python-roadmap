# Converta metros em centímetros e milímetros.
import os
os.system('clear')

metros_qnt = int(input('Insira uma quantidade em metros: '))

cm_qnt = metros_qnt * 100
mm_qnt = metros_qnt * 1000

print(f'Quantidade convertida em centímetros: {cm_qnt}')
print(f'Quantidade convertida em milímetros: {mm_qnt}')
