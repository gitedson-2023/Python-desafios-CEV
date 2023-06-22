print('{:=^70}'.format(' PRODUTOS '))
c = 0
soma = 0
p = 0
qtd = 0
cont = 0
while True:
    p = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    c = ' '
    barato = ''
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N} ')).strip().upper()[0]
    soma += preço
    cont += 1
    print('-='*50)
    if preço > 1000:
        qtd += 1
    if cont == 1:
        menor = preço
        barato = p
    else:
        if preço < menor:
            menor = preço
            barato = p
    if c in 'Nn':
        break
print(f'A soma dos valores de todos os produtos é R${soma:.2f}')
print(f'Ao todo, {qtd} produtos custam mais de R$1000.')
print(f'O produto com o menor preço é {barato} e custa R${menor:.2f}')