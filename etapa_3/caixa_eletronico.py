# Simule um caixa eletrônico pedindo saque e mostrando notas necessárias.
import os
os.system('clear')

saque_valor = int(input('Insira a quantidade a ser sacada: R$'))
os.system('clear')

saque_var = saque_valor

notas_valores = [100, 50, 20, 10, 5, 2]
notas_quantidades = [0, 0, 0, 0, 0, 0]

for i in range(len(notas_valores)):
    while saque_var >= notas_valores[i]:
        saque_var -= notas_valores[i]
        notas_quantidades[i] += 1

print(f'~ Quantidade de notas recebidas ~\n\nValor: R${saque_valor}\n')

for i in range(len(notas_quantidades)):
    if notas_quantidades[i] > 0:
        print(f'Notas de R${notas_valores[i]},00 = {notas_quantidades[i]}')
