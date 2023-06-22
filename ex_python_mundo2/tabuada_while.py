while True:
    n = int(input('Informe um número inteiro e veja sua tabuada: '))
    if n < 0:
        break
    print('-=' * 50)
    print(f'A tabuada do {n} é:')
    for c in range(1, 11):
        x = n * c
        print(f'{n} x {c} = {x}')
    print('-='*50)
print('Fim do programa.')
