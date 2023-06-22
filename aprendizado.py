s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n # também pode ser escrito s += n
print('A soma dos valores é {}.' .format(s))