#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Ângulo: '))
radianos = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'O {angulo}°graus tem como seno {seno:.3f}, Cosseno {cosseno:.3f} e tangente como {tangente:.3f}.')
