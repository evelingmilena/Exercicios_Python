'''
Bibliotecas em Python
Numpy
Matplotlib
Scipy
'''

import numpy as np
import matplotlib.pyplot as plt


# Numpy

# Array: sao analogos aos vetores
lista1 = [30,35,40,45,50]
array1 = np.array(lista1)
print(lista1)
print(array1)

array1[1] = 5
print("Apos mudar um elemento")
print(lista1)
print(array1)

print("Multiplicacao sobre lista e array")
print(lista1*3)
print(array1*3)


# arange: intervalo entre pontos
lista2 = list(range(30,120,10))
array2 = np.arange(30,120,10) # igual o range
print(lista2)
print(array2)


# linspace: quantidade de pontos
array3 = np.linspace(30,110,9)
print(array3)


# Matrizes
matriz1_l = [[0, 1], [2, 3]]
print(matriz1_l)
print(matriz1_l[0][1])
matriz1_a = np.array(matriz1_l)
print(matriz1_a)

matriz2_a = np.array([[3,7],[9,1]])
print(matriz2_a)
matriz3_a = np.dot(matriz1_a, matriz2_a)
print(matriz3_a)


print(len(matriz1_l))
print(len(matriz1_l[0]))
print(matriz1_a.shape)
qtde_linhas = matriz1_a.shape[0]


array4 = np.arange(12)
print(array4)
matriz4_a = array4.reshape((3,4))
print(matriz4_a)


# funcoes

# np.exp, np.log, np.log10, np.sin, np.cos, 
exp_array4 = np.exp(array4)
print(exp_array4)

print(array4**3)

