alt = float(input('Digite o valor da altura(em metros): '))
larg = float(input('Digite o valor da largura(em metros): '))
área = alt*larg
totaltinta = área/2
print('-'*170)

print('Determinada parede tem {}m de altura e {}m de largura. Sua área equivale a {} m².'. format(alt, larg, área))
print('1 litro de tinta pinta 2m², então para pintar essa parede são necessários {} litros de tinta.' .format(totaltinta))