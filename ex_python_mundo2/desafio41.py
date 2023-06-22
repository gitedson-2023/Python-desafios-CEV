from datetime import date
current_date = date.today()
data_nascimento = int(input('Informe a data de nascimento do atleta: '))
data_atual = current_date.year
idade = data_atual - data_nascimento
print('A idade do atleta é {} anos.' .format(idade))
if idade <= 9:
    print('Esse atleta é da categoria MIRIM.')
elif idade <= 14:
    print('Esse atleta é da categoria INFANTIL.')
elif idade <= 19:
    print('Esse atleta é da categoria JÚNIOR.')
elif idade <= 20:
    print('Esse atleta é da categoria SÊNIOR.')
else:
    print('Esse atleta é da categoria MASTER.')