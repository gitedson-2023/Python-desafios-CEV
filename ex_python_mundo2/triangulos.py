c1 = float(input('Informe o comprimento de um segmento de reta: '))
c2 = float(input('Informe o comprimento de um segmento de reta: '))
c3 = float(input('Informe o comprimento de um segmento de reta: '))
if c1 < c2 + c3 and c2 < c3 + c1 and c3 < c2 + c1 and c1 != c2 and c1 != c3 and c2 != c3:
    print('Os segmentos de reta informados podem formar um triângulo ESCALENO.') # todos os lados diferentes.
elif c1 == c2 and c1 == c3 and c2 == c3:
    print('Os segmentos de reta informados podem formar um triângulo EQUILÁTERO.') # todos os lados iguais.
elif c1 == c2 or c1 == c3 or c2 == c3:
    print('Os segmentos de reta informados podem formar um triângulo ISÓSCELES.') # dois lados iguais.
else:
    print('Os segmentos de reta informados NÃO PODEM formar um triângulo.')