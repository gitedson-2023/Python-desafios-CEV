produtos = ('Notebook', 3500, 'Mouse', 74, 'TV', 1980, 'Ventilador', 100)
print('='*50)
print('{:^45}'.format('LISTAGEM DE PRODUTOS'))
print('='*50)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')