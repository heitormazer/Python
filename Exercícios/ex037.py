#Escreva um programa que leia um número e peça para o usuário escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal
num = int(input('Digite um número: '))
print("Escola a opção q você deseja que seu número seja convertido")
print('[1] para Binário\n[2] para Octal\n]3] para Hexadecimal')
escolha = int(input('Escolha a opção: '))
if escolha != 1 and escolha != 2 and escolha != 3:
    print('Erro')
elif escolha == 1:
    print(f'O número convertido para binário é {bin(num)[2:]:}')
elif escolha == 2:
    print(f'O número convertido para Octal é {oct(num)[2:]:}')
else:
    print(f'O número convertido para Hexagonal é {hex(num)[2:]:}')
