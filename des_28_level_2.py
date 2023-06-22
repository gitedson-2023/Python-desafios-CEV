import random
tent = 0
j = 0
computador = random.randint(0, 10)
print('->'*50)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar.')
print('->'* 50)
while j != computador:
    j = int(input('Em que número pensei? '))
    tent += 1
    if j == computador:
        print('Parabéns, você acertou!')
        print('Foram necessárias {} tentativas para você acertar o número.' .format(tent))
    else:
        if j > computador:
            print('Ainda não... Pensei em um número menor.')
        if j < computador:
            print('Ainda não... Pensei em um número maior.')
