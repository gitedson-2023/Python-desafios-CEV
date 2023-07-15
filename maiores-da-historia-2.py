goats = ['Messi', 'Pelé', 'Maradona']
j = str(input('Informe o nome do jogador: '))
print('<>' * 25)
if j in goats:
    print('\033[1;34mEsse jogador é um dos 3 maiores da história.')
else:
    print('\033[1;31mEsse jogador não está no Olimpo do futebol.')