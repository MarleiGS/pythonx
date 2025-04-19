'''
Exercício 043
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
✓ Abaixo de 18,5: Abaixo do Peso;
✓ Entre 18,5 e 25: Peso ideal;
✓ 25 até 30: Sobrepeso;
✓ 30 até 40: Obesidade;
✓ Acima de 40: Obesidade mórbida (grave)
'''

print('\n{:=^50}'.format(' Exercício 043 '))
print('{:=^50}'.format(' Cálculo do IMC '), '\n')

nome = str(input('Informe seu nome: '))
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / altura**2

print(f'\n{nome} tem {idade} anos, {peso} kilos e {altura} m de altura, portanto, seu IMC é: {imc:.1f}\n')

if imc <= 18.5:
    print(f'{nome} você está abaixo do peso!\n')

elif imc <= 25:
    print(f'{nome} você está com o peso ideal!\n')

elif imc <= 30:
    print(f'{nome} você está com sobrepeso!\n')

elif imc <= 40:
    print(f'{nome} você está com obesidade!\n')

else:
    print(f'{nome} você está com obesidade mórbida grave!\n')

print('{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
