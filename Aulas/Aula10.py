tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 6:
    print(f'Nossa, seu carro só tem {tempo} anos? Ele é novo.')
elif tempo == 7 and tempo < 15:
    (print(f'Nossa, seu carro tem {tempo} anos? Ele não é tão antigo'))
else:
    print(f'Nossa, seu carro tem {tempo} anos? Ele é bem antigo.')
