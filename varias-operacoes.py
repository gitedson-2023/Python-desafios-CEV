n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
adi = n1 + n2
sub = n1-n2
mul = n1*n2
div = n1/n2
dint = n1//n2
rest = n1%n2
pot = n1**n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.2f}, a divisão inteira é {}, o resto da divisão é {} '. format(adi, sub, mul, div, dint, rest), end='')
print('e a potenciação é {}.'. format(pot))
