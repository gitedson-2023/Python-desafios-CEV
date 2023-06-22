d = float(input('Informe a distância em km: '))
if d <= 200:
    p1 = 0.50
    valortotal = d * p1
    print('Você vai fazer uma viagem de {} km. Sua passagem custará R${:.2f}.' .format(d, valortotal))
else:
    p2 = 0.45
    vtotal = d * p2
    print('Você vai fazer uma viagem de {} km. Sua passagem custará R${:.2f}.' .format(d, vtotal))
