print('=> Class 12: Condições Aninhadas')
print()
nome = str(input('Qual é seu nome? '))
print()

print('\033[1;4;33m=> Estrutura Condicional Simples:\033[m Utiliza somente "\033[1;34mif\033[m".')
if nome == 'Marlei':
    print('Você é muito inteligente!!!')
print('Tenha um bom dia, {}!!!'.format(nome))
print()

print('\033[1;4;33m=> Estrutura Condicional Composta:\033[m Utiliza "\033[1;34mif\033[m" e "\033[1;34melse\033[m".')
if nome == 'Marlei':
    print('Você é muito inteligente!!!!')
else:
    print('Seu nome é tão normal.')
print('Tenha um bom dia, {}!!!'.format(nome))
print()

print('\033[1;4;33m=> Estrutura Condicional Aninhada:\033[m Utiliza "\033[1;34mif\033[m", "\033[1;34melif\033[m" e '
      '"\033[1;34melse\033[m".')

print('\033[1;32mExemplo 1:\033[m')
if nome == 'Marlei':
    print('Você é muito inteligente!!!!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'José':
    print('O nome {} é bem popular no Brasil!!!'.format(nome))
else:
    print('Seu nome é tão normal.')
print('Tenha um bom dia, {}!!!'.format(nome))
print()

print('\033[1;32mExemplo 2:\033[m')
if nome == 'Marlei':
    print('Você é muito inteligente!!!!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'José':
    print('O nome {} é bem popular no Brasil!!!'.format(nome))
elif nome in 'Ana Juliana Letícia':
    print('Belo nome vc tem {}!!!'.format(nome))
else:
    print('Seu nome é tão normal.')
print('Tenha um bom dia, {}!!!'.format(nome))
