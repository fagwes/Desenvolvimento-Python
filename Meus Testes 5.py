#Funções

#Função Soma

# define as listas com os números a serem somados
l1 = [1, 2, 3, 4, 5]
l2 = [3, 1, 5, 9, 0, 8, 2, 3, 4]
l3 = [12, 43, 23, 12, 789]
# itera sobre cada lista e soma seus elementos
soma_l1 = 0
for item in l1:
 soma_l1 = soma_l1 + item
soma_l2 = 0
for item in l2:
 soma_l2 = soma_l2 + item
soma_l3 = 0
for item in l3:
 soma_l3 = soma_l3 + item
# exibe os resultados
print(f'Resultado: l1={soma_l1}, l2={soma_l2}, l3={soma_l3}')

Resultado: l1=15, l2=35, l3=879
  
  

# Função Calcula Àrea do Triângulo

# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura):
 return (base * altura)/2
print(area_triangulo(5, 10))

Resultado: 25.0
  
# Função Exibe Nomes

def exibe_pessoa(nome, idade=30):
 print(f'Meu nome é {nome} e tenho {idade} anos.')
exibe_pessoa('Antônio')
exibe_pessoa('Antônio', 36)

Resultado:
Meu nome é Antônio e tenho 30 anos.
Meu nome é Antônio e tenho 36 anos.

