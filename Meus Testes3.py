# Soma de Inteiros com While
n = 15
soma = 0
while n >= 0:
 soma = soma + n
 n = n - 1
print(f'A soma dos primeiros inteiros é {soma}')

Resultado: A soma dos primeiros inteiros é 120
  
  # Contagem de letras Usando o for
p = 'araraquara'
contador = 0
for letra in p:
 if letra == 'a':
 contador = contador + 1
print(f"A palavara {p} possuí {contador} letras 'a'")

Resultado: A palavara araraquara possuí 5 letras 'a'
  
# Soma de Inteiros com While (EX 2)
n = 15
soma = 0
for num in range(n + 1):
 soma = soma + num
print(f'A soma dos primeiros {n} inteiros é {soma}')

Resultado: A soma dos primeiros 15 inteiros é 120

  
  # Realiza a busca na faixa de 250 e 300
for num in range(250, 301):
 # verifica se o número é divisível por 21
 if num % 21 == 0:
 print('Número encontrado:', num)
 # se for divísivel por 21, interrompe a busca
 break

Resultado: Número encontrado: 252
    
# cria as variáveis com as idades
p1 = 27
p2 = 49
p3 = 12
# verifica qual a maior idade
if p1 >= p2:
 if p1 >= p3:
 print('Maior idade:', p1)
elif p2 >= p3:
 print('Maior idade:', p2)
else:
 print('Maior idade:', p3)

Resultado: Maior idade: 49

# Criar lista, Indices e Slices
    lista = [2, 'a', 5.44, True, None, 'casa']
# acesso por índices
print(lista[0])
print(lista[3])
print(lista[-1])
# acesso por slices
print(lista[1:4])
print(lista[-2:])
print(lista[:])

Resultado: 
2
True
casa
['a', 5.44, True]
[None, 'casa']
[2, 'a', 5.44, True, None, 'casa']


# Criar lista, Indices e Slices (EX 2)
lista = [2, 'a', 5.44, True, None, 'casa']
# acesso por índices
print(lista[0])
print(lista[3])
print(lista[-1])
# acesso por slices
print(lista[1:4])
print(lista[-2:])
print(lista[:])

Resultado:
2
True
casa
['a', 5.44, True]
[None, 'casa']
[2, 'a', 5.44, True, None, 'casa']

# Operações de concatenação (+), repetição (*) e filiação (in)

l1 = [30, 10, 20]
l2 = [2, 'a', 5.44, True]
print(l1 + l2)
print(l1 * 3)
print(10 in l1)
# Funções úteis
print(len(l2)) # len: retorna a quantidade de elementos da lista.
print(sum(l1)) # sum: retorna a soma dos elementos de uma lista.
print(max(l1)) # max: retorna o maior elemento da lista (!!!!)
# Métodos que alteram os valores internos da lista
l2.reverse() # reverse: inverte a ordem dos elementos
print(l2)
l1.extend([10, 20, 30, 40, 10]) # extend: adiciona elementos de outra sequência
print(l1)
l1.sort() # sort: ordena os valores da lista
print(l1)
l2.insert(2, 'novo valor') # insert: adiciona um elemento em um índice especifico
print(l2)
l2.pop() # pop: remove o último elemento da lista
print(l2)
l2.clear() # clear: limpa a lista, removendo todos os elementos
print(l2)
# Métodos que retornam valores e não alteram a lista
print(l1.index(40)) # index: retorna o índice da primeira ocorrência do elemento
print(l1.count(10)) # count: conta as ocorrências do elemento
