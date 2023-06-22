x = ''
valor = list()
pares = list()
impares = list()
while True:
    n = valor.append(int(input('Digite um valor: ')))
    x = str(input('Quer continuar? [S/N] '))
    while x not in 'SsNn':
        x = str(input('Quer continuar? [S/N] '))
    if x in 'Nn':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Foram digitados os valores {valor}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {impares}')