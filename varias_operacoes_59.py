import time
print('======================= CALCULADORA =========================')
print('')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('')
escolha = 0
while escolha != 5:
    print('Escolha uma das opções abaixo para prosseguir:')
    print('')
    print('Digite [1] para somar os valores')
    print('Digite [2] para multiplicar os valores')
    print('Digite [3] para saber qual valor é maior')
    print('Digite [4] para escolher outros números')
    print('Digite [5] para sair do programa')
    print('')
    escolha = int(input('Digite o número equivalente à operação desejada: '))
    if escolha == 1:
        soma = n1 + n2
        print('\033[34mA soma dos valores digitados é {}.\033[m' .format(soma))
    elif escolha == 2:
        mult = n1 * n2
        print('\033[34mA multiplicação {} x {} é {}.\033[m' .format(n1, n2, mult))
    elif escolha == 3:
        maior1 = n1
        maior2 = n2
        if n1 > n2:
            print('\033[34mO maior número entre os valores digitados é o {}.\033[m' .format(maior1))
        if n2 > n1:
            print('\033[34mO maior número entre os valores digitados é o {}.\033[34m' .format(maior2))
    elif escolha == 4:
        print('Escolha novos números para calcular.')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Encerrando...')
    else:
        print('Digite uma opção válida. Tente novamente.')
    print('<=>' * 20)
    time.sleep(2)
print('Até mais.')

