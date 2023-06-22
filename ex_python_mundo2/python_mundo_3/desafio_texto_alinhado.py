def alinhado(txt):
    tam = len(txt) + 4  # conta usada para alinhar o caractere ao tamanho do texto
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa Principal

alinhado('Edson Soares')
alinhado('FC Barcelona')
alinhado('São Paulo FC')
alinhado('Golden State Warriors')