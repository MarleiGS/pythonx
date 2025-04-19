'''
Exercício 045
Crie um programa que faça o computador jogar Jokenpô com você.
✓ Pedra: Ganha da tesoura e perde do papel;
✓ Papel: Ganha da pedra e perde da tesoura;
✓ Tesoura: Ganha do papel e perde da pedra;
'''

print('-*-'*15)
print('\033[1;7;48mExercício 045: GAME => Pedra, Papel e Tesoura\033[m')
print('-*-'*15)

import random
import time

print('\n\033[1;4;33mJokepô\033[m, que comece o jogo!!!\033[m\n'
      '     [1] Pedra; \n'
      '     [2] Papel; \n'
      '     [3] Tesoura.')

lista = ['pedra', 'papel', 'tesoura'] 
'''Verificar listas. Durante aula foi colocado em parenteses. Temos:
- pedra é 0
- papel é 1
- tesoura é 2
'''

n = int(input('\nQual é a sua jogada? '))
comp = random.choice(lista) # Ou comp = randint(0, 2)

if n == 0 or n > 3:
    print('\033[1;7;31mVocê digitou uma opção inválida.\033[m\n'
          '\033[1mPor favor digite um número de 1 a 3.\033[m')

elif n == 1 or n == 2 or n == 3:
    print('\n\033[1;36mJO\033[m')
    time.sleep(0.5)
    print('\033[1;36mKEN\033[m')
    time.sleep(0.5)
    print('\033[1;36mPÔ!!!\033[m')
    time.sleep(0.5)

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
        print('\033[1;7;31mVocê PERDEU!!!\033[m')

print(f'\n{" PROGRAMA ENCERRADO ":=^50}\n')
