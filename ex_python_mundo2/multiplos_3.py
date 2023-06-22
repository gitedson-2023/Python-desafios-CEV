import time
s = 0
cont = 0
print('Os múltiplos de 3 entre 1 e 500 são:')
time.sleep(2)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
        print(c, end= ' ')
print('')
print('\nA soma de todos os {} números encontrados é {}.' .format(cont, s))


