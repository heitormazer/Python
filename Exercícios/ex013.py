#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salar = float(input('Salário atual: '))
aumen = float(input('Porcentagem de aumento: '))
valaumen = salar * (aumen / 100)
salarfin = valaumen + salar
print(f'O salário atual com {aumen:.2f}% de aumento fica R${salarfin:.2f}')