#Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilatéro: Todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: Todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo',end=' ')
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar um triangulo')
