time = list()
dados = {}
partidas = list()
while True:
    dados.clear()
    dados['jogador'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input('{:^35}'.format(f'Quantos gols na {p+1}ª partida? '))))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Tente novamente. Digite apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('=-'*30)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15} ', end='')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Tente novamente. Não existe jogador com o código {busca}.')
    else:
        print(f' ----> LEVANTAMENTO DO JOGADOR {time[busca] ["jogador"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   Na {i+1}ª partida, fez {g} gols.')
    print('=-'*30)
print('>>>>> VOLTE SEMPRE <<<<<')