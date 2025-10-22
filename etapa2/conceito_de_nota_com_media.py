# Calcule o conceito de nota (A, B, C...) com base em uma média.
import os
os.system('clear')

nota1 = int(input('Insira a sua 1° nota: '))
os.system('clear')
nota2 = int(input('Insira a sua 2° nota: '))
os.system('clear')
nota3 = int(input('Insira a sua 3° nota: '))
os.system('clear')

qnt_notas = 3
media = (nota1 + nota2 + nota3) / qnt_notas

if media >= 9:
    conceito_nota = 'A'
elif media <= 8.9 and media >= 7.5:
    conceito_nota = 'B' 
elif media <= 7.4 and media >= 5:
    conceito_nota = 'C'
else:
    conceito_nota = 'F'

print(f'Sua média foi de {media:.2f}, equivalente ao conceito de {conceito_nota}')