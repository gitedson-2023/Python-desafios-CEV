financiamento = float(input('Qual o valor do financiamento? R$'))
salário = float(input('Qual o valor do salário? R$'))
anos =int(input('Em quantos anos o financiamento será pago? '))
mensalidade = (financiamento / anos) / 12
print('Valor da mensalidade: R${:.2f}.' .format(mensalidade))
if mensalidade > salário * 0.30:
    print('Segundo nossos cálculos, sua mensalidade excederá 30% do seu salário. Por esse motivo, seu financiamento será NEGADO.')
else:
    print('Parabéns! Seu financiamento foi APROVADO!')