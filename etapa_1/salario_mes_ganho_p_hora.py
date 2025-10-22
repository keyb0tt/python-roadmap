# Leia o salário e mostre quanto ganha por hora (considerando 160h/mês).
import os
os.system('clear')

salario_mes = int(input('Insira a sua renda salarial por mês: '))
qnt_horas_mes, qnt_horas_dia = {160, 24}
salario_dia = salario_mes / (qnt_horas_mes / qnt_horas_dia)
salario_hora = salario_dia / qnt_horas_dia 

print(f'Um salário de R${salario_mes:.2f} por mês trabalhando 160h ao mês rende R${salario_hora:.2f}/h')