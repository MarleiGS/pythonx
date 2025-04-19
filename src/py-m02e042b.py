'''
Exercício 042
Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
✓ Equilátero: todos os lados iguais;
✓ Isósceles: dois lados iguais;
✓ Escaleno: todos os lados diferentes.
'''

print('\033[36m-*-\033[m'*17)
print(f'\033[1;7;36m{" Exercício 042: Analisando Triângulos v2.0 ":#^51}\033[m')
print('\033[36m-*-\033[m'*17)

print(f'\033[1;33m{" Sugestão Prof. Gustavo Guanabara ":#^51}\033[m\n')

t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segunda  Segmento: '))
t3 = float(input('Terceira Segmento: '))
print()

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os valores acima \033[1;33mPODEM\033[m formar um Triângulo ', end='')

    if t1 == t2 == t3:
        print('\033[1;4;36mEquilátero\033[m.')
    elif t1 != t2 != t3 != t1:
        print('\033[1;4;36mEscaleno\033[m.')
    else:
        print('\033[1;4;36mIsósceles\033[m.')

else:
    print('Os valores acima \033[1;7;31mNÃO PODEM\033[m formar um Triângulo.')

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
