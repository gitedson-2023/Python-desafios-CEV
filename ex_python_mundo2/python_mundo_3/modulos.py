def metade(n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res


def aumento(n):
    res = n * 1.15
    return res


def reducao(n):
    res = n * 0.30
    return res


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'


def resumo(n):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \tR${dobro(n):.2f}')
    print(f'Metade do preço: \tR${metade(n):.2f}')
    print(f'Aumentado em 15%: \tR${aumento(n):.2f}')
    print(f'Diminuído em 30%: \tR${n-reducao(n):.2f}')
    print('-' * 30)