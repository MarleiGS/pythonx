'''
Exercício 038
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
✓ O primeiro valor é maior
✓ O segundo valor é maior
✓ Não existe valor maior, os dois são iguais
'''

print('\n{:=^50}'.format(' Exercício 038 '))
print('{:=^50}'.format(' Número Maior e Número Menor '), '\n')

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

print(f'\nOs números digitados foram {n1} e {n2}\n')

if n1 > n2:
    print(f'O 1º número ({n1}) é maior que o 2º número ({n2}).\n')
elif n2 > n1:
    print(f'O 2º número ({n2}) é maior que o 1º número ({n1}).\n')
else:
    print(f'Os dois números digitados  ({n1} e {n2})são iguais.\n')

print('{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
