frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1): # OUTRA FORMA DE CONSEGUIR O INVERSO DA PALAVRA É USANDO O CÓDIGO: INVERSO = JUNTO[::-1]
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {}. Temos um PALÍNDROMO!'.format(junto, inverso))
else:
    print('Essa frase não é um PALÍNDROMO.')
