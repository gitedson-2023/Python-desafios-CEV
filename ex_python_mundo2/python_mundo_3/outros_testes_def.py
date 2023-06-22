def soma(a, b, c=0):   # c = 0 é o parâmetro padrão caso o terceiro valor não seja informado dentro da função soma.
    s = a + b + c
    #print(f'A soma dos valores é {s}')
    return s


r1 = soma(12, 3, 75)
r2 = soma(6, 7, 86)
r3 = soma(3, 5, 63)
r4 = soma(2, 5)
print(f'Os resultados das somas foram {r1}, {r2}, {r3} e {r4}')