# Verifique se três lados podem formar um triângulo.
import os
os.system('clear')

lado1 = int(input('Insira o tamanho do 1° lado do triângulo (em cm): '))
os.system('clear')
lado2 = int(input('Insira o tamanho do 2° lado do triângulo (em cm): '))
os.system('clear')
lado3 = int(input('Insira o tamanho do 3° lado do triângulo (em cm): '))
os.system('clear')

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print('Os lados inseridos não podem formar um triângulo')
else:
    print('Os lados inseridos podem formar um triângulo')
