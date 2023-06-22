s = 0
lista = []
print('')
print('********** Digite [M] para Masculino e [F] para Femenino **********')
print('')
s = str(input('Digite o sexo da pessoa: ')).strip().lower()
lista = ['m', 'f', 'M', 'F']
while s not in lista:
    s = str(input('Digite uma opção válida [M ou F]: ')).strip().lower()
if s == 'm':
    print('Sexo [MASCULINO] registrado')
if s == 'f':
    print('Sexo [FEMENINO] registrado.')

