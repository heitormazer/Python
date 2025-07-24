#O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
random.seed()  #IMPORTANTE

al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str('Vanessa')
al4 = str(input('Digite o nome do quarto aluno: '))

lista = [al1,al2,al3,al4]
random.shuffle(lista)
print('A ordem de apresetação será: ')
for i, nome in enumerate(lista, start=1):
    print(f"{i}º - {nome}")