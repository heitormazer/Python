#Crie um progama que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

#import math
from math import trunc
num = float(input('Digite um número: '))
numint = trunc(num)
print(f'O número {num} tem a parte inteira como {numint}')
