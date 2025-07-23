#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
altu = float(input('Altura: '))
larg = float(input('Largura: '))
area = larg * altu
tint = area / 2 
print(f'A área total é de {area}m² e será necessário {tint} litros de tinta.')