saldo = float(input('Quanto dinheiro vc tem na sua conta? R$ '))
dólar = saldo/5.23
print('Com R${:.2f} vc pode comprar US${:.2f}.'.format(saldo, dólar))