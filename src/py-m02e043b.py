'''
Exercício 043
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
✓ Abaixo de 18,5: Abaixo do Peso;
✓ Entre 18,5 e 25: Peso ideal;
✓ 25 até 30: Sobrepeso;
✓ 30 até 40: Obesidade;
✓ Acima de 40: Obesidade mórbida (grave)
'''

print('\033[36m-*-\033[m'*17)
print(f'\033[1;7;36m{" Exercício 043: Índice da Massa Corporal (IMC) ":#^51}\033[m')
print('\033[36m-*-\033[m'*17)

n = input('\nInforme o nome completo do paciente: ').strip().title()
p = float(input('Informe o peso do paciente em Kg: '))
h = float(input('Informe a altura do paciente em metros: '))
imc = p / h**2

print('\nO paciente \033[1;35m{}\033[m tem peso \033[1;35m{:.2f}\033[m Kg e altura de \033[1;35m{:.2f}\033[m m, '
      'portanto seu IMC é \033[1;7;35m{:.1f}\033[m.'.format(n, p, h, imc))

if imc < 18.5:
    print('Classificação: \033[1;4;33mMagreza e Obesidade Grau 0\033[m')
#elif imc >= 18.5 and imc < 25: (Sugestão Guanabara)
#ou
#elif 18.5 <= imc < 25: (Sugestão Guanabara)

elif imc <25:
    print('Classificação: \033[1;4;33mNormal e Obesidade Grau 0\033[m')

elif imc < 30:
    print('Classificação: \033[1;4;33mSobrepeso e Obesidade Grau I\033[m')

elif imc < 40:
    print('Classificação: \033[1;4;33mObesidade e Obesidade Grau II\033[m')
    
else:
    print('Classificação: \033[1;4;33mObesidade Grave e Obesidade Grau III\033[m')

print('\n{:=^50}'.format(' PROGRAMA ENCERRADO '), '\n')
