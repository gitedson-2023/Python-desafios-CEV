salário = float(input('Informe o valor do salário do funcionário: R$'))
if salário > 1250:
    novosal = salário * 1.10
    print('Tal funcionário tem um salário de R${:.2f}. Receberá um aumento de 10%. Seu novo salário será de R${:.2f}.' .format(salário, novosal))
else:
    newsal = salário * 1.15
    print('Tal funcionário tem um salário de R${:.2f}. Receberá um aumento de 15%. Seu novo salário será de R${:.2f}.' .format(salário, newsal))