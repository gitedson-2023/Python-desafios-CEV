num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} vemos que...' .format(num))
print('A unidade vale {}' .format(u))
print('A dezena vale {}' .format(d))
print('A centena vale {}' .format(c))
print('A milhar vale {}' .format(m))
