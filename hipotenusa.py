import math

catopo = int(input('Digite um valor: '))
catadj = int(input('Digite um valor: '))
hipo = math.hypot(catopo, catadj)
print('Em determinado triângulo retângulo o cateto oposto vale {} e o cateto adjacente vale {}. Logo, o valor da hipotenusa é {:.2f}.' .format(catopo, catadj, hipo))