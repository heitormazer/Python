#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Analisador de Triângulos.')
prim = float(input('Digite o primeiro seguimento: '))
segu = float(input('Digite o segundo seguimento: '))
terc = float(input('Digite o terceiro seguimento: '))
if prim < segu + terc and segu < terc + prim and terc < prim + segu:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo')