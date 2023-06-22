'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))'''
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
#lista = (n1, n2, n3, n4)
if 9 in n:
    print(f'O número 9 aparece {n.count(9)} vezes na lista.')
if 3 in n:
    print('O primeiro número 3 foi digitado na {}ª posição.' .format(n.index(3)+1))
else:
    print('O número 3 não foi digitado nenhuma vez.')
print(f'O(s) valor(es) par(es) digitado(s) foi(foram):', end=' ')
for c in n:
    if c%2 == 0:
        print(c, end=' ')
