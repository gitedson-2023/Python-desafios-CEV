'''print('{:^50}'.format('Controle de terrenos'))
print('=-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área = l * c
print(f'A área desse terreno é {l} x {c} = {área}m²')'''

# RESOLVENDO O PROGRAMA USANDO A FUNÇÃO DEF:

def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno é de {larg} x {comp} = {a}m²')


# PROGRAMA PRINCIPAL

print('{:^30}'.format('CONTROLE DE TERRENOS'))
print('-=' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)