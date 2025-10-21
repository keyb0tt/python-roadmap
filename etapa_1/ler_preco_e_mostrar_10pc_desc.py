# Leia o preço de um produto e mostre com 10% de desconto.
import os
os.system('clear')

preco_produto = int(input('Insira o preço do produto: R$'))

desconto_produto = preco_produto * 0.1

print(f'O Produto sairá R${(preco_produto - desconto_produto):.2f} após a aplicação do desconto')