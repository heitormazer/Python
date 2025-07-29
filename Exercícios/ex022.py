#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todos as letras maiusculas
#O nome com todas as letras minusculas
#quantas letras ao todo(sem considerar espaço)
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
letrasTot = len(nome.replace(' ', ' '))#conta as letras sem espaço
print(letrasTot)

print("primeiro nome: ", nome.split())