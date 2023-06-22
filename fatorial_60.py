import math
n = int(input('Digite um número e veja seu fatorial: '))
print('')
c = n
print('O valor de {}! é: '.format(n))
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c = c - 1
print(math.factorial(n))

