'''
Exercício 045
Crie um programa que faça o computador jogar Jokenpô com você.
✓ Pedra: Ganha da tesoura e perde do papel;
✓ Papel: Ganha da pedra e perde da tesoura;
✓ Tesoura: Ganha do papel e perde da pedra;
'''

print('\033[36m-*-\033[m'*19)
print(f'\033[1;7;36m{" Exercício 045: GAME => Pedra, Papel e Tesoura ":#^57}\033[m')
print('\033[36m-*-\033[m'*19)

#Para 'import random' e 'import time' => ver ex045.
from random import choice
from time import sleep

print('\n\033[1;4;33mJokepô\033[m, que começe o jogo!!!\033[m\n'
      '     [1] Pedra; \n'
      '     [2] Papel; \n'
      '     [3] Tesoura.')

lista = ['pedra', 'papel', 'tesoura']

n = int(input('\nQual é a sua jogada? '))
comp = choice(lista)
#Para 'comp = random.choice(lista)' => Ver ex045

if n == 0 or n > 3:
    print('\n\033[1;7;31mVocê digitou uma opção inválida.\033[m\n'
          '\033[1mPor favor digite um número de 1 a 3.\033[m')

elif n == 1 or n == 2 or n == 3:
    print('\n\033[1;36mJO\033[m')
    sleep(0.5)
    #Para 'time.sleep(0.5)' => Ver ex045
    print('\033[1;36mKEN\033[m')
    sleep(0.5)
    print('\033[1;36mPÔ!!!\033[m')
    sleep(0.5)

    print('\nVocê jogou \033[1;32m{}\033[m.'.format(lista[n - 1].upper()))
    print('Computador jogou \033[1;36m{}\033[m\n'.format(comp.upper()))

    if lista[n - 1] == comp:
        print('\033[1;33mEmpate, joguem novamente!!!\033[m')
    elif lista[n - 1] == lista[0] and comp == lista[2]:
        print('{:*^40}'.format(' \033[1;7;34mVocê Ganhou!!!\033[m '))
    elif lista[n - 1] == lista[1] and comp == lista[0]:
        print('{:=^40}'.format(' \033[1;7;34mVocê Ganhou!!!\033[m '))
    elif lista[n - 1] == lista[2] and comp == lista[1]:
        print('{:=^40}'.format(' \033[1;7;34mVocê Ganhou!!!\033[m '))
    else:
        print('\n\033[1;7;31mVocê PERDEU!!!\033[m')

print(f'\n{" PROGRAMA ENCERRADO ":=^50}\n')
