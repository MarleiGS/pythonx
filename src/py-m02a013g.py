print('\nExemplo 7: Digitar Valor no Laço\n')

print('A. Digite um valor no laço')
for c in range(0, 3):
    i = int(input(' - Digite um valor: '))
print('FIM!\n')

print('B. Digite um valor e soma dos números digitados')
s = 0
for c in range(0, 3):
    n = int(input(' - Digite um valor: '))
    s = s + n # ou s += n
print('\nRespostas:')
print('-> Modelo 1: O somatório dos valores digitados foi {}. (Utilizando ".format()").'.format(s))
print(f'-> Modelo 2: O somatório dos valores digitados foi {s}. (Utilizando "f").\n')
