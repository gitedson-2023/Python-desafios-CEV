import math
a = 's'
n = 1
media = 0
qtd = 0
soma = 0
tot = 0
maior = 0
menor = 0
while a in 'sS':
    n = int(input('Digite um número: '))
    a = str(input('Deseja continuar? [S/N] ')).upper()
    qtd += 1
    soma += n
    tot += 1
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / qtd
print('Programa encerrado.')
print('')
print('Foram digitados {} números até a parada do programa.'.format(qtd))
print('A soma entre eles é {}.' .format(soma))
print('A média entre eles é {:.2f}.' .format(media))
print('O menor número lido foi {} e o maior foi {}.' .format(menor, maior))
