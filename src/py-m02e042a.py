'''
Exercício 042
Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
✓ Equilátero: todos os lados iguais;
✓ Isósceles: dois lados iguais;
✓ Escaleno: todos os lados diferentes.
'''

print('\n{:=^50}'.format(' Exercício 042 '))
print('{:=^50}'.format(' Tipo de triângulo '), '\n')

lado1 = float(input('Informe o lado 1 do triângulo: '))
lado2 = float(input('Informe o lado 2 do triângulo: '))
lado3 = float(input('Informe o lado 3 do triângulo: '))

print(f'\nOs lados digitados foram:\n - Lado 1: {lado1}\n - Lado 2: {lado2}\n - Lado 3: {lado3}')

if lado1 == lado2 == lado3:
    print('\nCom todos os lados iguais temos um triângulo Equilátero.')

elif lado1 + lado2 <= lado3:
    print('Não é possível formar um triângulo.')

elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
    print('\nCom dois lados iguais temos um triângulo Isósceles.')

elif lado1 != lado2 != lado3:
    print('\nCom todos os lados diferentes temos um triângulo Escaleno.')

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
