# Some duas listas elemento a elemento.
import os 
os.system('clear')

lista_um = [1, 2, 3, 4, 5]
lista_dois = [5, 4, 3, 2, 1]
lista_soma = []

for i in range(len(lista_um)):
    lista_soma.append(lista_um[i] + lista_dois[i])

print(f'{lista_um=}')
print(f'{lista_dois=}')
print(f'{lista_soma=}')