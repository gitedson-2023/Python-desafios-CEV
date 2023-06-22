cont = 0
soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print('A soma dos {} números digitados até a parada do programa é {}.' .format(cont, soma))