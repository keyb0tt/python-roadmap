# Converta temperatura de Celsius para Fahrenheit.
import os
os.system('clear')

temp_celsius = float(input('Insira a temperatura em Celsius: '))

temp_fahr = (temp_celsius * 1.8) + 32

print(f'{temp_celsius}°C é igual a {temp_fahr:.0f}°F')