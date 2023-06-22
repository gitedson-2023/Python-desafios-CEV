v = float(input('Informe a velocidade em km/h: '))
if v > 80:
    multa = (v-80) * 7
    print('QUE PENA! VC SERÁ MULTADO POR TER ULTRAPASSADO O LIMITE DE VELOCIDADE, QUE É DE 80 KM/H.')
    print('O VALOR DA SUA MULTA É DE R${:.2f}.' .format(multa))
print('<>'*50)
print('DIRIJA COM SEGURANÇA!')