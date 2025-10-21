# Calcule o tempo que um carro leva para percorrer uma distância a certa velocidade.
import os
os.system('clear')

velocidade_km_h = int(input('Insira a velocidade em km/h do veículo: '))
distancia_km = int(input('Insira a distância a ser percorrida em km: '))

tempo_horas = 0
while distancia_km >= velocidade_km_h:
    tempo_horas += 1
    distancia_km -= velocidade_km_h

tempo_minutos = 0
velocidade_km_m = velocidade_km_h / 60
while distancia_km >= velocidade_km_m:
    tempo_minutos += 1
    distancia_km -= velocidade_km_m

tempo_segundos = 0
velocidade_km_s = velocidade_km_m / 60
while distancia_km >= velocidade_km_s:
    tempo_segundos += 1
    distancia_km -= velocidade_km_s


print(f'\nO veículo irá percorrer o trajeto em {tempo_horas}h {tempo_minutos}m {tempo_segundos}s\n')
