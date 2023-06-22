n = str(input('Nome completo: ')).strip()
nome = n.split()
print('Muito Prazer, \033[1;4;36m{}\033[m. \nSeu primeiro nome é \033[1;33m{}\033[m.' .format(n, nome[0]))
print('Seu último nome é \033[1;32m{}\033[m.' .format(nome[len(nome)-1]))
