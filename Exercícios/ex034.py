#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%w
#Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Qual o seu sarário atual? '))
if salario > 1250.00:
    nov_salario = salario + (salario * 0.10)
else:
    nov_salario = salario + (salario * 0.15)
print(f'Antes você ganhava R${salario}, agora irá ganhar R${nov_salario:.2f}')