p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
dec = p + (11-1) * r
for c in range(p, dec, r):
    print(c, end=' - ')
print('FIM')
