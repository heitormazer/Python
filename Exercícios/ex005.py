#Faça programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
num1 = int(input("Digite um número:"))
numant = num1 - 1
numsuc = num1 + 1
print('O número digitado foi {}, seu antecessor é {} e seu sucessor {}'.format(num1,numant,numsuc))