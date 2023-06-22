from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
            'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []
print('{:^40}'.format('Valores sorteados:'))
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou {v}')
print()
print('{:^40}'.format('Ranking dos jogadores:'))
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'Na {i+1}ª posição: {v[0]} que tirou {v[1]}')