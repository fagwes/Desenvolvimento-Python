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


