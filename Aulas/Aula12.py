nome = str(input('Qual é o seu nome: '))
if nome == 'Heitor':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Jessica Claúdia Juliana':
    print('Belo nome feminino.')
else:
    print(f'Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')