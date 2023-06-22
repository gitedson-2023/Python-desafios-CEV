from time import sleep
def maior(* num):
    cont = maior = 0
    print('=-'*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(3, 5, 7, 18, 23, 6)
maior(3, 9, 1)
maior(6, 9)
maior()