medida = float(input('Digite uma medida em metros: '))
cen = medida * 100
mil = medida * 1000
km = medida/1000
print('A medida de', medida, 'metros em centímetros é {}cm \nem milímetros é {}mm \ne é {} em km'. format(cen, mil, km))
