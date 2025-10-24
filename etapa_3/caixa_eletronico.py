# Simule um caixa eletrônico pedindo saque e mostrando notas necessárias.
import os
os.system('clear')

saque_valor = int(input('Insira a quantidade a ser sacada: R$'))
os.system('clear')

saque_var = saque_valor
nota_100, nota_50, nota_20, nota_10, nota_5, nota_2 = (100, 50, 20, 10, 5, 2)
qnt_100, qnt_50, qnt_20, qnt_10, qnt_5, qnt_2, notas_range = (0, 0, 0, 0, 0, 0, 6)

# if saque_var >= nota_100:
    # while True:
        # if saque_var >= nota_100:
            # saque_var -= nota_100
            # qnt_100 += 1
        # else:
            # break
# if saque_var >= nota_50:
    # while True:
        # if saque_var >= nota_50:
            # saque_var -= nota_50
            # qnt_50 += 1
        # else:
            # break
# if saque_var >= nota_20:
    # while True:
        # if saque_var >= nota_20:
            # saque_var -= nota_20
            # qnt_20 += 1
        # else:
            # break
# if saque_var >= nota_10:
    # while True:
        # if saque_var >= nota_10:
            # saque_var -= nota_10
            # qnt_10 += 1
        # else:
            # break
# if saque_var >= nota_5:
    # while True:
        # if saque_var >= nota_5:
            # saque_var -= nota_5
            # qnt_5 += 1
        # else:
            # break
# if saque_var >= nota_2:
    # while True:
        # if saque_var >= nota_2:
            # saque_var -= nota_2
            # qnt_2 += 1
        # else:
            # break

notas_valores = [nota_100, nota_50, nota_20, nota_10, nota_5, nota_2]
notas_quantidades = [qnt_100, qnt_50, qnt_20, qnt_10, qnt_5, qnt_2]
notas_ordem = ['R$100,00', 'R$50,00','R$20,00','R$10,00','R$5,00','R$2,00',]

for i in range(notas_range):
    while saque_var >= notas_valores[i]:
        saque_var -= notas_valores[i]
        notas_quantidades[i] += 1

print(f'~ Quantidade de notas recebidas ~\n\nValor: R${saque_valor}\n')

for i in range(notas_range):
    if notas_quantidades[i] > 0:
        print(f'Notas de {notas_ordem[i]} = {notas_quantidades[i]}')
