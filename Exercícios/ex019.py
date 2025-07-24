#Um professor que sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude a ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

al1 = 'Matheus'
al2 = 'Claudia'
al3 = 'Ronnie'
al4 = 'Jaison'

alunos = [al1,al2,al3,al4]
resultado = random.choice(alunos)

print(f'O aluno que deve se apresentar ao quadro é o {resultado}')