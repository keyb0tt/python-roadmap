import os
os.system('clear')

lista_valores = [10, 5, 7, 2, 20, 3]
maior_valor, menor_valor = 10, 10

for valor in lista_valores:
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

print(maior_valor)
print(menor_valor)