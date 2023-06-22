'''teste = list()
teste.append('Edson')
teste.append(28)
familia = list()
familia.append(teste[:])
teste[0] = 'Débora'
teste[1] = 45
teste[2] = 'Marcos'
teste[3] = 52
familia.append(teste[:])
print(familia)'''

familia = [['Débora', 46], ['Marcos', 53], ['Douglas', 25], ['Dayane', 23], ['Gabriel', 24], ['Clarisse', 5], ['Edson', 29]]
#print(familia[0] [0])
for p in familia:
    print(p[0])