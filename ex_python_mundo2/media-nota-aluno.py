n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
média = (n1 + n2) / 2
print('A média foi de {}' .format(média))
if média < 5.0:
    print('O aluno está \033[1;31mREPROVADO!')
elif média >= 7.0:
    print('O aluno está \033[1;32mAPROVADO!')
else:
    print('O aluno está de \033[1;33mRECUPERAÇÃO!')
