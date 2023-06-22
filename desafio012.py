preço = float(input('Digite o preço do produto: R$'))
desc = preço*0.05
novopreço = preço-(preço*0.05)
print('-'*200)
print('Determinado produto custa R${:.2f}. Este produto está na promoção, com 5% de desconto. Seu novo preço será de R${:.2f}.' .format(preço, novopreço))