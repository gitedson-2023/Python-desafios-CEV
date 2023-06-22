# MINHA RESOLUÇÃO

'''from datetime import datetime
def voto():
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade > 15 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade > 17 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')


ano = int(input('Em que ano você nasceu? '))
voto()'''

# RESOLUÇÃO DO CURSO EM VÍDEO

def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))


