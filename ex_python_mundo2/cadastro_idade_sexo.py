print('{:=^80}'.format(' CADASTRO DE PESSOAS '))
c = 0
dezoito = 0
h = 0
mvinte = 0
print('-=-=-=-=-= CADASTRO -=-=-=-=-=')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        dezoito += 1
    if idade < 20 and sexo in 'Ff':
        mvinte += 1
    if sexo in 'Mm':
        h += 1
    if c in 'Nn':
        break
print('-='* 70)
print(f'Foram cadastradas {dezoito} pessoas com mais de 18 anos.')
print(f'Ao todo, foram cadastrados {h} homens.')
print(f'Também foram registradas {mvinte} mulheres com menos de 21 anos.')