n = int(input('Digite um número para ver sua tabuada: '))
print('<->' * 20)
print('A tabuada do {} é:' .format(n))
for c in range(1, 11):
    x = n*c
    print('{}x{} = {}' .format(n, c, x))