import modulos
preco = float(input('Digite um preço: R$'))
print(f'A metade de {modulos.moeda(preco)} é {modulos.moeda(modulos.metade(preco))}')
print(f'O dobro de {modulos.moeda(preco)} é {modulos.moeda(modulos.dobro(preco))}')
print(f'Aumentando {modulos.moeda(preco)} em 15%, temos {modulos.moeda(modulos.aumento(preco))}')
print(f'Diminuindo 30% de {modulos.moeda(preco)}, temos R${preco - modulos.reducao(preco)}')
modulos.resumo(preco)