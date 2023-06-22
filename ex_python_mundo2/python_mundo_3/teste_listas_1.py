'''num = [2, 4, 8, 3, 9, 7] # Exemplo de lista
num[2] = 12 # código para acrescentar o número 12 na posição 2(no lugar do 8)
num.append(13) # código para adicionar o valor 13 na última posição
num.sort(reverse=True) # num.sort para ordenar os valores em ordem crescente e reverse=True p/ ordenar em decrescente
num.insert(2, 25) # código para acrescentar o valor 25 na posição 2
num.pop(4) # código para excluir o valor na posição 4. Com os () vazios, exclui o último valor da lista
num.remove() # também exclui valores da lista

print(num)
print(f'Essa lista tem {len(num)} elementos')'''
valores = list()
'''valores.append(13)
valores.append(28)
valores.append(4)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')