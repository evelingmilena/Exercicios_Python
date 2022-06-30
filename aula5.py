# Uma lista e uma variavel que guarda outras variaveis

# Lista de compras de supermercado
print("Lista de compras")
lista_de_compras = ["leite","ovos","acucar"]
print(lista_de_compras)

# Atualizar listas com novos valores
lista_de_compras.append("carne")
print(lista_de_compras)


# Lista das notas da turma de um professor
print("\nLista das notas da turma")
lista_notas = [7, 8, 9.5, 3, 8.5]
print(lista_notas)
lista_de_alunos = ["pedro","laura","gustavo","amanda", "regiane"]
print(lista_de_alunos)

# Pegar um elemento da lista
# Comeca em 0 e termina em N-1 (N elementos)
nome = lista_de_alunos[2]
nota = lista_notas[2]
print("\nA nota do aluno",nome,"e",nota)

# Pegar mais de um elemento da lista
print("Alguns alunos da turma",lista_de_alunos[1:4]) # start:stop
print("Alguns alunos da turma",lista_de_alunos[1:4:2]) #start:stop:step

# Alterar um elemento da lista (ex. corrigir a nota)
lista_notas[4] = 8.75
print(lista_notas)

# Pegar o tamanho de uma lista
qtde_alunos = len(lista_de_alunos)
print("\nHa",qtde_alunos,"alunos na turma")

# Fazer a media da turma
soma = 0
for i in range(qtde_alunos):
    soma = soma+lista_notas[i]
media = soma/qtde_alunos
print("\nA media da turma e",media)


# Quando a gente tem outras variaveis (int, float, string)
var1 = 5.5
var2 = var1
var1 = var1+7 # atualizei var1
var2 = var2*2 # atualizei var2
print(var1,var2)

# Com listas
lista1 = [2, 4, 5]
lista2 = lista1
lista1[2] = 27
print(lista1)
print(2*lista2[2])


# Simples: criar uma lista vazia [] e ir colocando os elementos um a um
lista_vazia = []


# Direta: lista[::]
lista1 = [2, 4, 5]
lista2 = lista1[::]
lista1[2] = 27
print(lista1)
print(2*lista2[2])


# Tarefas:
# fazer o for do plot do alpha
# fazer a criacao de uma nova lista a partir de outra antiga da maneira simples
# Descobrir o que a operacao de + faz com as listas 
