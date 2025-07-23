#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
num = int(input('Digite um número: '))
print(f'Tabuada do número {num}:')
for i in range(1,11):
    print(f'{num} x {i} = {num * i}')

#for i in range é uma estrutura de repetição.