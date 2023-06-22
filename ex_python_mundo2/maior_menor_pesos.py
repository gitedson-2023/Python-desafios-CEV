lista = []
for p in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    lista += [peso]
print('O maior peso é {}kg e o menor é {}kg.' .format(max(lista), min(lista)))
