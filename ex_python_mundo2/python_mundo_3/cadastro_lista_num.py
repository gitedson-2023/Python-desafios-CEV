valor = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não será adicionado à lista')
    x = str(input('Deseja continuar? [S/N] '))
    if x in'Nn':
        break
print(f'Você digitou os valores {sorted(valor)}')