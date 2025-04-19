'''
Exercício 036
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos pretende pagar.
✓ Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. Considerar que não há juros.
'''

print('-*-'*13)
print('\033[1;7;48m => Exercise 036: Aprovando empréstimo \033[m')
print('-*-'*13)

from math import ceil

nome = str(input('\nInforme seu nome: ')).strip().title()
sal = float(input('Informe seu salário: R$ '))
imovel = float(input('Informe o valor do imóvel: R$ '))
ano = int(input('Informe o prazo de pagamento em anos: '))

sal30 = sal * 0.30
prest = imovel / (ano * 12)
ano1 = (imovel / sal30) / 12
ano2 = ceil(ano1)

print('\nPara pagar um imóvel de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.' .format(imovel, ano, prest))
print(f'Para pagar um imóvel de R$ {imovel:.2f} em {ano} anos, a prestação será de R$ {prest:.2f}.')

if sal30 > prest:
    print('\n\033[1;33mParabéns {}, seu empréstimo foi aprovado!!!\033[m\n'
          'A prestação será de \033[1;7;33mR$ {:.2f}\033[m.'.format(nome, prest))
else:
    print('\n\033[1;36mDesculpe {}, seu empréstimo foi reprovado.\033[m\n'
          'A prestação ficou acima dos \033[1;7;36m30% permitidos\033[m.'.format(nome))
    print('Aumente o prazo para {:.4f} anos para conseguir o seu empréstimo.'.format(ano1))
    print('Aumente o prazo para {} anos para conseguir o seu empréstimo.'.format(ano2))
    print('Aumente o prazo para {} anos para conseguir o seu empréstimo.'.format(ceil(ano1)))

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
