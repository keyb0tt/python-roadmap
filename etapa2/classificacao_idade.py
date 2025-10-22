# Classifique uma pessoa com base na idade (criança, jovem, adulto, idoso).
import os
os.system('clear')

idade = int(input('Insira a sua idade: '))

if idade <= 11:
    classificacao_idade = 'Criança'
elif idade >= 12 and idade <= 19:
    classificacao_idade = 'Jovem/Adolescente'
elif idade >= 20 and idade <= 59:
    classificacao_idade = 'Adulto'
else:
    classificacao_idade = 'Idoso'

print(f'A Classificação correspondente à sua idade é de {classificacao_idade}')
