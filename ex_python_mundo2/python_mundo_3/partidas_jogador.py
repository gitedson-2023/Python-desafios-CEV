import math
dados = {}
partidas = list()
dados['Jogador'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
for p in range(0, tot):
    partidas.append(int(input('{:^35}'.format(f'Quantos gols na {p+1}ª partida? '))))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'{k} = {v}')
print('=-'*30)
print(f'O jogador {dados["Jogador"]} jogou {len(dados["gols"])} partidas.')
print('=-'*30)
for i, v in enumerate(dados['gols']):
    print(f'      ===> Na {i+1}ª partida, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
