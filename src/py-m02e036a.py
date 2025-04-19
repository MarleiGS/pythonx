'''
Exercício 036
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos pretende pagar.
✓ Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. Considerar que não há juros.
'''

print('\n{:=^50}'.format(' Exercício 036 '))
print('{:=^50}'.format(' Empréstimo Bancário '), '\n')

nome = str(input('Qual é seu nome? '))
imovel = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe o valor da renda mensal: R$ '))
anos = int(input('Informe quantos anos de financiamento: '))
prestacao = imovel / (anos*12)
renda = prestacao / salario * 100

print(f'\nO valor da prestação será de R$ {prestacao:.2f}, ocupando {renda:.2f}% da sua renda.\n')

if renda <= 30:
    print(f'{nome}, seu emprétimo foi aprovado!')
else:
    print(f'{nome}, seu empréstimo foi reprovado! Refaça o calculo e altere a quantidade de anos para {(imovel/(salario*0.3))/12:.0f} anos.')

print('Tenha um bom dia, {}!!!'.format(nome))

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
