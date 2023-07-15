r1 = float(input('Informe o tamanho de um segmento de reta: '))
r2 = float(input('Informe o tamanho de um segmento de reta: '))
r3 = float(input('Informe o tamanho de um segmento de reta: '))
print('*' * 80)
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os segmentos de reta {}, {} e {} PODEM formar um triângulo.' .format(r1, r2, r3))
else:
    print('Os segmentos de reta informados informados NÃO PODEM formar um triângulo.')