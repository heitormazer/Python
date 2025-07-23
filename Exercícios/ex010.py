#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere U$ 1.00 = 3.27
din = float(input('Quantos reais você tem: '))
dindol = din * 3.27
print(f'Você tem {din} reais, e {dindol:.2f} doláres')