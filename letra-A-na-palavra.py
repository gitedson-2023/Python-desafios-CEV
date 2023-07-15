word = str(input('Informe uma palavra: ')).upper().strip()
a = word.count('A')

print('Na palavra digitada, a letra A aparece {} vezes.' .format(a))
print('O primeiro A aparece na posição {}.' .format(word.find('A')+1))
print('O último A aparece na posição {}.' .format(word.rfind('A')+1))