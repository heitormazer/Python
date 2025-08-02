#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print(f'O primeiro é o número maior!')
elif num1 < num2:
    print(f'O segundo é o número maior')
else:
    print(f'Não existe valor maior, os dois são iguais!')
