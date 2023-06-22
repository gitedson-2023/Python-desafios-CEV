valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores {valores}')
print('-='*36)
print(f'O maior valor da lista é {max(valores)} nas posições ',end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
print(f'O menor valor da lista é {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
print()
print('-='*36)
print('Fim do programa.')