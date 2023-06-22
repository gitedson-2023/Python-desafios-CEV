import random
n1 = input('Digite o nome da pessoa: ')
n2 = input('Digite o nome da pessoa: ')
n3 = input('Digite o nome da pessoa: ')
n4 = input('Digite o nome da pessoa: ')
lista = [n1, n2, n3, n4]
sorteado = random.choice (lista)
print('O nome sorteado foi {}.' .format(sorteado))