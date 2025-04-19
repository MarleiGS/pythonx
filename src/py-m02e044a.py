'''
Exercício 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
✓ À vista cash/pix: 10% de desconto;
✓ À vista cartão: 5% de desconto;
✓ Em até 2x no cartão: Preço normal;
✓ 3x ou mais no cartão: 20% de juros.
'''

'''
print('\n{:=^50}'.format(' Exercício 044 '))
print('{:=^50}'.format(' Desconto de um produto '), '\n')
Versão 2020, ver configuração abaixo
'''
print(f'{" Exercício 044 ":=^50}')

produto = float(input('\nInforme o valor do produto: R$ '))

print('\n{:*^40}'.format(' FORMAS DE PAGAMENTO '))
print('[1] À vista - cash ou pix: 10% de desconto.')
print('[2] À vista - cartão (crédito ou débito): 5% de desconto.')
print('[3] 2x no cartão (crédito ou débito): preço normal.')
print('[4] 3x no cartão (crédito ou débito): 20% de juros.')

pagamento = input('\nEscolha a forma de pagamento: ')

if pagamento == '1':
    print('\nForma escolhida para o pagamento: À vista com 10% de desconto')
    print(f'O valor do produto será: R$ {produto * 0.9:.2f}\n')

elif pagamento == '2':
    print('\nForma escolhida para o pagamento: À vista com 5% de desconto')
    print(f'O valor do produto será: R$ {produto * 0.95:.2f}\n')

elif pagamento == '3':
    print('\nForma escolhida para o pagamento: 2x no cartão preço normal')
    print(f'O valor do produto será: R$ {produto}\n')

elif pagamento == '4':
    print('\nForma escolhida para o pagamento: 3x no cartão com 20% de juros')
    print(f'O valor do produto será: R$ {produto*1.2:.2f}\n')

else:
    print('\nForma de pagamento escolhida INCORRETA! Escolha um forma de pagamento.\n')

print('{:=^50}'.format(' PROGRAMA ENCERRADO '))
print(f'{" PROGRAMA ENCERRADO ":=^50}', 'Versão 2020\n')
