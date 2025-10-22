# Peça a idade e diga se pode votar.
import os
os.system('clear')

idade_eleitor = int(input('Insira a sua idade: '))

if idade_eleitor >= 18:
    print('Você tem direito a voto')
else:
    print('Você não tem direito a voto')
