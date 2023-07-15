sal = float(input('Digite o valor do salário: R$'))
au = sal*1.15
print('-'*200)
print('Fulano recebe R${:.2f} por mês. Foi promovido e terá um aumento de salário de 15%. Seu novo salário será de R${:.2f}.' .format(sal, au))