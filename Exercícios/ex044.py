#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#Á vista dinheiro/pix: 10% de desconto
#Á vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
from enum import nonmember

valor = float(input('Digite o preço do produto que irá ser comprado: '))
print('Escolha o método de pagamento \n '
      '1- Dinheiro/Pix: 10% de desconto \n '
      '2- Cartão: 5% de desconto \n '
      '3- 2x no cartão: Preço normal \n '
      '4- 3x no cartão ou mais: 20% de juros.')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    total = valor * 0.90
elif opcao == 2:
    total = valor * 0.95
elif opcao == 3:
    total = valor
    print(f'Valor por parcela: R$ {total/2:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = valor * 1.20
    print(f'Valor por parcela: R$ {total/parcelas:.2f}')
else:
    print('Opção Invalida.')
    total = 0

if total != 0:
    print(f'Valor final a pagar R${total:.2f} ')
