'''
Exercício 039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
✓ Se ele ainda vai se alistar ao serviço militar;
✓ Se é a hora de se alistar;
✓ Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.
'''

print('-*-'*12)
print('\033[1;7;48m=> Exercise 039: Alistamento Militar\033[m')
print('\033[1;mDesafio Extra: Incluir sexo feminino\033[m')
print('-*-'*12)

import datetime
# from datetime import date => Utilizado pelo GG

nome = input('\nInforme seu nome: ').strip().title()
sexo = int(input('Informe seu sexo | [1] Masc [2] Fem: '))
a = int(input('Digite o ano de nascimento com 4 dígitos: '))
a1 = datetime.date.today().year
a2 = datetime.date.today().month
age = a1 - a

#print('Quem nasceu em {} tem {} anos em {}. Portanto:'.format(a, age, a1))

if sexo == 2:
    print('\nOlá \033[1;35m{}!!!\033[m O alistamento militar não é obrigatório para mulheres. \n'
          '     => Mas caso queira se alistar, procure um junta militar no ano em que completar 18 anos. \n'
          '     => Será um prazer em receber você nas forças armadas!!!!'.format(nome))

elif age > 18:
    print('\nOlá \033[1;34m{}!!!\033[m Você nasceu em {} e tem {} anos em {}, portanto:\n'
          '     \033[1;31m=> Você passou {} anos do seu alistamento militar. \033[m\n'
          '     => Você deveria ter se alistado em {}. \n'
          '     => Compareça uma junta militar URGENTE e regulariza sua situação.'.format(nome, a, age, a1, age - 18, a + 18))

elif age < 18:
    print('\nOlá \033[1;34m{}!!!\033[m Você nasceu em {} e tem {} anos em {}, portanto:\n'
          '     \033[1;32m=> Falta(m) {} ano(s) para o seu alistamento militar. \033[m\n'
          '     => Compareça uma junta militar em {}.'.format(nome, a, age, a1, 18 - age, 18 + a))

else:
    ''' #Outra maneira
    print('\nOlá \033[1;34m{}!!!\033[m Você nasceu em {} e tem {} anos em {}, portanto:\n'
          '     \033[1;34m=> {} é o seu ano de alistamento militar. \033[m\n'
          '     => Compareça à uma junta militar e faça seu alistamaneto.'.format(nome, a, age, a1, a1))
    '''
    
    print(f'''
          Olá \033[1;34m{nome}!!!\033[m Você nasceu em {a} e tem {age} anos em {a1}, portanto:
        \033[1;34m=> {a1} é o seu ano de alistamento militar. 
        \033[m=> Compareça à uma junta militar e faça seu alistamaneto.
    ''')

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
