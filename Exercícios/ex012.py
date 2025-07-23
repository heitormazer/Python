#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço atual do produto: '))
desco = float(input('Desconto %:'))
vadesc = preco * (desco / 100)
precofi = preco - vadesc
print(f'O preço do produto com {desco:.2f}%, então o preço do produto fica R${precofi:.2f}.')