#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0 : reprovado
#Média entre 5.0 e 6.9: recuperação
#média superior a 7.0: aprovado
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'A sua média final foi igual a {media:.2f}. Reprovado.')
elif media < 6.9:
    print(f'A sua média final foi igual a {media:.2f}. Recuperação.')
else:
    print(f'A sua média final foi igual a {media:.2f}. Aprovado.')