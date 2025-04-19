print('-*-'*12)
print('\033[1;7;48m=> Exercício 038: Comparando Numeros\033[m')
print(f'\033[1;7;36m{" Exercício 038: Comparando Numeros ":#^50}\033[m')
print('{:=^50}'.format('\033[1;7;48mTESTE\033[m'))
print('-*-'*12)
print()

n1 = int(input('1. Digite o primeiro número inteiro: '))
n2 = int(input('2. Digite o segundo  número inteiro: '))
print()

print('Os números digitados foram:\n'
      '     a) \033[1;34m{}\033[m é o Primeiro Número;\n'
      '     b) \033[1;34m{}\033[m é o Segundo Número.'.format(n1, n2))
print()

if n1 > n2:
    print('O Primeiro número \033[1;35m{}\033[m é \033[1;7;33mmaior\033[m!!!'.format(n1))
elif n2 > n1:
    print('O Segundo número \033[1;35m{}\033[m é \033[1;7;33mmaior\033[m!!!'.format(n2))
else:
    print('\033[1;31mNão existe valor maior, pois os dois números são iguais!!!\033[m')

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
