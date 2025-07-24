#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

oposto = float(input('Comprimento do Cateto Oposto: '))
adjacente = float(input('Comprimento do Cateto Adjcente: '))
hipo = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipo:.2f}')