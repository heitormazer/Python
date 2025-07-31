#Escreva um programa que leia a velocidade de um carro, se ele ultrapasasr 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você ultrapassou o limete de velocidade. MULTADO!')
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:.2f}.')
else:
    print('Tenha um bom dia, continue dirigindo com segurança!')
