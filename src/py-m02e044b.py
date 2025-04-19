'''
Exercício 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
✓ À vista cash/pix: 10% de desconto;
✓ À vista cartão: 5% de desconto;
✓ Em até 2x no cartão: Preço normal;
✓ 3x ou mais no cartão: 20% de juros.
'''

print('\033[36m-*-\033[m'*17)
print(f'\033[1;7;36m{" Exercício 044: Gerenciador de Pagamentos ":#^51}\033[m')
print('\033[36m-*-\033[m'*17)

n = float(input('\nInforme o valor do produto: R$ '))

print('\n\033[1;34mCondições de Pagamentos:\033[m\n'
      '     [ 1 ] À vista: Dinheiro, Cheque, Cart Débito ou PIX - 10% de desconto;\n'
      '     [ 2 ] À vista: Cartão de Crédito - 5% de desconto;\n'
      '     [ 3 ] 2x no Cartão de Crédito - valor normal;\n'
      '     [ 4 ] 3x ou mais no Cartão de Crédito - 20% de juros.')

c = int(input('\nEscolha uma opção de pagamento: '))

if c == 1:
    print('\nO valor do produto de R$ {:.2f} para pagamento à vista em dinheiro, cheque, débito ou PIX\n'
          'é R$ {:.2f} com 10% de desconto.'.format(n, n * 0.9))

elif c == 2:
    print('\nO valor do produto de R$ {:.2f} para pagamento à vista com cartão de crédito é R$ {:.2f} com 5% de desconto.'.format(n, n * 0.95))

elif c == 3:
    print('\nO valor do produto para pagamento em 2x com cartão de crédito é R$ {:.2f}\n'
          'e o valor de cada parcela será de R$ {:.2f}.'.format(n, n / 2))

elif c == 4:
    parc = int(input('Quantidade de parcelos desejada? '))
    print('\nO valor do produto de R$ {:.2f} para pagamento em {}x com cartão de crédito é R$ {:.2f}\n'
          'com 20% de juros e o valor de cada parcela será de R$ {:.2f}.'.format(n, parc, n * 1.2, (n * 1.2) / parc))

else:
    print('\033[1;4;31mOpção {} inválida!!! Escolha uma opção de 1 a 4.\033[m'.format(c))

print(f'\n{" PROGRAMA ENCERRADO ":=^50}\n')
