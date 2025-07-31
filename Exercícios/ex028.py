#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O prgama deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
num = randint(0, 10)
num1 = int(input('Advinhe o número entre 0 e 10 que o programa sorteou: '))
if num1 > 10:
    print('O número está acima da 10, tente novamente.')
elif num == num1:
    print('Você acertou!')
else:
    print(f'Você errou! O número era {num}')