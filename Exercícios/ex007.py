#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.
notmat = float(input('Nota de Matemática: '))
notpor = float(input('Nota de Português: '))
notfinal = (notmat + notpor)/2
print(f'A nota final é {notfinal}')