'''
Exercício 040
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
✓ Média abaixo de 5,0: REPROVADO
✓ Média entre de 5,0 e 6,9: RECUPERAÇÃO
✓ Média 7,0 ou superior: APROVADO
'''

print('\033[36m-*-\033[m'*17)
print(f'\033[1;7;36m{" Exercício 040: Aquele clássico da Média ":#^51}\033[m')
print('\033[36m-*-\033[m'*17)

aluno = input('\nNome do aluno: ').strip().title()
n1 = float(input('Digite a nota de {} do Primeiro Bimestre: '.format(aluno)))
n2 = float(input('Digite a nota de {} do Segundo Bimestre: '.format(aluno)))

print(f'''\nNota do aluno(a) {aluno}:
    => Primeiro Bimestre é {n1}
    => Segundo  Bimestre é {n2}
''')

m = (n1 + n2) / 2

print('A média atual do {} é: {:.1f} => sendo ":.1f" para "uma" casa decimal.'.format(aluno, m))

if m >= 7:
    print('     => O aluno \033[1;36m{}\033[m está \033[1;7;32mAPROVADO!!!\033[m'.format(aluno))

elif m < 5:
    print('     => O aluno \033[1;36m{}\033[m está \033[1;7;31mREPROVADO!!!\033[m'.format(aluno))

else: # Opção: 7 > média >= 5
    print('     => O aluno \033[1;36m{}\033[m está de \033[1;7;33mRECUPERAÇÃO!!!\033[m'.format(aluno))

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
