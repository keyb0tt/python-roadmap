# Peça notas de alunos e mostre a maior e menor nota.
import os 
os.system('clear')

notas_1aluno = []
notas_2aluno = []
notas_3aluno = []

for aluno in range(3):
    for i in range(3):
        print(f'Aluno {aluno + 1}:')
        if aluno == 0:
            notas_1aluno.append(int(input(f'Insira a {i+1}ª nota: ')))
            os.system('clear')
        elif aluno == 1:
            notas_2aluno.append(int(input(f'Insira a {i+1}ª nota: ')))
            os.system('clear')
        elif aluno == 2:
            notas_3aluno.append(int(input(f'Insira a {i+1}ª nota: ')))
            os.system('clear')

notas = [*notas_1aluno, *notas_2aluno, *notas_3aluno]
maior_nota = max(notas)

print(f'{notas=}')
print(f'{maior_nota=}')