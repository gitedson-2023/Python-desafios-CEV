soma = 0
cont = 0
for c in range(1, 4):
    num = int(input('Digite o {} número: '. format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma deles é {}.' .format(cont, soma))
