from random import randint
import time
print('='*50)
print('{:^50}'.format('PALPITES DA MEGA-SENA'))
print('='*50)
q = int(input('Quantos jogos vc quer sortear? '))
print(f'Vou sortear {q} jogos...')
print()
for cont in range(q):
    c = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    time.sleep(1)
    print(sorted(c))
print('BOA SORTE!')