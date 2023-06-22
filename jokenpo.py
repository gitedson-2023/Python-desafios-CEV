import random
import time
opções = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
print('<>' * 50)
print('Vamos jogar jokenpô. Tente adivinhar qual eu escolhi.')
print('')
print('Escolha uma opção:')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
print('<>' * 50)
jogador =int(input('Qual eu escolhi? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(0)
if jogador == computador:
    print('\033[1;33mDeu ruim. Ninguém venceu. Eu escolhi {} e vc também escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 0 and computador == 2:
    print('\033[1;32mVocê venceu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 0 and computador == 1:
    print('\033[1;31mVocê perdeu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 1 and computador == 2:
    print('\033[1;31mVocê perdeu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 1 and computador == 0:
    print('\033[1;32mVocê venceu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 2 and computador == 1:
    print('\033[1;32mVocê venceu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
elif jogador == 2 and computador == 0:
    print('\033[1;31mVocê perdeu! Eu escolhi {} e vc escolheu {}.' .format(opções[computador], opções[jogador]))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA!')
