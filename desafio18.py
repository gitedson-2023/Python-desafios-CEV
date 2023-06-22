import math

a = int(input('Informe o valor de um ângulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Determinado ângulo mede {}.\n \nSeu seno vale {:.3f}, \no cosseno vale {:.3f} \ne a tangente vale {:.3f}.' .format(a, s, c, t))
