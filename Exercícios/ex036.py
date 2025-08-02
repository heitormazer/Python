#Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo
#bancário sera negado.
casa = float(input('Qual o valor da casa? '))
salario = float(input('Informe o seu salário: '))
anos = float(input('Em quantos anos você vai pagar?'))

meses = anos * 12
prestacao = casa / meses
limite = salario * 0.30

print(f'Para pagar uma casa de valor R${casa:.2f} em {anos:.0f} anos. A prestação será de R${prestacao:.2f}')

if prestacao <= limite:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado! A prestação excede 30% do salário.')