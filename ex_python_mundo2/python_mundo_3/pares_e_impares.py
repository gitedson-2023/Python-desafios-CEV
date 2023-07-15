valor = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = valor.append(int(input(f'Digite o {c}ª valor: ')))
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Foram digitados os valores {valor}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {impares}')