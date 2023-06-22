import random
import time
computador = random.randint(0, 5) # Comando para fazer o computador sortear um número entre 0 e 5.
print('='*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('='*50)
jogador = int(input('Em que número pensei? ')) # O jogador tenta adivinhar o número.
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('\033[1;33mParabéns! Vc acertou o número!')
else:
    print('\033[1;31mVc errou! Eu pensei no número {} e não no número {}.' .format(computador, jogador))