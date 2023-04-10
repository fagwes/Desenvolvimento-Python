#Verifica nota e falta se foi aprovado ou reprovado

aluno = 'Wesley'
print('Nome do aluno:',aluno)

nota1 = 10
nota2 = 8
nota3 = 10
nota4 = 4

media = (nota1+nota2+nota3+nota4)/4
falta = 2

if media>6 and falta<=5:
  print('Aprovado')
else:
  print('Reprovado')  

Resultado:
Nome do aluno: Wesley
Aprovado

# Conceito de slicing

palavra = 'consolação'
# consola
print(palavra[:7])
# sol
print(palavra[3:6])
# sola
print(palavra[3:7])
# ação
print(palavra[-4:])
# palavra original
print(palavra[:])

Resultado:
consola
sol
sola
ação
consolação

#Exemplo 2:
palavra = 'Wesley' 
palavra1 = 'Amorim'

print(palavra[0:3])
print(palavra[3:6])
print(palavra1[0:3])
print(palavra1[3:6])

Resultado:
Wes
ley
Amo
rim

# Concatenação e Repetição:

s1 = 'Wesley'
s2 = 'Amorim'

# Concatenação (+)
print(s1 + s2)
print(s1 + ' ' + s2)
print(s1 + ' Gomes')

# Repetição
print(s1 * 5)
print((s1 + ', ') * 4)

Resultado:
WesleyAmorim
Wesley Amorim
Wesley Gomes
WesleyWesleyWesleyWesleyWesley
Wesley, Wesley, Wesley, Wesley, 

# Contador de digitos

nome = 'Deus seja sempre louvado Amém'
print(len(nome))

Resultado:
29  


# Verifica se uma pessoa está apta para se aposentar
idade = 20
tempo_contrib = 20
if idade >= 65 or tempo_contrib >= 35:
 print('Habilitado para solicitar aposentadoria!')
else:
 print('Não habilitado para solicitar aposentadoria!')

Resultado: Não habilitado para solicitar aposentadoria

  
# Verifica se uma pessoa está apta para se aposentar
idade = 20
tempo_contrib = 20
if idade >= 65:
 print('Habilitado para aposentadoria por idade!')
else:
 if tempo_contrib >= 35:
 print('Habilitado para aposentadoria por tempo de contribuição!')
 else:
 print('Não habilitado para solicitar aposentadoria!')  
  
Resultado: Não habilitado para solicitar aposentadoria
  
# Verifica faixa etária: Criança, Adolescente, Adulto e Idoso
idade = 22
if idade < 12:
 faixa_etaria = 'Criança'
else:
 if idade < 18:
 faixa_etaria = 'Adolescente'
 else:
 if idade < 60:
 faixa_etaria = 'Adulto'
 else:
 faixa_etaria = 'Idoso'
print('Faixa Etária: ', faixa_etaria)
  


