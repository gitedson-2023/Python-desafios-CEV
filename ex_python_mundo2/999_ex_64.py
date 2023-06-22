n = 1
qtd = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    qtd += 1
    tot = qtd - 1
    soma = soma + n
    s = soma - 999
print('')
print('Você digitou o número 999 e o programa parou. Foram digitados {} números até a parada.' .format(tot))
print('A soma dos números digitados (excetuando o 999) é {}.' .format(s))