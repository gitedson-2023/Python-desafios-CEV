x = ''
valor = list()
for cont in range(0, 100):
    n = valor.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso.')
    x = str(input('Deseja continuar? [S/N] '))
    while x not in 'SsNn':
        x = str(input('Deseja continuar? [S/N] '))
    if x in 'Nn':
        break
print('-='*30)
if 5 in valor:
    print('O valor 5 faz parte da lista.')
else:
    print('Não foi digitado o número 5.')
print(f'Você digitou {len(valor)} valores.')
print(f'Você digitou os valores {sorted(valor, reverse=True)}')
