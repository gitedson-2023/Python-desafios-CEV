n = int(input('Número: '))
print('Digite 1 para converter para binário.')
print('Digite 2 para converter para octal.')
print('Digite 3 para converter para hexadecimal.')
escolha = int(input('Informe sua escolha: '))
bin = bin(n)
oct = oct(n)
hex = hex(n)
if escolha == 1:
    print('{} convertido para binário é {}.' .format(n, bin[2:]))
elif escolha == 2:
    print('{} convertido para octal é {}.' .format(n, oct[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é {}.' .format(n, hex[2:]))
else:
    print('Opção inválida. Tente novamente.')