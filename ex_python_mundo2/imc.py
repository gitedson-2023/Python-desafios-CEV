peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura * altura)
print('<>' * 30)
print('Seu IMC é de {:.2f} kg/m².' .format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc == 18 or imc < 25:
    print('Parabéns! Você está no peso ideal.')
elif imc == 25 or imc <= 30:
    print('Controle-se! Você está na categoria SOBREPESO.')
elif imc == 30 or imc <= 40:
    print('Cuidado! Você está na categoria OBESIDADE.')
else:
    print('Procure um médico! Você está com OBESIDADE MÓRBIDA!')
