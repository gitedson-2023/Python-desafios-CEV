from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Nº da CTPS (digite 0 se o usuário não tiver CTPS): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário(R$)'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)
    print('-=' * 30)
for k, v in dados.items():
    print(f'---> {k} = {v}')