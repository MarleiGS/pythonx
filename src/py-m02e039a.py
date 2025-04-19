'''
Exercício 039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
✓ Se ele ainda vai se alistar ao serviço militar;
✓ Se é a hora de se alistar;
✓ Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.
'''

print('\n{:=^50}'.format(' Exercício 039 '))
print('{:=^50}'.format(' Alistamento Militar '), '\n')

ano1 = int(input('Digite o ano atual: '))
ano2 = int(input('Digite o ano de seu nascimento: '))
idade = ano1 - ano2

if idade == 1:
    print(f'\nO ano atual é {ano1} e o ano do seu nascimento é {ano2}, portanto, você tem {idade} ano.\n')
else:
    print(f'\nO ano atual é {ano1} e o ano do seu nascimento é {ano2}, portanto, você tem {idade} anos.\n')

if idade < 18:
    if idade == 17:
        print(f'Você deverá se alistar em {18 - idade} ano.\n')
    else:
        print(f'Você deverá se alistar em {18 - idade} anos.\n')

elif idade == 18:
    print(f'Você está com 18 anos. É hora de se alistar!\n')

else:
    if idade-18 == 1:
        print(f'Você já passou do tempo de alistamento em {idade-18} ano.\n')
    else:
        print(f'Você já passou do tempo de alistamento em {idade-18} anos.\n')

print('{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
