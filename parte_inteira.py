import math
n = float(input('Digite um número "quebrado" e veja sua parte inteira: '))
print('A parte inteira de {} é \033[1;33m{}\033[m.' .format(n, math.trunc(n)))