import time
print('{:=^40}'.format(' CALCULADORA DE PAGAMENTOS '))
preço = float(input('Informe o preço do produto: R$'))
print('\nDigite 1 para pagar à vista em espécie ou em cheque\nDigite 2 para pagar à vista pelo cartão de crédito\nDigite 3 para parcelar de 2x\nDigite 4 para parcelar de 3x ou mais')
print('<>' * 40)
pagamento = int(input('Informe a forma de pagamento: '))
cash = preço - (preço * 0.10)
cashcard = preço - (preço * 0.05)
twice = preço
tresx = preço * 1.20
if pagamento == 1:
    print('PROCESSANDO...')
    time.sleep(1)
    print('Você vai pagar em dinheiro em espécie, portanto ganhará 10% de desconto. O preço final será de R${:.2f}.' .format(cash))
elif pagamento == 2:
    print('PROCESSANDO...')
    time.sleep(1)
    print('Você vai pagar à vista pelo cartão de crédito, portanto ganhará 5% de desconto. O preço final será de R${:.2f}.'.format(cashcard))
elif pagamento == 3:
    parc = preço / 2
    print('PROCESSANDO...')
    time.sleep(1)
    print('Você vai pagar parcelado de 2x de R${:.2f} no cartão de crédito, portanto não haverá desconto na sua compra.\nVocê pagará R${:.2f} sem juros.' .format(parc, preço))
elif pagamento == 4:
    parcelas = int(input('Vai pagar de quantas vezes? '))
    parc = preço / parcelas
    print('PROCESSANDO...')
    time.sleep(1)
    print('Você irá pagar parcelado de {}x pelo cartão de crédito, portanto será acrescido 20% de juros ao preço inicial.\nSerão {} parcelas de R${:.2f}. O preço final será de R${:.2f}.' .format(parcelas, parcelas, parc, tresx))
else:
    print('\033[1;31mOpção inválida! Tente novamente.')
