'''
Exercício 037
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
✓ Para binário;
✓ Para octal;
✓ Para hexadecimal.
Dica: Ver aula de Bases Numéricas!
'''

print('-*-'*16)
print('\033[1;7;48m => Exercício 037: Conversor de Bases Numéricas \033[m')
print('-*-'*16,'\n')

n = int(input('Informe um número inteiro: '))

'''
print('\n\033[1;33mBase Numéricas:\033[m\n'
      '     [1] Base Binária;\n'
      '     [2] Base Octal;\n'
      '     [3] Base Hexadecimal.')
'''

print('''
\033[1;33mBase Numéricas:\033[m
    [1] Base Binária;
    [2] Base Octal;
    [3] Base Hexadecimal.''') # Se der um enter após as ''' (em outra linha), não necessita do \n na variável bn. 

bn = int(input('\nInforme uma opção de Base Numéria para conversão: '))

#print('\n=> Número escolhido: \033[1;32m{}\033[m;\n=> Base Numérica: \033[1;32m{}\033[m.'.format(n, bn)) => Exercício do PyCharm

print(f'\n=> Número: \033[1;32m{n}\033[m')
print(f'=> Base Numérica: \033[1;32m{bn}\033[m\n')

b = bin(n)
'''
O Python tem conversores automáticos em sua biblioteca, e.g. Bases Numéricas:
    - bin para Base Binária
    - oct para Base Octal;
    - hex para Base Hexadecimal.
''' 
if bn == 1:
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Binária.'.format(n, bin(n)))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Binária.'.format(n, bin(n)[2:]))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{:b}\033[m na Base Binária.'.format(n, n))

elif bn == 2:
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Octal.'.format(n, oct(n)))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Octal.'.format(n, oct(n)[2:]))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{:o}\033[m na Base Octal.'.format(n, n))

elif bn == 3:
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Hexadecimal.'.format(n, hex(n)))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{}\033[m na Base Hexadecimal.'.format(n, hex(n)[2:]))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{:x}\033[m na Base Hexadecimal.'.format(n, n))
    print('O número \033[1;34m{}\033[m na Base Decimal é \033[1;36m{:X}\033[m na Base Hexadecimal.'.format(n, n))
else:
    print('A opção \033[1;7;31m{}\033[m não é uma opção válida. Escolha as opções 1, 2 ou 3.'.format(bn))

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
