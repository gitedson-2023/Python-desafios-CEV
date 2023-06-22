from datetime import date
current_date = date.today()
data_atual = current_date.year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa. '. format(c)))
    idade = data_atual - n
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('*' * 90)
print('Ao todo foram analisadas {} pessoas, {} maiores de idade e {} menores de idade.' .format(c, totmaior, totmenor))


