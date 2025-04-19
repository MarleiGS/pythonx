'''
Exercício 041
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
✓ Até 9 anos: MIRIM;
✓ Até 14 anos: INFANTIL;
✓ Até 19 anos: JUNIOR;
✓ Até 20 anos: SÊNIOR;
✓ Acima: MASTER.
'''

print('\033[36m-*-\033[m'*17)
print(f'\033[1;7;36m{" Exercício 041: Classificando Atletas ":#^51}\033[m')
print('\033[36m-*-\033[m'*17)

import datetime 
# Opção: from datetime import date

a1 = datetime.date.today().year
a2 = datetime.date.today().month
print(f'\nAno: {a1} | Mês: {a2}\n')

n = input('Informe o nome completo do atleta: ').strip().title()
a = int(input('Digite o ano de nascimento do atleta {} com 4 dígitos: '.format(n)))

i = a1 - a

print('\nO atleta \033[1;4;33m{}\033[m nasceu em \033[1;7;33m{}\033[m.'.format(n, a))
#print('O atleta \033[1;4;33m{}\033[m nasceu em \033[1;7;33m{}\033[m.'.format(n, a), end=' ')

if i <= 9:
    print('A categoria do atleta \033[1;4;33m{}\033[m é \033[1;7;35mMirim\033[m.'.format(n))

elif i <= 14:
    print('A categoria do atleta \033[1;4;33m{}\033[m é \033[1;7;35mInfantil\033[m.'.format(n))

elif i <= 19:
    print('A categoria do atleta \033[1;4;33m{}\033[m é \033[1;7;35mJunior\033[m.'.format(n))

elif i <= 25:
    print('A categoria do atleta \033[1;4;33m{}\033[m é \033[1;7;35mSenior\033[m.'.format(n))

else:
    print('A categoria do atleta \033[1;4;33m{}\033[m é \033[1;7;35mMaster\033[m.'.format(n))

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
