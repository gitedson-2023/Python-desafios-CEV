def fatorial(num, show=True):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
num = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(num, show=True))