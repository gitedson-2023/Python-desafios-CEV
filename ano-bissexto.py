import datetime
ano = int(input('Informe um ano para saber se ele é bissexto. Digite 0 para saber se o ano atual é bissexto ou não. '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0: # Expressão para saber se um ano é bissexto.
    print(f'O ano de {ano} é BISSEXTO.')
else:
    print(f'O ano de {ano} não é BISSEXTO.')
