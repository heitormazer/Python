n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 +n2) / 2
print(f'A sua nota final foi {m:.2f}.')
if m <= 4:
    print('Você ficou com vermelha na média, melhore.')
elif m <= 8:
    print('Você ficou com azul, mas da para melhorar.')
else:
    print('Você foi muito bem, parabéns.')