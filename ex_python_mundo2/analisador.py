somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for a in range(1, 5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(a))).upper()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: '))
    somaidade += idade
    print('*'* 90)
    if a == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.' .format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo, são {} mulheres com menos de 20 anos de idade.'.format(totmulher20))

