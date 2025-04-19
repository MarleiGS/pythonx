'''
Exercício 041
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
✓ Até 9 anos: MIRIM;
✓ Até 14 anos: INFANTIL;
✓ Até 19 anos: JUNIOR;
✓ Até 20 anos: SÊNIOR;
✓ Acima: MASTER.
'''

print('\n{:=^50}'.format(' Exercício 041 '))
print('{:=^50}'.format(' Categoria do atleta '), '\n')

nome = str(input('Informe o nome do atleta: '))
idade = int(input('Informe a idade do atleta: '))

if idade <= 9:
    print(f'\n{nome} tem {idade} anos e sua categoria é Mirim.\n')

elif idade <= 14:
    print(f'\n{nome} tem {idade} anos e sua categoria é Infantil.\n')

elif idade <= 19:
    print(f'\n{nome} tem {idade} anos e sua categoria é Junior.\n')

elif idade <= 20:
    print(f'\n{nome} tem {idade} anos e sua categoria é Sênior.\n')

else:
    print(f'\n{nome} tem {idade} anos e sua categoria é Master.\n')

print('{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
