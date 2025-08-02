#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade: 2025
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo do alistamento
#Seu programa também devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano_atual = date.today().year
nascimento = int(input("Digite sua data de nascimento: "))
idade = ano_atual - nascimento

if idade <  18:
    tempo = 18 - idade
    print(f'Faltam {tempo} anos para você precisar se alistar!')
elif idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    tempo = idade - 18
    print(f'Você já deveria ter se alistado há {tempo} anos')


