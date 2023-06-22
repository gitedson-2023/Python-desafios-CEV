n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print('-='*50)
print(f'Foram digitados {cont} números até a parada do programa.')
print('A soma dos números informados é {}.' .format(s))
# print(f'A soma dos números informados é {s}')  --> ALÉM DE USAR O .FORMAT, PODE-SE USAR O F STRING.