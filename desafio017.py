'''catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hip = (catop**2 + catadj**2) ** (1/2)
print('Os catetos de determinado triângulo retângulo medem {} e {}. Sua hipotenusa vale {:.2f}.' .format(catop, catadj, hip))'''

import math
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}.' .format(hi))