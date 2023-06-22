from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
print('=-'*30)
print(f'A tabuada do {n} é:')
print('')
for t in range(1, 11):
    sleep(1)
    print(f'{n} x {t} = {n * t}')