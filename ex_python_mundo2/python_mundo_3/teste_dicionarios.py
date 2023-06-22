# INTRODUÇÃO A DICIONÁRIOS

'''familia = {}
familia = dict() ----> uma outra forma de declarar um dicionário
familia = {'nome': 'Débora', 'sexo': 'F', 'idade': 45}
#del familia['sexo'] -------> comando para apagar uma 'KEY'.
#familia['nome'] = 'Dayane' --------> comando para trocar de 'VALUE'.
#familia['peso'] = 60.3 ---------> comando para adicionar uma 'KEY'.
#print(f'O nome da minha mãe é {familia["nome"]} e ela tem {familia["idade"]} anos.')
#print(familia.keys())
#print(familia.values())
#print(familia.items())
for k in familia.items():
    print(k)
for k, v in familia.items():
    print(f'{k} = {v}')'''

# COLOCANDO DICIONÁRIOS DENTRO DE LISTAS

'''brasil = []
estado1 = {'uf': 'Pará', 'sigla': 'PA'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Nome de estado: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)