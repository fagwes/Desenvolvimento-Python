# Verifica Maior e Menor idade
idades = [27, 49, 12, 67, 21, 32, 18, 45, 84, 53, 22, 56, 80, 35, 18]
print('Maior idade:', max(idades))
print('Menor idade:', min(idades))

Resultado: 
Maior idade: 84
Menor idade: 12

# Criação dos conjuntos A e B
c1 = {1, 2, 3, 4, 5}
c2 = {4, 5}
c3 = {91, 92, 93}
# Adiciona um elemento ao conjunto
c1.add(6)
print(c1)
# Adiciona os elementos de uma sequência iterável
c1.update([2, 4, 6, 8])
print(c1)
# Descarta um elemento do conjunto,
c1.discard(8)
print(c1)
# Diferentemente do set.remove(), o discard não gera um erro
# se o elmento a ser removido não existir
c1.discard(99)
print(c1)
# Verifica se os conjuntos são disjuntos, ou seja,
# se não possuem nenhum elemento em comum
print(c1.isdisjoint(c2))
print(c1.isdisjoint(c3))
# Verifica se o conjunto é subconjunto de outro
print(c1.issubset(c2))
print(c2.issubset(c1))
# Verifica se o conjunto contém outro conjunto (superset)
print(c1.issuperset(c2))
print(c2.issuperset(c1))

Resul:
  {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6, 8}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
False
True
False
True
True
False

# Criação das listas de alunos das turmas
ING = ['Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna']
ESP = ['Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui']
FRA = ['Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina']
# Concatenação de todas as listas de alunos
ALL = ING + ESP + FRA
# Ordenação para melhor visualização
ALL.sort()
# Exibição do resultado
print('Relação de todos os alunos da escola:')
print(ALL)

Resultado:
  Relação de todos os alunos da escola:
['Ana', 'Artur', 'Beatriz', 'Bruna', 'Bruna', 'Bruna', 'Caio', 'Caio', 'Carolina', 'Carolina', 'Flávia', 'Flávia', 'Gabriel', 'Juliano',
'Juliano', 'Maria', 'Maria', 'Maria', 'Paula', 'Pedro', 'Rubens', 'Rui', 'Rui', 'Tiago']


