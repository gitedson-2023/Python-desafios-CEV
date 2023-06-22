
from datetime import date
current_date = date.today()
data_nascimento = int(input('Informe sua data de nascimento: ')) # código para retornar a idade atual
data_atual = current_date.year
idade = data_atual - data_nascimento
print('Sua idade é {} anos.' .format(idade))
if idade < 18:
    faltam = 18 - idade
    anoalist = data_atual + faltam
    print('Você ainda vai se alistar nas Forças Armadas.')
    print('Faltam {} anos para vc se alistar.' .format(faltam))
    print('Seu alistamento será em {}.' .format(anoalist))
elif idade == 18:
    print('Jovem, está na hora de se alistar!')
else:
    passou = idade - 18
    anoalist = data_nascimento + 18
    print('Já se passaram {} anos desde quando vc se alistou.' .format(passou))
    print('Vc se alistou no ano de {}.' .format(anoalist))