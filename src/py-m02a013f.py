print('\nExemplo 6: Criar Início, Fim e Passo (step)\n')

print('A. Início, fim e passo')
i = int(input('=> Início: '))
f = int(input('=> Fim: '))
p = int(input('=> Passoo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!\n')
