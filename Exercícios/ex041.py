#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre na sua categoria, de acordo com a sua idade
#Até 9 anos:Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos:Sênior
#Acima: master
idade = int(input('Qual a sua idade atual? '))
if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14:
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Junior.')
elif idade <= 25:
    print('Categoria Senior.')
else:
    print('Categoria Master.')