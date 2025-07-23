#Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o peço a pagar, sabendo que o carro custa R$60 por dia e R$ por Km rodado.
quant_km = float(input('Quantos KM foram rodados: '))
quant_dia = int(input('Quandos dias ele foi alugado: '))
quant_km_fin = quant_km * 0.15
quant_dia_fin = quant_dia * 60
total = quant_dia_fin + quant_km_fin
print(f'Total a pagar: {total:.2f}')
