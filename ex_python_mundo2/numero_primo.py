n = int(input('Digite um número e saiba se ele é um número primo: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ') # divisíveis por n
        tot += 1
    else:
        print('\033[31m', end=' ') # não divisíveis por n
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisível por {} números.'.format(n, tot))
if tot == 2:
    print('A saber: só por 1 e por ele mesmo.\nPor isso ele é PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO')